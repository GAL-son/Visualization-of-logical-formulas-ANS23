import utils as ut
from statement import Statement

import pipeline as pi

def main():
    path = "./asset/testfilile21_12.cnf"
    path2 = "./asset/test1.cnf"
    file = ut.read_dimcas_file(path)
    
    # Call this functions to calculate graph json
    red_graph = pi.graph_reduction_pipeline(file, 2 ,True)
    res_graph = pi.resolution_graph_pipeline(file, True)

    # print(res_graph)

    # For demo purpose - Save Json to file
    ut.argument_to_file_name_specified(res_graph, "RESGRAPH.json")
    ut.argument_to_file_name_specified(red_graph, "REDGRAPH.json")

    return

main()
