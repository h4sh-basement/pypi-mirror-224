import logging
import time
import traceback
from fastapi import APIRouter
import rdflib

from cognite.neat.graph.transformations import query_generator

from cognite.neat.app.api.configuration import neat_app, cache_store
from cognite.neat.app.api.data_classes.rest import NodesAndEdgesRequest, QueryRequest, RuleRequest
from cognite.neat.app.api.asgi.metrics import counter
from cognite.neat.app.api.utils.data_mapping import rdf_result_to_api_response
from cognite.neat.app.api.utils.query_templates import query_templates


router = APIRouter()


@router.get("/api/list-queries")
def list_queries():
    counter.inc()
    return query_templates


@router.post("/api/get-nodes-and-edges")
def get_nodes_and_edges(request: NodesAndEdgesRequest):
    logging.info("Querying graph nodes and edges :")
    if "get_nodes_and_edges" in cache_store and request.cache:
        return cache_store["get_nodes_and_edges"]
    nodes_result = {}
    edges_result = {}
    query = ""
    elapsed_time_sec = 0
    """
    "nodes": [
        {
            "node_id": "http://purl.org/nordic44#_a63ce14e-fba0-4f9e-8b59-7ef2fe887ff8",
            "node_class": "http://entsoe.eu/CIM/SchemaExtension/3/2#RateTemperature",
            "node_name": "-5degreeCelsius"
        }],
    "edges": [
        {
            "src_object_ref": "http://purl.org/nordic44#_f1769eaa-9aeb-11e5-91da-b8763fd99c5f",
            "conn": "http://iec.ch/TC57/2013/CIM-schema-cim16#OperationalLimitSet.Terminal",
            "dst_object_ref": "http://purl.org/nordic44#_2dd90186-bdfb-11e5-94fa-c8f73332c8f4"
        },
    """
    if request.sparql_query:
        mixed_result = get_data_from_graph(request.sparql_query, request.graph_name, request.workflow_name)

        edges_result = []
        nodes_result = []
        try:
            nodes_result = [
                {
                    "node_id": v[rdflib.Variable("node_id")],
                    "node_class": v[rdflib.Variable("node_class")],
                    "node_name": v[rdflib.Variable("node_name")],
                }
                for v in mixed_result["rows"]
            ]
        except Exception as e:
            logging.error(f"Error while parsing nodes : {e}")

        try:
            edges_result = [
                {
                    "src_object_ref": v[rdflib.Variable("src_object_ref")],
                    "dst_object_ref": v[rdflib.Variable("dst_object_ref")],
                }
                for v in mixed_result["rows"]
                if rdflib.Variable("src_object_ref") in v and rdflib.Variable("dst_object_ref") in v
            ]
        except Exception as e:
            logging.error(f"Error while parsing edges : {e}")

        query = request.sparql_query
        elapsed_time_sec = mixed_result["elapsed_time_sec"]
    else:
        nodes_filter = ""
        edges_dst_filter = ""
        edges_src_filter = ""

        if len(request.node_class_filter) > 0:
            nodes_filter = "VALUES ?node_class { " + " ".join([f"<{x}>" for x in request.node_class_filter]) + " }"

        node_name_property = request.node_name_property or "cim:IdentifiedObject.name"
        nodes_query = f"SELECT DISTINCT ?node_id ?node_class ?node_name WHERE \
        {{ {nodes_filter} \
        ?node_id {node_name_property} ?node_name . ?node_id rdf:type ?node_class }} "
        if len(request.src_edge_filter) > 0:
            edges_src_filter = (
                "VALUES ?src_object_class { " + " ".join([f"<{x}>" for x in request.src_edge_filter]) + " }"
            )
        if len(request.dst_edge_filter) > 0:
            edges_dst_filter = (
                "VALUES ?dst_object_class { " + " ".join([f"<{x}>" for x in request.dst_edge_filter]) + " }"
            )

        edges_query = f"SELECT  ?src_object_ref ?conn ?dst_object_ref \
            WHERE {{ \
            {edges_src_filter} \
            {edges_dst_filter} \
            ?src_object_ref ?conn  ?dst_object_ref . \
            ?src_object_ref  rdf:type ?src_object_class . \
            ?dst_object_ref  rdf:type ?dst_object_class .\
            }} "
        nodes_query = f"{nodes_query} LIMIT {request.limit}"
        edges_query = f"{edges_query} LIMIT {request.limit}"
        logging.info(f"Nodes query : {nodes_query}")
        logging.info(f"Edges query : {edges_query}")
        nodes_result = get_data_from_graph(nodes_query, request.graph_name, request.workflow_name)
        edges_result = get_data_from_graph(edges_query, request.graph_name, request.workflow_name)
        elapsed_time_sec = nodes_result["elapsed_time_sec"] + edges_result["elapsed_time_sec"]
        query = nodes_query + edges_query
        nodes_result = nodes_result["rows"]
        edges_result = edges_result["rows"]

    merged_result = {
        "nodes": nodes_result,
        "edges": edges_result,
        "error": "",
        "elapsed_time_sec": elapsed_time_sec,
        "query": query,
    }

    if request.cache:
        cache_store["get_nodes_and_edges"] = merged_result
    return merged_result


@router.post("/api/query")
def query_graph(request: QueryRequest):
    logging.info(f"Querying graph {request.graph_name} with query {request.query}")
    sparq_query = request.query
    return get_data_from_graph(sparq_query, request.graph_name, workflow_name=request.workflow_name)


@router.post("/api/execute-rule")
def execute_rule(request: RuleRequest):
    logging.info(
        f"Executing rule type: { request.rule_type } rule : {request.rule} , workflow : {request.workflow_name} , "
        f"graph : {request.graph_name}"
    )
    # TODO : add support for other graphs
    workflow = neat_app.workflow_manager.get_workflow(request.workflow_name)
    if not workflow.source_graph or not workflow.solution_graph:
        workflow.step_load_transformation_rules()
        workflow.step_configuring_stores()
    if request.graph_name == "source":
        if not workflow.source_graph:
            logging.info("Source graph is empty , please load the graph first")
            return {"error": "source graph is empty , please load the graph first"}
        graph = workflow.source_graph
    elif request.graph_name == "solution":
        if not workflow.solution_graph:
            logging.info("Solution graph is empty , please load the graph first")
            return {"error": "solution graph is empty , please load the graph first"}
        graph = workflow.solution_graph
    else:
        raise Exception("Unknown graph name")

    if request.rule_type == "rdfpath":
        start_time = time.perf_counter()
        sparq_query = query_generator.build_sparql_query(
            graph, request.rule, prefixes=workflow.transformation_rules.prefixes
        )
    else:
        logging.error("Unknown rule type")
        return {"error": "Unknown rule type"}
    stop_time = time.perf_counter()
    elapsed_time_sec_1 = stop_time - start_time
    logging.info(f"Computed query : {sparq_query} in {elapsed_time_sec_1 * 1000} ms")

    api_result = get_data_from_graph(sparq_query, request.graph_name, workflow_name=request.workflow_name)
    api_result["elapsed_time_sec"] += elapsed_time_sec_1
    return api_result


@router.get("/api/object-properties")
def get_object_properties(reference: str, graph_name: str = "source", workflow_name: str = "default"):
    logging.info(f"Querying object-properties from {graph_name} :")
    query = f"SELECT ?property ?value WHERE {{ <{reference}> ?property ?value }} ORDER BY ?property"
    return get_data_from_graph(query, graph_name, workflow_name=workflow_name)


@router.get("/api/search")
def search(
    search_str: str, graph_name: str = "source", search_type: str = "value_exact_match", workflow_name: str = "default"
):
    logging.info(f"Search from {graph_name} :")
    if search_type == "reference":
        query = (
            f"SELECT ?class ?reference WHERE {{ {{?reference ?class <{search_str}> . }} "
            f"UNION {{ <{search_str}> ?class ?reference }} }} limit 10000"
        )

    elif search_type == "value_exact_match":
        query = (
            f"select ?object_ref ?type ?property ?value where "
            f"{{ ?object_ref ?property ?value . ?object_ref rdf:type ?type . "
            f'FILTER(?value="{search_str}") }} limit 10000'
        )
    elif search_type == "value_regexp":
        query = (
            f"select ?object_ref ?type ?property ?value where "
            f"{{ ?object_ref ?property ?value . ?object_ref rdf:type ?type .  "
            f'FILTER regex(?value, "{search_str}","i") }} limit 10000'
        )
    return get_data_from_graph(query, graph_name, workflow_name=workflow_name)


@router.get("/api/get-classes")
def get_classes(graph_name: str = "source", workflow_name: str = "default", cache: bool = True):
    logging.info(f"Querying graph classes from graph name : {graph_name}, cache : {cache}")
    cache_key = f"classes_{graph_name}"
    if cache_key in cache_store and cache:
        return cache_store[cache_key]
    query = (
        "SELECT ?class (count(?s) as ?instances ) WHERE { ?s rdf:type ?class . } "
        "group by ?class order by DESC(?instances)"
    )
    api_result = get_data_from_graph(query, graph_name, workflow_name)
    cache_store["get_classes"] = api_result
    return api_result


def get_data_from_graph(sparq_query: str, graph_name: str = "source", workflow_name: str = "default"):
    total_elapsed_time = 0
    api_result = {"error": ""}
    result = None

    try:
        logging.info(f"Preparing query :{sparq_query} ")
        start_time = time.perf_counter()
        workflow = neat_app.workflow_manager.get_workflow(workflow_name)
        try:
            if not workflow.source_graph or not workflow.solution_graph:
                workflow.step_load_transformation_rules()
                workflow.step_configuring_stores(clean_start=False)
        except Exception as e:
            logging.debug(f"Error while loading transformation rules or stores : {e}")

        if graph_name == "source":
            if workflow.source_graph:
                result = workflow.source_graph.query(sparq_query)
            else:
                logging.info("Source graph is empty , please load the graph first")
                api_result["error"] = "source graph is empty , please load the graph first"
        elif graph_name == "solution":
            if workflow.solution_graph:
                result = workflow.solution_graph.query(sparq_query)
            else:
                logging.info("Solution graph is empty , please load the graph first")
                api_result["error"] = "solution graph is empty , please load the graph first"
        else:
            raise Exception("Unknown graph name")

        stop_time = time.perf_counter()
        elapsed_time_sec_1 = stop_time - start_time
        logging.info(f"Query prepared in {elapsed_time_sec_1 * 1000} ms")

        start_time = time.perf_counter()
        if result:
            api_result = rdf_result_to_api_response(result)
        stop_time = time.perf_counter()
        elapsed_time_sec_2 = stop_time - start_time
        total_elapsed_time = elapsed_time_sec_1 + elapsed_time_sec_2
    except Exception as e:
        logging.error(f"Error while executing query :{e}")
        traceback.print_exc()
        api_result["error"] = str(e)

    api_result["query"] = sparq_query
    api_result["elapsed_time_sec"] = total_elapsed_time
    logging.info(f"Data fetched in {total_elapsed_time * 1000} ms")
    return api_result
