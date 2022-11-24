import pygame
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
      
    
    
    
    