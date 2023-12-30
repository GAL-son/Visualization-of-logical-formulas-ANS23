from statement import Statement
import utils as ut
from methods.resolution_graph import build_resolution_graph

def resolution_graph_reduction(statement: Statement, red_strength=2): 
    """This mmethod builds a resolution graph for given statement
    and then reduces it based on given reduction strength
    """

    graph = build_resolution_graph(statement)
    # print(graph) #DEBUG

    reduced_graph = reduce_graph(graph, red_strength)

    # print(reduced_graph) # DEBUG

    return reduced_graph

def reduce_graph(graph, red_strength): 
    """It simplifies the graf by grouping connected nodes based on number of connections to different nodes
    """

    standard_nodes = []
    node_groups = []

    for node in graph:
        # print(node) #DEBUG

        if len(node["edges"]) > red_strength:
            # build standard node
            # new_node = {"index": node["index"], "name": node["name"], "edges": node["edges"]}
            # print(node) # DEBUG
            standard_nodes.append(node)
            continue

        # build node group
        # print("CHAIN NODE") # DEBUG

        # Check if current node is connected with any node groups
        connected_groups = []
        for ng in node_groups:
            ng_nodes = ng["index"]
            inter = ut.intersection(node["edges"], ng_nodes)            

            if len(inter) != 0:
                # print("CONNECTED GROUPS")
                connected_groups.append(ng)

        # Incorporate node in node groups
        if len(connected_groups) == 0:
            new_ng = create_node_group(node)
            # print(f"NEW GROUP: {new_ng}") # DEBUG
            node_groups.append(new_ng)
            # Append new node group to array
        elif len(connected_groups) == 1:
            new_ng = add_node_to_group(node, connected_groups[0])
            # Update old node group
        else: 
            new_ng = merge_groups_with_node(connected_groups, node)
            # Replace merged node groups with a new one  

    # print(node_groups) # DEBUG
    # print(standard_nodes) # DEBUG

    # Re-index graph
    new_graph = []
    for index, node in enumerate(standard_nodes):
        node["name"] = f"C{index}"
        new_graph.append(node)

    for index, group in enumerate(node_groups):
        group["name"] = f"G{index}"
        new_graph.append(group)

    for node in new_graph:
        node_edges = node["edges"]
        new_edges = []

        for edge in node_edges:
            for i, check_node in enumerate(new_graph):
                if edge in check_node["index"]: 
                    # Update new node
                    new_edges.append(i)

        node["edges"] = new_edges
        
    new_graph = ut.graph_drop_index(new_graph)

    return new_graph

def create_node_group(node): 
    new_ng = {}

    # new_ng["name"] = f"G{index}"
    new_ng["edges"] = node["edges"]
    new_ng["index"] = node["index"] 

    return new_ng

def add_node_to_group(node, group):
    # Add new node to group
    group["index"] += node["index"]
    group["edges"] = list(set(node["edges"]+group["edges"]))

    # Remove edges that point to the group
    for index in group["index"]:
        if index in group["edges"]:
            group["edges"].remove(index)
    
    return group

def merge_groups_with_node(groups_arr: [], node): 
    new_ng = {}
    new_ng["index"] = node["index"]
    new_ng["edges"] = node["edges"]

    for ng in groups_arr:
        new_ng["index"] += ng["index"]
        new_ng["edges"] = list(set(new_ng["edges"] + ng["edges"]))

    # Remove edges that point to the group
    for index in new_ng["index"]:
        new_ng["edges"].remove(index)

    return new_ng


