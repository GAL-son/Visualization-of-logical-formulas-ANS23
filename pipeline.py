from statement import Statement
import utils as ut
from methods.graph_reduction import resolution_graph_reduction
from methods.resolution_graph import resolution_graph_no_index

def resolution_graph_pipeline(cnfString): 
    return ut.graph_to_JSON(resolution_graph_no_index(Statement(cnfString)))

def graph_reduction_pipeline(cnfString, red_strength):
    return ut.graph_to_JSON(resolution_graph_reduction(Statement(cnfString), red_strength))
