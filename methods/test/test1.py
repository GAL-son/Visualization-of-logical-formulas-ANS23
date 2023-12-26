import igraph as ig
from statement import Statement
from clause import Clause

import concurrent.futures

def create_connections(statement):
    connections = set()
    vert_num = len(statement)

    def process_clauses(i):
        clause1 = statement[i]
        local_connections = set()
        for j in range(i + 1, vert_num):
            clause2 = statement[j]
            common_vars = set(clause1).intersection(clause2)
            if common_vars:
                local_connections.add((i, j))
        return local_connections

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(process_clauses, i) for i in range(vert_num)]
        for future in concurrent.futures.as_completed(futures):
            connections.update(future.result())

    return list(connections)


def methodTest1(statement):
    if type(statement) != Statement:
        raise ValueError("Argument is not Statement type")
    
    # In this graph each vertex represents one clause
    vert_num = len(statement.clauses)
    vert_strenght = []
    edge_strenght = []
    vert_name = []

    statement_fast = []
    for c in statement.clauses:
        statement_fast.append(c.variables)
        vert_strenght.append(len(c.variables))
        vert_name.append(c.name)

    # Each vertex is connected if there is at least one common variable
    # Tworzenie połączeń w sposób równoległy
    connections = create_connections(statement_fast)
    # connections=[]

    
    
    
    # for i,c1 in enumerate(statement_fast):
    #     vert_strenght.append(len(c1))
    #     for j in range(i+1, vert_num):
    #         c2 = statement_fast[j]
    #         intersection = [v for v in c1 if v in c2 or abs(v) in c2]
    #         if intersection:
    #             connections.append([i,j])
    #             edge_strenght.append(len(intersection))

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
    #g.vs["label"] = vert_name
    g.vs["size"]  = ig.rescale(vert_strenght, (10, 80))
    g.vs["label_size"] = 30

    # g.es["width"] = ig.rescale(edge_strenght, (1,10))

    box_size = 500 + (0.5*vert_num)
    vert_size_max = box_size / 100
    #g.vs["size"] = 10
    
    print("plot")
    #fig, ax = plt.subplots()
    #ig.plot(g, layout="auto")
    ig.plot(g, "./img/test.png",layout=layout, bbox=(box_size, box_size), margin=vert_size_max + 10)  # Cairo backend

    #fig.show()
    
    
