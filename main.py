import utils as ut
from statement import Statement

import pipeline as pi

def main():
    path = "./asset/testChain.cnf"
    file = ut.read_dimcas_file(path)
    
    
    red_graph = pi.graph_reduction_pipeline(file, 2)
    res_graph = pi.resolution_graph_pipeline(file)

    print(res_graph)

    ut.argument_to_file_name_specified(res_graph, "RESGRAPH.json")
    ut.argument_to_file_name_specified(red_graph, "REDGRAPH.json")

    return

main()
