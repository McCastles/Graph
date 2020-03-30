import math
import numpy as np

class Wireframe(object):

    def __init__(self, nodes, edges):

        nodes = np.array(nodes)
        ones = np.ones((len(nodes), 1), dtype=int)
        self.nodes = np.hstack((nodes, ones))
        self.edges = edges

    def transform(self, matrix):
        self.nodes = np.dot(self.nodes, matrix)
        # print(self)

    def translation_matrix(self, dx, dy, dz):
        return np.array([
            [1, 0, 0, 0],
            [0, 1, 0, 0],
            [0, 0, 1, 0],
            [dx, dy, dz, 1],
        ])

    def x_rotation_matrix(self, angle):

        s = np.sin(angle)
        c = np.cos(angle)

        return np.array([
            [1, 0, 0, 0],
            [0, c, -s, 0],
            [0, s, c, 0],
            [0, 0, 0, 1]
        ])

    def y_rotation_matrix(self, angle):

        c = np.cos(angle)
        s = np.sin(angle)

        return np.array([
            [ c, 0, s, 0],
            [ 0, 1, 0, 0],
            [-s, 0, c, 0],
            [ 0, 0, 0, 1]
        ])

    def z_rotation_matrix(self, angle):

        s = np.sin(angle)
        c = np.cos(angle)

        return np.array([
            [c, -s, 0, 0],
            [s, c, 0, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 1]
        ])


    def cast_3d_to_2d(self, point_3d, view_width, view_heigh, focal):
        
        from_focal = focal / point_3d[1]
        x = from_focal * point_3d[0] + view_width / 2
        y = view_heigh / 2 - from_focal * point_3d[2]

        return x, y

    def __repr__(self):
        return f'<Wireframe object> with nodes at:\n{self.nodes}\n'
