import pygraphviz as pgv

A=pgv.AGraph()

A.add_edge(1,2)
A.add_edge(2,3)
A.add_edge(1,3)

A.graph_attr['label']='Name of graph'
A.node_attr['shape']='circle'
A.edge_attr['color']='red'

print(A.string()) # print to screen
print("Wrote simple.dot")
A.write('simple.dot') # write to simple.dot

B=pgv.AGraph('simple.dot') # create a new graph from file
B.layout() # layout with default (neato)
B.draw('simple.png') # draw png
print("Wrote simple.png")