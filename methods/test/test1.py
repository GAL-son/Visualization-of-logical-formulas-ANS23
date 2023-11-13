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

    statement_fast = []
    for c in statement.clauses:
        statement_fast.append(c.variables)
        vert_name.append(c.name)
    
    for i,c1 in enumerate(statement_fast):
        vert_strenght.append(len(c1))
        for j in range(i+1, vert_num):
            c2 = statement_fast[j]
            intersection = [v for v in c1 if v in c2 or abs(v) in c2]
            if intersection:
                connections.append([i,j])
                edge_strenght.append(len(intersection))

    # for i in range(0,vert_num):
    #     clause1 = statement.clauses[i]
    #     vert_strenght.append(len(clause1.variables))
    #     vert_name.append(clause1.name)
    #     for j in range(i+1, vert_num):
    #         clause2 = statement.clauses[j]
    #         for v in clause1.variables:
                
    #             if v in clause2.variables or -v in clause2.variables:
    #                 connections.append([i,j])
    #                 break
   
    print("graph")
    # Plot graph
    g = ig.Graph(n=vert_num, edges=connections)  
    layout = g.layout("auto") 
    g.vs["label"] = vert_name
    g.vs["size"]  = ig.rescale(vert_strenght, (20, 150))
    g.vs["label_size"] = 30

    g.es["width"] = ig.rescale(edge_strenght, (1,10))

    
    print("plot")
    #fig, ax = plt.subplots()
    #ig.plot(g, layout="auto")
    ig.plot(g, "./img/test.png",layout=layout, bbox=(2000, 2000), margin=50)  # Cairo backend

    #fig.show()
    
    
