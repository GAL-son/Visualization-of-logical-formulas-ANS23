from statement import Statement
import utils as ut

def build_resolution_graph(statement: Statement) -> []:
    """Method buidls resolution graph for given Statement
    
    Clauses are connected based on shared Variables.
    If two Clauses Share Variable - they will be connected.

    Returns array of dictionaries in form:
    {"name": , "edges": }
    where edges is array of indecies to connected Clauses
    """
    total_len = len(statement.clauses)
    node_arr = [{"index":[i],"name":f"C{i}", "edges":[]} for i in range(0,total_len)]


    for i, clause_1 in enumerate(statement.clauses):
        for j in range(i+1, total_len):
            clause_2 = statement.clauses[j]

            # calculate common variables
            inter = ut.intersection(clause_1.variables, clause_2.variables)

            if len(inter) == 0:
                continue

            node_arr[i]["edges"].append(j)
            node_arr[j]["edges"].append(i)   
    
    return node_arr

def resolution_graph_no_index(statement: Statement):
    return ut.graph_drop_index(build_resolution_graph(statement))