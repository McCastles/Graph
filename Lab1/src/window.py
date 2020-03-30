
import time
import pygame
from .pen import Pen


class Window:

    def __init__(
        self, width, height,
        rotation_angle, step,
        focal, focal_step,
        focal_min, focal_max,
        safe_mode):

        pygame.display.set_caption('Virtual Camera')
        self.bindings = {
        
            pygame.K_SPACE:   lambda a: a.translate_all( 0, 0, -self.STEP ),
            pygame.K_LSHIFT:  lambda a: a.translate_all( 0, 0, self.STEP  ),
            pygame.K_UP:      lambda a: a.translate_all( 0, -self.STEP, 0 ),
            pygame.K_DOWN:    lambda a: a.translate_all( 0, self.STEP,  0 ),
            pygame.K_RIGHT:   lambda a: a.translate_all( -self.STEP, 0, 0 ),
            pygame.K_LEFT:    lambda a: a.translate_all( self.STEP,  0, 0 ),

            pygame.K_EQUALS:  lambda a: a.zoom(self.FOCAL_STEP),
            pygame.K_MINUS:   lambda a: a.zoom(-self.FOCAL_STEP),

            pygame.K_1:       lambda a: a.rotate_all( 'z', self.ROT_ANGLE ),
            pygame.K_2:       lambda a: a.rotate_all( 'z', -self.ROT_ANGLE ),

            pygame.K_3:       lambda a: a.rotate_all( 'x', -self.ROT_ANGLE ),
            pygame.K_4:       lambda a: a.rotate_all( 'x', self.ROT_ANGLE ),

            pygame.K_5:       lambda a: a.rotate_all( 'y', -self.ROT_ANGLE ),
            pygame.K_6:       lambda a: a.rotate_all( 'y', self.ROT_ANGLE )
            
        }

        # WINDOW
        self.WIDTH = width
        self.HEIGHT = height
        self.BACKGROUND = (10,10,50)
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))

        # MOVEMENT
        self.STEP = step
        self.ROT_ANGLE = rotation_angle

        # CAMERA
        self.focal = focal
        self.aim_radius = int(focal / 10)
        self.FOCAL_STEP = focal_step
        self.FOCAL_MAX = focal_max
        self.FOCAL_MIN = focal_min

        # FIGURES STORAGE
        self.figures = []
        self.display_nodes = False
        self.display_edges = True
        self.safe_mode = safe_mode

        # PEN OBJECT
        self.pen = Pen()
    

    def zoom(self, step):
        self.focal += step
        if self.focal > self.FOCAL_MAX:
            self.focal = self.FOCAL_MAX
        elif self.focal < self.FOCAL_MIN:
            self.focal = self.FOCAL_MIN
        print(f'Zoom: {self.focal}/{self.FOCAL_MAX}')
        self.aim_radius = int(self.focal / 10)
    


    def display(self):
        
        is_visible = lambda node: \
            node[1] > self.focal if self.safe_mode else True
            

        self.screen.fill(self.BACKGROUND)
        self.pen.draw_aim(
            self.screen,
            self.WIDTH // 2, self.HEIGHT // 2,
            self.aim_radius)

        # FIGURES
        for figure in self.figures:
            
            # NODES
            if self.display_nodes:
                for node in figure.nodes:
                    if is_visible(node):
                        x, y = figure.cast_3d_to_2d(
                            node, self.WIDTH, self.HEIGHT, self.focal)
                        self.pen.draw_node(self.screen, int(x), int(y))

            # EDGES
            if self.display_edges:
                for (index_start, index_finish) in figure.edges:

                    node_start = figure.nodes[index_start]
                    node_finish = figure.nodes[index_finish]

                    if is_visible(node_start) and is_visible(node_finish):

                        pair_start = figure.cast_3d_to_2d(
                            node_start,
                            self.WIDTH, self.HEIGHT, self.focal)

                        pair_finish = figure.cast_3d_to_2d(
                            node_finish,
                            self.WIDTH, self.HEIGHT, self.focal)
                            
                        self.pen.draw_edge(
                            self.screen,
                            pair_start,
                            pair_finish)
                    
                    
    def rotate_all(self, axis, rotation_angle):

        method_name = axis + '_rotation_matrix'

        for figure in self.figures:
            rotation_matrix_method = getattr(figure, method_name)
            matrix = rotation_matrix_method(rotation_angle)
            figure.transform( matrix )

    def translate_all(self, dx, dy, dz):

        for figure in self.figures:
            matrix = figure.translation_matrix(dx, dy, dz)
            figure.transform( matrix )

        
    def run(self):
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key in self.bindings.keys():
                        self.bindings[event.key](self)
                    
            self.display()
            pygame.display.flip()
