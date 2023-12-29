import igraph as ig
import os

from statement import Statement
import utils as ut

def test2(statement):
    total_len = len(statement.clauses)
    nodes = [[] for i in range(0,total_len)]
    #print(nodes)

    #print(len(nodes))

    # BUILD CONNECTIONS
    for i,c1 in enumerate(statement.clauses):
        print("Create Nodes: ", ((i+1)/total_len)*100, "%")
        for j in range(i+1, total_len):
            c2 = statement.clauses[j]

            inter = ut.intersection(c1.variables, c2.variables)
            #print("[",i,",",j,"]",c1.variables, c2.variables, inter)

            if len(inter) != 0:
                edge_i = (j, len(inter))
                if edge_i not in nodes[i]:
                    #print("append to node[",i,"]", edge_i)
                    nodes[i].append(edge_i)
                    #print(nodes)
                edge_j = (i, len(inter))
                if edge_j not in nodes[j]:
                    #print("append to node[",j,"]", edge_j)
                    nodes[j].append(edge_j)
                    #print(nodes)

    #print("Normal nodes: ", nodes, "\n")  

    # REDUCE GRAPH
    #print("\nREDUCTION\n")  

    nodes_reduced = []
    nodes_groups = []
    skipped_counter = 0

    for i, node in enumerate(nodes):
        print("Group Nodes: ", ((i+1)/len(nodes))*100, "%")
        #print("-----\nWORKING NODE: ", i)
        #print("NODE LENGTH: ", len(node))
        if len(node) <= 2:
            skipped_counter+=1
            connected_nodes = [x[0] for x in node]
            #print("CHAIN NODE\nCONNECTED NODES: ", connected_nodes)
            for ng in nodes_groups:
                #print("CHECK NODE GROUP: ", ng)
                ng_nodes = ng[0]
                ng_edges = ng[1]
                indersecting_nodes = ut.intersection(connected_nodes, ng_nodes)
                #print("CONNECTTIONS TO GROUP: ", len(indersecting_nodes))
                if len(indersecting_nodes) != 0:
                    ng_nodes.append(i)
                    #print("GROUP UPDATE NODES: ", ng_nodes)
                    ng_edges += node
                    #print("GROUP UPDATE EDGES: ", ng_edges)
                    for edge in set(ng_edges):
                        #print("EDGE CHECK: ", edge[0])
                        if(edge[0] in ng_nodes):
                            #print("EDGE CHECK POSITIVE")
                            ng_edges.remove(edge)
                    #print("GROUP UPDATED EDGES: ", ng_edges)
                    updated_ng = (ng_nodes, ng_edges)
                    ng = updated_ng
                    break
            else:
                #print("CREATE NEW GROUP")
                new_ng = ([i], node)
                nodes_groups.append(new_ng)  
        else:
            #print("BASIC NODE")
            normal_node = (i, node)
            nodes_reduced.append(normal_node)

    #print("NORMAL NODES: ",nodes_reduced)
    #print("NODE GROUPS: ", nodes_groups)

    #ASSEMBLE NEW GRAPH

    # Assign new indexes to a group nodes
    group_index_start = len(nodes_reduced)
    indexed_ngs = []   

    for i, ng in enumerate(nodes_groups):
        indexed_ngs.append((group_index_start+i, ng[0], ng[1]))
        nodes_reduced.append((group_index_start+i, ng[1]))

    # assign new indexes to a node groups

    #print(indexed_ngs)

    indexed_nodes = []
    for i, node in enumerate(nodes_reduced):
        print("Truncade Nodes: ", ((i+1)/len(nodes_reduced))*100, "%")
        #print("UPDATE NODE: ", i)
        edges = node[1]
        new_edges = []
        #print(i, node)

        for edge in edges:
            # check if edge leads to any node group
            for ng in indexed_ngs:
                if edge[0] in ng[1]:
                    # update edge destination to a group new index
                    #print("UPDATE GROUP EDGE INDEX: ", edge[0], "->", ng[0])
                    new_edges.append(ng[0])
                    break
                    
                else:
                    for j, check_node in enumerate(nodes_reduced):
                        #print("CHECK EDGE: ", check_node, edge[0])
                        # update destination to a new node index
                        if check_node[0] == edge[0]:
                            #print("UPDATE NORMAL EDGE INDEX: ", check_node[0], "->", j)
                            new_edges.append(j)
                            break
        
        indexed_nodes.append(new_edges)

    # Build Graph

    # Prepare verticies and edges data
    verts = []
    verts_data = {"type": []}
    edges = []
    for i, node in enumerate(indexed_nodes):
        print("Build graph data: ", ((i+1)/len(indexed_nodes))*100, "%")
        vert_data = {}
        if i < group_index_start:
            verts_data["type"].append("normal") 
        else:
            verts_data["type"].append("group") 
        
        vert_data["edges"] = len(node)
        verts.append(vert_data)

        for n in node:
            edge = (i, n)
            edge_reverse = (n, i)
            if not(edge in edges or edge_reverse in edges):
                edges.append(edge)

                


    print("Igraph")
    vert_num = len(verts)

    g = ig.Graph(n=len(verts), edges=edges)  
    layout = g.layout("auto") 

    box_size = 500 + (0.5*vert_num)
    vert_size_max = box_size / 100
    g.vs["type"] = verts_data["type"]
    color_dict = {"group": "blue", "normal": "red"}
    g.vs["color"] = [color_dict[gender] for gender in g.vs["type"]]
    #g.vs["size"] = verts["strenght"] + vert_size_max
    
    print("plot")
    #fig, ax = plt.subplots()
    #ig.plot(g, layout="auto")
    ig.plot(g, "./img/test2.png",layout=layout, bbox=(box_size, box_size), margin=vert_size_max + 10)  # Cairo backend


    print("Graph Reduction: ", total_len, "->", len(indexed_nodes), ": ", (len(indexed_nodes)/total_len)*100, "%")





            

