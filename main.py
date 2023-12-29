import utils
import utils as ut
from statement import Statement


from methods.test.test1 import methodTest1
from methods.test.test2 import test2
from methods.graph_reduction import resolution_graph_reduction
from methods.resolution_graph import resolution_graph_no_index

def main():
    # Test reading from file
    path = "data/test-cnf.cnf"
    path2 = "asset/test1.cnf"
    path3 = "asset/testshort.cnf"
    path4 = "asset/selfTest.cnf"
    path5 = "data/medium/unsat/Analiza4-aaai10-planning-ipc5-pathways-17-step20.cnf"
    path6 = "asset/testChain.cnf"
    path7 = "asset/graph-red-test.cnf"
    file = ut.read_dimcas_file(path7)
    test = Statement(file)   

    # methodTest1(test)
    # test2(test) 
    print(ut.graph_to_JSON(resolution_graph_reduction(test)))
    print(ut.graph_to_JSON(resolution_graph_no_index(test)))

    test.int()

    # utils.argument_to_file("witam_to_Test2")
    # utils.argument_to_file_name_specified("witam_to_Test","testFileName"


    return

main()
