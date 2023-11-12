import igraph as ig
import matplotlib.pyplot as plt

from statement import Statement
from clause import Clause

def methodTest1(statement):
    if type(statement) != Statement:
        raise ValueError("Argument is not Statement type")
    
    # In this graph each vertex represents one clause
    vert_num = len(statement.clauses)
    vert_strenght = []
    edge_strenght = []
    vert_name = []


    # Each vertex is connected if there is at least one common variable
    connections=[]
    for i in range(0,vert_num):
        clause1 = statement.clauses[i]
        vert_strenght.append(len(clause1.variables))
        vert_name.append(clause1.name)
        for j in range(i+1, vert_num):
            clause2 = statement.clauses[j]
            for v in clause1.variables:
                
                if v in clause2.variables or -v in clause2.variables:
                    connections.append([i,j])
                    break
   
    # Plot graph
    g = ig.Graph(n=vert_num, edges=connections)   
    g.vs["label"] = vert_name
    g.vs["size"]  = ig.rescale(vert_strenght, (10, 50))

    print(g.edge_betweenness())
    fig, ax = plt.subplots()
    ig.plot(g, target=ax, layout="auto")

    plt.show()
    
    
