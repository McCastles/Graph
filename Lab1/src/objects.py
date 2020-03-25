import math

class Wireframe(object):

    def __init__(self, nodes, edges):

        self.nodes = nodes
        self.edges = edges

    def translate_along_axis(self, axis, step):
        for node in self.nodes:
            setattr(node, axis, step + getattr(node, axis))


    def scale(self, centre_x, centre_y, factor):
        """ factor the wireframe from the centre of the screen """

        for node in self.nodes:
            node.x = centre_x + factor * (node.x - centre_x)
            node.y = centre_y + factor * (node.y - centre_y)
            node.z *= factor



    # def check(self):

    #     # print(type(self.nodes[0].x))

    #     a = abs(self.nodes[0].y - self.nodes[2].y)
    #     b = abs(self.nodes[0].x - self.nodes[4].x)
    #     # c = self.nodes[0].y - self.nodes[2].y
    #     # d = self.nodes[0].y - self.nodes[2].y
    #     if a == b:
    #         print('square', a)
    #     else:
    #         print('not a square', a, b)

    
        
    def find_local_center(self):

        nodes_qty = len(self.nodes)

        center_x = sum([node.x for node in self.nodes]) / nodes_qty
        center_y = sum([node.y for node in self.nodes]) / nodes_qty
        center_z = sum([node.z for node in self.nodes]) / nodes_qty

        return Node(center_x, center_y, center_z)
        

    def rotate_x(self, angle, center):

        # center = Node(center)
        for node in self.nodes:
            h = node.y - center.y
            v = node.z - center.z
            d = math.hypot(v, h)
            
            theta = math.atan2(v, h) + angle
            # print(f'theta: {theta} rad -> {math.degrees(theta)} deg')
            node.y = center.y + d * math.cos(theta)
            node.z = center.z + d * math.sin(theta)
            # print('\n')


    def rotate_y(self, angle, center):
        
        # center = Node(center)
        for node in self.nodes:
            h = node.x - center.x
            v = node.z - center.z
            d = math.hypot(v, h)
            theta = math.atan2(v, h) + angle
            # print(f'theta: {theta} rad -> {math.degrees(theta)} deg')
            node.x = center.x + d * math.cos(theta)
            node.z = center.z + d * math.sin(theta)
            # print('\n')


    def rotate_z(self, angle, center):

        # center = Node(center)
        for node in self.nodes:
            h = node.x - center.x
            v = node.y - center.y
            d = math.hypot(v, h)
            theta = math.atan2(v, h) + angle
            # print(f'theta: {theta} rad -> {math.degrees(theta)} deg')
            node.x = center.x + d * math.cos(theta)
            node.y = center.y + d * math.sin(theta)
            # print('\n')



    def __repr__(self):
        a = '\n'.join([f'\t- {node}' for node in self.nodes])
        # s = 'Edges:' + '\n'.join([f'\t- edge from {edge.start} to {edge.finish}' for edge in self.edges])
        s = ''
        return f'<Wireframe object> with nodes at:\n{a}\n' + s


class Node():
    
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        return f'({self.x} {self.y} {self.z})'

class Edge(object):
    

    def __init__(self, start, finish):

        self.start = start
        self.finish = finish

    def __repr__(self):
        return f'<Edge object> from {self.start} to {self.finish}'