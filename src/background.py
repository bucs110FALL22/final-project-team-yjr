import pygame

pygame.init()

screen = pygame.display.set_mode((1203, 696))
gameon = True 
pygame.display.set_caption("Nice Field")
background = pygame.image.load('background.png')
from sys import exit
while gameon:
  for event in pygame.event.get():
    if event.type == pygame.quit:
      gameon=False

  screen.blit(background,(0,0))
  pygame.display.update()
pygame.quit()
exit()
                