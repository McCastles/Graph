
from .objects import Wireframe

def get_figures(path):

    figures = []
    nodes = []
    edges = []
    
    with open(path) as datafile:

        for row in datafile:
            if not row == '\n':
                row = row.rstrip().split(' ')

                # NODES
                if len(row) == 3:
                    nodes.append( (int(row[0]), int(row[2]), int(row[1])) )

                # EDGES
                else:
                    edges.append( (int(row[0]), int(row[1])) )
            else:
                figures.append( Wireframe(nodes, edges) )
                nodes = []
                edges = []

        if nodes or edges:
            figures.append( Wireframe(nodes, edges) )

    return figures
