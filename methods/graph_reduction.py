from statement import Statement
import utils as ut
from methods.resolution_graph import build_resolution_graph

def resolution_graph_reduction(statement: Statement, red_strength=2, verbose=False): 
    """This mmethod builds a resolution graph for given statement
    and then reduces it based on given reduction strength
    """

    graph = build_resolution_graph(statement,verbose)
    # print(graph) #DEBUG

    reduced_graph = reduce_graph(graph, red_strength, verbose)

    # print(reduced_graph) # DEBUG

    return reduced_graph

def resolution_graph_reduction_NGX(statement: Statement, red_strength=2, verbose=False):
    graph = resolution_graph_reduction(statement, red_strength, verbose)

    ngx_data = {
        'nodes': [],
        'links': []
    }

    links_check = {}

    for index, node in enumerate(graph):
        #Create new NGX node
        node_type = "node"
        if node["name"][0] == 'G':
            node_type="group"
        new_node = {
            'id': str(index+1),
            'label': node["name"],
            'data': {
                "weight": len(node["edges"]),
                "type": node_type
            }
        }

        ngx_data["nodes"].append(new_node)

        for edge in node["edges"]:
            new_link = {
                'id': "",
                'source': str(index+1),
                'target': str(edge+1)                
            }

            if new_link["source"] in links_check:
                target_check = links_check[new_link["source"]]
                if new_link["target"] in target_check:
                    continue
                else:
                    new_link["id"] = len(ngx_data["links"])
                    ngx_data["links"].append(new_link)
                    links_check[new_link["source"]].append(new_link["target"])
            else:
                new_link["id"] = len(ngx_data["links"])
                ngx_data["links"].append(new_link)
                links_check[new_link["source"]] = [new_link["target"]]


    # print(ngx_data) # DEBUG

    return ngx_data

def reduce_graph(graph, red_strength, verbose): 
    """It simplifies the graf by grouping connected nodes based on number of connections to different nodes
    """
    if verbose:
        print("GROUPED RESOLUTION GRAPH")

    standard_nodes = []
    node_groups = []
    
    total_len = len(graph)
    progress = 0
    i = 0

    for node in graph:
        # print(node) #DEBUG
        # Verbose Progres Tracking
        if verbose:
            
            new_progress = (i/total_len)*100
            
            if(new_progress >= progress+1):
                progress = round(new_progress)
                print(f"Progres(Group nodes):{progress}% - [{i}/{total_len}]")
            i+=1

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
            # Update old node group
            c_group = connected_groups[0]
            new_ng = add_node_to_group(node, c_group)
            node_groups.remove(c_group)
            node_groups.append(new_ng)            
        else: 
            # Replace merged node groups with a new one  
            new_ng = merge_groups_with_node(connected_groups, node)
            for c_ng in connected_groups:
                node_groups.remove(c_ng)
            node_groups.append(new_ng)
            

    # print(node_groups) # DEBUG
    # print(standard_nodes) # DEBUG

    # Re-index graph
            
    indexTranslation = {}

    new_graph = []
    for index, node in enumerate(standard_nodes):
        node["name"] = f"C{index}"
        for g_index in node["index"]:
            print(f"INDEX [{g_index}] -> [{index}]")
            indexTranslation[g_index] = index
        new_graph.append(node)

    for index, group in enumerate(node_groups):
        group["name"] = f"G{index}"
        # TODO: For all contained groups create entry
        for g_index in group["index"]:
            indexTranslation[g_index] = len(new_graph)
        new_graph.append(group)

    progress= 0
    total_len = len(new_graph)
    index = 0

    
    # print(standard_nodes) # DEBUG
    # print(node_groups) # DEBUG

    for node in new_graph:
        # Verbose Progres Tracking
        if verbose:
            new_progress = (index/total_len)*100
            if(new_progress >= progress+1):
                progress = round(new_progress)
                print(f"Progres(Reindex):{progress}% - [{index}/{total_len}]")
            index+=1

        node_edges = node["edges"]
        new_edges = []
        # print(node["index"]) # DEBUG
        # for edge in node_edges:
        #     for i, check_node in enumerate(new_graph):
        #         if edge in check_node["index"]: 
        #             # Update new node
        #             new_edges.append(i)

        for edge in node_edges:
            # print(f"{edge} -> {indexTranslation[edge]}") # DEBUG
            new_edges.append(indexTranslation[edge])

        node["edges"] = new_edges

    if verbose:
        print("DROP INDEX")     
    new_graph = ut.graph_drop_index(new_graph)

    if verbose:
        print("END")
    
    # print(new_graph) # DEBUG

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
        if index in new_ng["edges"]: 
            new_ng["edges"].remove(index)

    return new_ng


