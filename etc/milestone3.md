# Final Project Milestone #3

[Final Project Description](https://docs.google.com/document/d/1j3zgypVjPjzXl4pL1_Wpjvp3GLCW9zcFydkwUjNfNUA/edit?usp=sharing)

Complete this document in **your** portfolio (CH 9). 

You should now begin to code your models. 

Define your models in the `FinalProject/src/` folder in your portfolio.

Although you will probably need to alter them further, you should try to write as much of the models as you can. You can always change things later.

## Models Design

You need to make sure you have the following for each Model:

1. for classes that should be sprites:
    * inherit sprite functionality
    * have instance variables image and rect
2. Models should not have any event logic
    * In other words, you should not be inspecting or responding to events in your models
    * Although some is required, such as the Sprite class, try to minimize how much of the pygame library you use in your models

Remember, this is to get you thinking and help me guide you. Nothing is set in stone.

***

Using the example below, list each model class and its interface

1. #positions for the button
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
  
  
  
  
    

  
  
    
class lives():
  def starting_lives():
    heart_position = [(55,67), (65,67), (75,67)]
    for i in heart_position:
      screen.blit(heart1)
      pygame.display.flip
  def remaining_lives(player_wrong1 = False, player_wrong2 = False, player_wrong3 = False):
    if player_wrong1 == True:
      screen.blit(heart2, (75,67))
    if player_wrong2 == True:
      screen.blit(heart2, (65,67))
    if player_wrong3 == True:
      screen.blit(heart2, (55,67))
      #outcomelose.py here
      
class lives():
  def starting_lives():
    heart_position = [(1145,67), (1135,67), (1125,67)]
    for i in heart_position:
      screen.blit(heart1)
      pygame.display.flip
  def remaining_lives(player_correct1 = False, player_correct2 = False, player_correct3 = False):
    if player_correct1 = True
      screen.blit(heart2, (1125,67))
    if player_correct2 = True
      screen.blit(heart2, (1135,67))
    if player_correct3 = True
      screen.blit(heart2, (1145,67))
      #outcomewin.py here
    