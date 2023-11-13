from utils import read_dimcas_file
from statement import Statement


from methods.test.test1 import methodTest1

def main():
    # Test reading from file
    path = "data/test-cnf.cnf"
    path2 = "asset/test1.cnf"
    path3 = "asset/testshort.cnf"
    path4 = "asset/selfTest.cnf"
    path5 = "data/very-hard/sat/Analiza1-gss-25-s100.cnf"
    file = read_dimcas_file(path4)
    test = Statement(file)   

    methodTest1(test)

    return

main()
