
from .objects import Edge, Node, Wireframe

def get_figures(path):

    figures = []
    nodes = []
    edges = []

    with open(path) as datafile:

        for row in datafile:
            # print(row, end='')
            # print(len(row))
            if not row == '\n':
                row = row[:-1].split(' ')

                # NODES
                if len(row) == 3:
                    # node = Node([int(c) for c in row])
                    node = Node(int(row[0]), int(row[1]), int(row[2]))
                    nodes.append(node)

                # EDGES
                else:
                    start  =  nodes[ int(row[0]) ]
                    finish =  nodes[ int(row[1]) ]

                    edge = Edge(start, finish)

                    edges.append(edge)
            else:

                # print('empty')
                figures.append( Wireframe(nodes, edges) )
                nodes = []
                edges = []

        if nodes or edges:
            figures.append( Wireframe(nodes, edges) )

    return figures

# def get_figures1(path, qty, cellsize):

#     with open(path) as datafile:

#         figures = []

#         for i in range(qty):

#             nodes_list = []
#             for _ in range(8):
#                 coords = datafile.readline().strip().split(' ')
#                 # node = Node([c for c in coords])
#                 node = Node([int(c) for c in coords])
#                 nodes_list.append(node)

#             edges_list = []
#             for _ in range(12):
#                 edge = datafile.readline().strip().split(' ')
                
#                 # print(edge)
#                 start  =  nodes_list[ int(edge[0]) ]
#                 finish =  nodes_list[ int(edge[1]) ]

#                 edge = Edge(start, finish)

#                 edges_list.append(edge)

#             datafile.readline()

#             figure = Wireframe(nodes=nodes_list, edges=edges_list)
#             figures.append(figure)

#     # print('\nLoaded figures:\n')
#     # for figure in figures:
#     #     print(figure) 

#     return figures

