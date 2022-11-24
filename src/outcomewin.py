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
    
    
    