import pygame
pygame.init()

screen = pygame.display.set_mode((720, 400))
FPS = 60
clock = pygame.time.Clock()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

rect = pygame.Rect((0, 0), (32, 32))
image = pygame.Surface((32, 32))
image.fill(WHITE)

while True:
  pass