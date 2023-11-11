from utils import read_dimcas_file

def main():
    # Test reading from file
    path = "data/easy/sat/Analiza1-itox_vc1033.cnf"
    print(read_dimcas_file(path))

    return

main()
import statement
def analyseFile(filePath):
    file=open(filePath)
    file.readline()
    statement_string = ""
    for line in file:
        statement_string += line
    return statement.Statement(statement_string)




test=analyseFile("asset/test1.cnf")


for i in test.clauses:
    print(i)

print(test.variables_already_existing)
for i in test.variables:
    print(i)