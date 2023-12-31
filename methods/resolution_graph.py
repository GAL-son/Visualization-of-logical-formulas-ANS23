from statement import Statement
import utils as ut

def build_resolution_graph(statement: Statement, verbose=False) -> []:
    """Method buidls resolution graph for given Statement
    
    Clauses are connected based on shared Variables.
    If two Clauses Share Variable - they will be connected.

    Returns array of dictionaries in form:
    {"name": , "edges": }
    where edges is array of indecies to connected Clauses
    """
    total_len = len(statement.clauses)
    node_arr = [{"index":[i],"name":f"C{i}", "edges":[]} for i in range(0,total_len)]

    progress = 0    

    if verbose:
        print("RESOLUTION GRAPH")

    for i, clause_1 in enumerate(statement.clauses):
        # Verbose Progres Tracking
        if verbose:
            new_progress = (i/total_len)*100
            if(new_progress >= progress+1):
                progress = round(new_progress)
                print(f"Progres (Resolution Graph):{progress}% - [{i}/{total_len}]")

        for j in range(i+1, total_len):
            clause_2 = statement.clauses[j]

            # calculate common variables
            inter = ut.intersection(clause_1.variables, clause_2.variables)

            if len(inter) == 0:
                continue

            node_arr[i]["edges"].append(j)
            node_arr[j]["edges"].append(i)   
    
    return node_arr

def resolution_graph_no_index(statement: Statement, verbose=False):
    return ut.graph_drop_index(build_resolution_graph(statement, verbose))

def resolution_graph_NGX(statement: Statement, verbose=False):
    graph = ut.graph_drop_index(build_resolution_graph(statement, verbose))

    ngx_data = {
        'nodes': [],
        'links': []
    }

    links_check = {}

    for index, node in enumerate(graph):
        #Create new NGX node
        new_node = {
            'id': str(index),
            'label': node["name"],
            'data': {"weight": len(node["edges"])}
        }

        ngx_data["nodes"].append(new_node)

        for edge in node["edges"]:
            new_link = {
                'id': "",
                'source': str(index),
                'target': str(edge)                
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

