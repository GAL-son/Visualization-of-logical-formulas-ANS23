from utils import read_dimcas_file
from statement import Statement

def main():
    # Test reading from file
    path = "data/test-cnf.cnf"
    file = read_dimcas_file(path)

    test = Statement(file)   

    return

main()
