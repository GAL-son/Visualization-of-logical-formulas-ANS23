from utils import read_dimcas_file
from statement import Statement

def main():
    # Test reading from file
    path = "data/test-cnf.cnf"
    path2= "asset/test1.cnf"
    path3= "asset/selfTest.cnf"
    file = read_dimcas_file(path3)

    test = Statement(file)

    for i in test.clauses:
        print(i)

    print(test.variables_already_existing)
    for i in test.variables:
        print(i)

    test.int()

    return

main()
