import pygame

class Pen():

    def __init__(self):

        self.node_color = (0,0,0)
        self.edge_color = (0,0,0)
        # self.node_color = (255,255,255)
        # self.edge_color = (200,200,200)
        # self.grid_color = (177,177,177)
        self.aim_color = (255,0,255)
        self.node_radius = 4
        self.grid_radius = 2

    def draw_grid(self, screen, step, width, height):

        for i in range(0, width+1, step):
            for j in range(0, height+1, step):
                pygame.draw.circle(
                    screen,
                    self.grid_color,
                    (i, j),
                    self.grid_radius,
                    0)

    def draw_edge(self, screen, start, finish):

        pygame.draw.aaline(
            screen,
            self.edge_color,
            start,
            finish,
            1)

    def draw_node(self, screen, node_x, node_y):
        pygame.draw.circle(
            screen,
            self.node_color,
            (node_x, node_y),
            self.node_radius,
            0)

    def draw_aim(self, screen, x, y, aim_radius):
        pygame.draw.circle(
            screen,
            self.aim_color,
            (x, y),
            aim_radius,
            1)

