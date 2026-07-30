from settings import *
import pygame
from board import Board
from piece import Piece

pygame.init()

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 700

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Tetris")
clock = pygame.time.Clock()

board = Board()
piece = Piece()

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type ==pygame.KEYDOWN:
            if event.key== pygame.K_LEFT:
                piece.move_left()
            elif event.key == pygame.K_RIGHT:
                piece.move_right()
            elif event.key == pygame.K_DOWN:
                piece.move_down()

    screen.fill((30,30,30))
    board.draw(screen)
    piece.draw(screen)
    pygame.display.flip()

    clock.tick(60)

pygame.quit()