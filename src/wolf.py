import pygame
import random

#possible wolf positions
pos1 = (366 , 390)
pos2 = (530, 387)
pos3 = (672, 381)
pos4 = (866, 454)
pos5 = (344, 574)
pos6 = (533, 565)
pos7 = (763, 544)
pos8 = (1037, 587)

class wolf():
  #figure out random position of the wolf
  def position():
    position = random.rand(1,8)
    if position == 1:
      return pos1
    elif position == 2:
      return pos2
    elif position == 3:
      return pos3
    elif position == 4:
      return pos4
    elif position == 5:
      return pos5
    elif position == 6:
      return pos6
    elif position == 7:
      return pos7
    elif position == 8:
      return pos8

  #drawing the wolf onscreen
  def image(position):
    wolf_img = pygame.image.load('wolf.py')
    pygame.screen.blit(wolf_img, position)
    pygame.display.flip()

    

  


        



  