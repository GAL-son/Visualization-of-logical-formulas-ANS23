from utils import read_dimcas_file

def main():
    # Test reading from file
    path = "./data/test-file.txt"
    print(read_dimcas_file(path))

    return

main()