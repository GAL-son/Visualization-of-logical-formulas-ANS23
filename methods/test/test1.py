import igraph as ig
import matplotlib.pyplot as plt

from statement import Statement
from clause import Clause

def methodTest1(statement):
    if type(statement) != Statement:
        raise ValueError("Argument is not Statement type")
    
    # In this graph each vertex represents one clause
    vert_num = len(statement.clauses)

    # Each vertex is connected if there is at least one common variable
    connections=[]
    for i in range(0,vert_num):
        for j in range(i+1, vert_num):
            clause1 = statement.clauses[i]
            clause2 = statement.clauses[j]
            for v in clause1.variables:
                if v in clause2.variables:
                    connections.append([i,j])
                    break
    
                    
    g = ig.Graph(n=vert_num, edges=connections)   
    fig, ax = plt.subplots()
    ig.plot(g, target=ax)

    plt.show()
    
    
