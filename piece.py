import pygame

from settings import *
from colors import *

class Piece:
    def __init__(self):
        self.shape=[[1,1,1,1]]
        self.color = CYAN
        
        self.row = 0
        self.col = 3

    def draw (self, screen):

        for r, row in enumerate(self.shape):
            for c, value in enumerate(row):
                if value == 1:
                    x = BOARD_X + (self.col + c) * CELL_SIZE
                    y = BOARD_Y + (self.row + r) * CELL_SIZE

                    rect = pygame.Rect(x, y, CELL_SIZE, CELL_SIZE)
                    pygame.draw.rect(screen, self.color, rect)

                    pygame.draw.rect(screen, BLACK, rect, 1)