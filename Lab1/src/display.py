
import time
import pygame
from .pen import Pen


class Display:

    def __init__(self, width, height, cellsize, rotation_angle, scale_factor):
        pygame.display.set_caption('Kamerka')
        
        # WINDOW
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((width, height))
        self.background = (10,10,50)
        
        # GRID
        self.cellsize = cellsize

        # MOVEMENT
        self.translation_speed = cellsize // 2
        self.rotation_angle = rotation_angle
        self.scale_factor = scale_factor

        # FIGURES STORAGE
        self.figures = {}
        self.display_nodes = True
        self.display_edges = True

        # PEN OBJECT
        self.pen = Pen()
        
    

    def display(self):
        
        self.screen.fill(self.background)

        # GRID
        self.pen.draw_grid(self.screen, self.cellsize, self.width, self.height)

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
        for figure in self.figures.values():
            figure.translate_along_axis(axis, step)

    def scale_all(self, factor):

        center_x = self.width // 2
        center_y = self.height // 2

        for figure in self.figures.values():
            figure.scale(center_x, center_y, factor)
    
    def rotate_all(self, axis, rotation_angle):

        method_name = 'rotate_' + axis

        for figure in self.figures.values():
            rotate_method = getattr(figure, method_name)
            rotate_method(rotation_angle)

        


    def run(self):
        running = True

        bindings = {
            
            pygame.K_LEFT:  lambda x: x.translate_all('x', self.translation_speed),
            pygame.K_RIGHT: lambda x: x.translate_all('x',  -self.translation_speed),
            pygame.K_DOWN:  lambda x: x.translate_all('y',  -self.translation_speed),
            pygame.K_UP:    lambda x: x.translate_all('y', self.translation_speed),

            pygame.K_EQUALS: lambda x: x.scale_all(self.scale_factor),
            pygame.K_MINUS:  lambda x: x.scale_all(1 / self.scale_factor),

            pygame.K_1:     lambda x: x.rotate_all(axis='z', rotation_angle=-self.rotation_angle),
            pygame.K_2:     lambda x: x.rotate_all(axis='z', rotation_angle=self.rotation_angle),

            pygame.K_3:     lambda x: x.rotate_all(axis='x', rotation_angle=-self.rotation_angle),
            pygame.K_w:     lambda x: x.rotate_all(axis='x', rotation_angle=self.rotation_angle),

            pygame.K_5:     lambda x: x.rotate_all(axis='y', rotation_angle=-self.rotation_angle),
            pygame.K_6:     lambda x: x.rotate_all(axis='y', rotation_angle=self.rotation_angle)
            
        }
        
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key in bindings.keys():
                        bindings[event.key](self)
                    
            self.display()
            pygame.display.flip()


            

            # self.figures['cube'].check()
            # print(self.figures['cube'])
            # time.sleep(1)