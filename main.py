from utils import read_dimcas_file

def main():
    # Test reading from file
    path = "data/easy/sat/Analiza1-itox_vc1033.cnf"
    print(read_dimcas_file(path))

    return

main()