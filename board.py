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

                if self.grid[row][col] == 1:
                    filled_rect = pygame.Rect(
                        x,
                        y,
                        CELL_SIZE,
                        CELL_SIZE
                    )

                    pygame.draw.rect(
                        screen,
                        (100, 180, 255),
                        filled_rect
                    )
    
    def lock_piece(self,piece):

        for r, row in enumerate(piece.shape):
            for c, value in enumerate(row):

                if value == 1:
                    board_row = piece.row + r
                    board_col = piece.col + c

                    self.grid[board_row][board_col] = 1