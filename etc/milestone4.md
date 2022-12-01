class Controller:

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

pygame.init()

heart1 = pygame.image.load('heart1.png')
heart2 = pygame.image.load('heart2.png')

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

heart1 = pygame.image.load('heart1.png')
heart2 = pygame.image.load('heart2.png')

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
    

from assets import loser.png

class loser():
  def image():
    image = pygame.image.load('loser.py')
    image = pygame.transform.scale(image, (1203, 696))
    screen.blit(image,(0,0))
    pygame.display.flip()

  def message():
    pygame.font.init()
    my_font = pygame.font.SysFont('Comic Sans MS', 200)
    msg = my_font.render('The Werewolf is the King of the Forest!')
    
    #need to change
    screen.blit(msg, (600,325))
    
    pygame.display.flip()

from assets import winner.jpg

class winner():
  def image():
    image = pygame.image.load('winner.py')
    image = pygame.transform.scale(image, (1203, 696))
    screen.blit(image,(0,0))

  def message():
    pygame.font.init()
    my_font = pygame.font.SysFont('Comic Sans MS', 200)
    msg = my_font.render('You Scared off the Werewolf!')
    
    #need to change
    screen.blit(msg, (600,325))
    
    pygame.display.flip
    

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

Our controller class is not complete and up to par because our Visual Studio Code was not working properly. Our github for some reason only sent our milestone 3 push today when we opened it and resent it. We have reached all the checkpoints but our code is not yet functioning and we are currently debugging.