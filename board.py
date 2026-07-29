import pygame
from settings import *

class Board:
    def __init__(self):
        self.grid=[]

        for row in range(ROWS):
            current_row = []

            for col in range(COLS):
                current_row.append("0")

            self.grid.append(current_row)

    def draw(self, screen):
        for row in range(ROWS):
            for col in range (COLS):

                x = BOARD_X + col * CELL_SIZE
                y = BOARD_Y + row * CELL_SIZE

                rect = pygame.Rect(x,y, CELL_SIZE, CELL_SIZE)

                pygame.draw.rect(screen,(70,70,70),rect,1)