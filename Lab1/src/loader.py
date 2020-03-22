
from .objects import Edge, Node, Wireframe


def get_figures(path, qty, cellsize):

    with open(path) as datafile:

        figures = []

        for i in range(qty):

            nodes_list = []
            for _ in range(8):
                coords = datafile.readline().strip().split(' ')
                # node = Node([c for c in coords])
                node = Node([cellsize * int(c) for c in coords])
                nodes_list.append(node)

            edges_list = []
            for _ in range(12):
                edge = datafile.readline().strip().split(' ')
                
                # print(edge)
                start  =  nodes_list[ int(edge[0]) ]
                finish =  nodes_list[ int(edge[1]) ]

                edge = Edge(start, finish)

                edges_list.append(edge)

            datafile.readline()

            figure = Wireframe(nodes=nodes_list, edges=edges_list)
            figures.append(figure)

    # print('\nLoaded figures:\n')
    # for figure in figures:
    #     print(figure) 

    return figures

