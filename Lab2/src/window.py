
import time
import pygame
from .pen import Pen
from .display import display as inner_display


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
        self.BACKGROUND = (0,0,0)
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.pen = Pen()
        
        # SAFE MODE
        self.safe_mode = safe_mode

        # MOVEMENT
        self.STEP = step
        self.ROT_ANGLE = rotation_angle

        # CAMERA
        self.focal = focal
        self.aim_radius = int(focal / 10)
        self.FOCAL_STEP = focal_step
        self.FOCAL_MAX = focal_max
        self.FOCAL_MIN = focal_min

        # FIGURE COMPONENTS
        self.figures = []
        self.display_nodes = 0
        self.display_edges = 0
        self.display_facets = 1
        
        self.facets_composition = [
            [0, 2, 6, 4],
            [0, 2, 3, 1],
            [1, 3, 7, 5],
            [5, 7, 6, 4],
            [2, 3, 7, 6],
            [0, 1, 5, 4]
        ]
        
        self.facets_colors = [
            (75, 200, 60),  # green
            (70, 60, 200),  # blue
            (250, 10, 20),  # red
            (250, 250, 10), # yellow
            (10, 250, 250), # cyan
            (230, 10, 250)  # pink
        ]


    def zoom(self, step):
        self.focal += step
        if self.focal > self.FOCAL_MAX:
            self.focal = self.FOCAL_MAX
        elif self.focal < self.FOCAL_MIN:
            self.focal = self.FOCAL_MIN
        print(f'Zoom: {self.focal}/{self.FOCAL_MAX}')
        self.aim_radius = int(self.focal / 10)
    

    def display(self):
        inner_display(self)                
                    
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
