def read_dimcas_file(path):
    text = ""

    with open(path, "r") as fp:
        lines = fp.readlines()

    for line in lines:
        if(not line.startswith(("c", "p"))):
            text += line

    return text



