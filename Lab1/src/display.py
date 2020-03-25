
import time
import pygame
from .pen import Pen
from .objects import Node


class Display:

    def __init__(self, width, height, rotation_angle, step):
        pygame.display.set_caption('Kamerka')
        
        # WINDOW
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((width, height))
        self.background = (10,10,50)

        # CAMERA
        self.focal_distance = step * 10
        
        # GRID
        # self.cellsize = cellsize

        # MOVEMENT
        self.step = step
        self.rotation_angle = rotation_angle
        # self.scale_factor = scale_factor

        # FIGURES STORAGE
        self.figures = {}
        self.display_nodes = False
        self.display_edges = True

        # PEN OBJECT
        self.pen = Pen()
        

    def set_camera(self):

        mutual_center = self.find_global_center()
        self.camera = Node(
            self.width // 2,
            self.height // 2,
            mutual_center.z - self.focal_distance)
    

        
    

    def display(self):
        
        
        self.screen.fill(self.background)

        # AIM
        self.pen.draw_aim(self.screen, self.width // 2, self.height // 2)


        # GRID
        # self.pen.draw_grid(self.screen, self.cellsize, self.width, self.height)

        # FIGURES
        for figure in self.figures.values():

            # EDGES
            if self.display_edges:
                for edge in figure.edges:
                    self.pen.draw_edge(self.screen, edge.start, edge.finish)
                    
            # NODES
            if self.display_nodes:
                for node in figure.nodes:
                    self.pen.draw_node(self.screen, node)
                    


    def translate_all(self, axis, step):


        # CAMERA TO THE ONE SIDE
        setattr(self.camera, axis, getattr(self.camera, axis) - step)
        print('Camera at:', self.camera)

        # OBJECTS TO THE OTHER
        for figure in self.figures.values():
            figure.translate_along_axis(axis, step)


    def scale_all(self, step):

        

        # TODO scale step
        # center_x = self.width // 2
        # center_y = self.height // 2
        center_x = self.camera.x
        center_y = self.camera.y

        # FACTOR CALCULATION

        if (self.camera.z + step) == 0:
            print('Limit.')
            return

        tmp = self.camera.z
        self.camera.z += step
        factor = tmp / self.camera.z
        # if factor == 0:
            # factor = 0.5
            # self.camera.z = tmp
        # print(tmp, factor, self.camera.z)
        print(factor)
        print('Camera at:', self.camera)

        for figure in self.figures.values():
            figure.scale(center_x, center_y, factor)
    

    def find_global_center(self):

        local_centers = [figure.find_local_center() for figure in self.figures.values()]
        no = len(local_centers)

        global_x = sum([ center.x for center in local_centers ]) / no
        global_y = sum([ center.y for center in local_centers ]) / no
        global_z = sum([ center.z for center in local_centers ]) / no

        return Node(global_x, global_y, global_z)


    def rotate_all(self, axis, rotation_angle):

        global_center = self.find_global_center()

        method_name = 'rotate_' + axis

        for figure in self.figures.values():
            rotate_method = getattr(figure, method_name)
            rotate_method(rotation_angle, global_center)

        


    def run(self):
        running = True

        bindings = {
            
            pygame.K_LEFT:  lambda x: x.translate_all('x', self.step),
            pygame.K_RIGHT: lambda x: x.translate_all('x',  -self.step),
            pygame.K_DOWN:  lambda x: x.translate_all('y',  -self.step),
            pygame.K_UP:    lambda x: x.translate_all('y', self.step),

            # pygame.K_EQUALS: lambda x: x.scale_all(self.scale_factor),
            # pygame.K_MINUS:  lambda x: x.scale_all(1 / self.scale_factor),

            pygame.K_EQUALS: lambda x: x.scale_all(self.step),
            pygame.K_MINUS:  lambda x: x.scale_all(-self.step),

            pygame.K_1:     lambda x: x.rotate_all(axis='z', rotation_angle=-self.rotation_angle),
            pygame.K_2:     lambda x: x.rotate_all(axis='z', rotation_angle=self.rotation_angle),

            pygame.K_3:     lambda x: x.rotate_all(axis='x', rotation_angle=-self.rotation_angle),
            pygame.K_4:     lambda x: x.rotate_all(axis='x', rotation_angle=self.rotation_angle),

            pygame.K_5:     lambda x: x.rotate_all(axis='y', rotation_angle=-self.rotation_angle),
            pygame.K_6:     lambda x: x.rotate_all(axis='y', rotation_angle=self.rotation_angle)
            
        }
        
        # i = 0
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key in bindings.keys():
                        bindings[event.key](self)
            # i+=1
            # if i==400:
            #     print('Camera at:', self.camera)
            #     i = 0
                    
            self.display()
            pygame.display.flip()


            

            # self.figures['cube'].check()
            # print(self.figures['cube'])
            # time.sleep(1)