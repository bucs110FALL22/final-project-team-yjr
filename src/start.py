from asset import start.jpg
import pygame
import sys

pygame.init()

class start():
  #making the background of the start screen
  def background():
    start_background = pygame.image.load('start.jpg')
    #start_background = pygame.transform.scale(start_background, (1203, 696))
    screen.blit(start_background, (0,0))
    pygame.display.flip()

  #making the button
  class button():
    main_font = pygame.font.SysFont("Comic Sans", 50)
    def __init__(self, image, x_pos, y_pos, text_input):
      self.image = image
      self.x_pos = x_pos
      self.y_pos = y_pos
      self.rect = self.image.get_rect(center = (self.x_pos, self.y_pos))
      self.text_input = text.input
      self.text = main_font.render(self.text_input, True, "white")
      self.text_rect = self.text.get_rect(center = (self.x_pos, self.y_pos))

    #putting the button onscreen
    def update(self):
      screen.blit(self.image, self.rect)
      screen.blit(self.text, self.text_rect)

    #mouse reaction + what happens when it gets clicked
    def input(self, position):
      if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
        #write result below

    #hovering over the button will change its color
    def colorChange(self, position):
      if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
        self.text = main_font.render(self.text_input, True, "green")
      else:
        self.text = main_font.render(self.text_input, True, "white")

  button_surface = pygame.image.load("button.png")
  #change size of the button
  button_surface = pygame.transform.scale(button_surface, (400,150))


  

  
  