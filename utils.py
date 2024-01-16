import io
import os

def read_dimcas_file(path):
    text = ""

    with open(path, "r") as fp:
        lines = fp.readlines()

    for line in lines:
        if(not line.startswith(("c", "p"))):
            text += line

    return text

def intersection(lst1, lst2):
    """Returns list that is intersection of two given lists"""
    return [abs(value) for value in lst1 if value in lst2 or -value in lst2]

def move_cursor(y,x): 
    print("\033[%d;%dH" % (y, x))

def graph_to_JSON(graph):

    output = io.StringIO()
    print(graph, file=output)
    json = output.getvalue()
    output.close()
    json = json.replace("'", "\"")

    return json

def graph_drop_index(graph):
    for node in graph:
        del node["index"]

    return graph

# tested,works creates file with no extention in data dictiuonary, argument_file file,if file exists it will overwtire,
def argument_to_file(argument):
    f = open("data/argument_file", "w")
    f.write(argument)
    f.close()
#same, can specify file name
def argument_to_file_name_specified(argument,filename):

    dir_path = r'output/'
    count = 0
    # Iterate directory
    for path in os.listdir(dir_path):
        # check if current path is a file
        if os.path.isfile(os.path.join(dir_path, path)):
            count += 1

    f = open(dir_path+filename + str((count-1)//2) + '.json', "w")
    f.write(argument)
    f.close()
