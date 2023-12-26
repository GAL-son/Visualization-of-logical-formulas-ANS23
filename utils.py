import io

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

    return json

def graph_drop_index(graph):
    for node in graph:
        del node["index"]

    return graph