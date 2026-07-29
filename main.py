from settings import *
import pygame
from board import Board

pygame.init()

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 700

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Tetris")
clock = pygame.time.Clock()

board = Board()

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((30,30,30))
    board.draw(screen)

    pygame.display.flip()

    clock.tick(60)

pygame.quit()