from settings import SCREEN_WIDTH
import pygame

pygame.init()

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 700

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Tetris")
clock = pygame.time.Clock()

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((30,30,30))

    pygame.display.flip()

    clock.tick(60)

pygame.quit()