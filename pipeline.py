from statement import Statement
import utils as ut

from methods.graph_reduction import resolution_graph_reduction
from methods.graph_reduction import resolution_graph_reduction_NGX


from methods.resolution_graph import resolution_graph_no_index
from methods.resolution_graph import resolution_graph_NGX

def resolution_graph_pipeline(cnfString, verbose=False): 
    return ut.graph_to_JSON(resolution_graph_NGX(Statement(cnfString), verbose))

def graph_reduction_pipeline(cnfString, red_strength, verbose=False):
    return ut.graph_to_JSON(resolution_graph_reduction_NGX(Statement(cnfString),red_strength, verbose))
