import utils as ut
from statement import Statement

import pipeline as pi

def main():
    path = "./asset/formula.cnf"
    file = ut.read_dimcas_file(path)

    print(file)
    
    # Call this functions to calculate graph json
    red_graph = pi.graph_reduction_pipeline(file, 8 ,True)
    res_graph = pi.resolution_graph_pipeline(file, True)

    # For demo purpose - Save Json to file
    ut.argument_to_file_name_specified(res_graph, "WEIGHTED_GRAPH")
    ut.argument_to_file_name_specified(red_graph, "REDUCTION_GRAPH")

    return

main()
