from assets import loser.png

class winner():
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
    