import pygame 
from assets.bush import bush

bush_img = pygame.image.load('bush.png').convert_alpha()

#positions for the button
class bush_button():
  pos1 = (366, 390)
  pos2 = (530, 387)
  pos3 = (672, 381)
  pos4 = (866, 454)
  pos5 = (344, 574)
  pos6 = (533, 565)
  pos7 = (763, 544)
  pos8 = (1037, 587)

  #create the button
  def __init__(self, x, y):
    self.image = bush_img
    self.polygon = self.image.get_polygon()
    self.polygon.topleft = (x,y)
    self.clicked = False

  #reaction after mouse clicks it
  def mouse(self, surface):
    #get mouse position and see if it clicks onscreen
    pos = pygame.mouse.get_pos()
    if self.rect.collidepoint(pos):
      if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
        self.clicked = True
      if pygame.mouse.get_pressed()[0] == 0:
        self.clicked = False

    
    pygame.display.flip
    pygame.time.wait(100)
    

        
  #draw bushes
  def bushes(self):
    positions = [pos1, pos2, pos3, pos4, pos5, pos6, pos7, pos8]
    for i in positions: 
      screen.blit(bush_img, (self.polygon.x, self.polygon.y))
  button_1 = bush_button()

mouse(self, surface)
  screen.blit(pos1,(500,500))
  running = True
  while running:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        running = False

    screen.blit(pos1,(500,500))
  pygame.display.flip
pygame.quit()
  
  
  
  
    

  
  
    

    
    
    