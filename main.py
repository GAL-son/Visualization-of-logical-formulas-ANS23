from utils import read_dimcas_file
from statement import Statement


from methods.test.test1 import methodTest1

def main():
    # Test reading from file
    path = "data/test-cnf.cnf"
    path2 = "data/easy/sat/Analiza1-itox_vc1033.cnf"
    file = read_dimcas_file(path)
    test = Statement(file)   

    methodTest1(test)

    return

main()
