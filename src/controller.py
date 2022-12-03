import pygame
from src.data import Data
class Controller:
    def __init__(self):

    # Importing background image
        self.background= pygame.image.load("assets/background.png")
        WIDTH, HEIGHT=900,600
        WIN = pygame.display.set_mode((WIDTH,HEIGHT))
        self.background=pygame.transform.rotate(pygame.transform.scale(self.background,(WIDTH,HEIGHT)),0)
    # Calling main function
        self.main()

    # Window updates screen every seconf
    def window(self):
        # Showing background
        WIDTH, HEIGHT=900,600
        WIN=pygame.display.set_mode((WIDTH,HEIGHT))
        WIN.blit(self.background,(0,0))

        # Class for application data is called
        Data()

        # Updating score
        if player_hearts<= 0:
            WIN.blit(winner,(0,0))
            if your_score > score:

                insert = "UPDATE num SET id = "+ str(your_score) 
                db.execute(insert)
                db.commit()
        elif wolf_hearts<= 0:
            if your_score > score:
                insert = "UPDATE num SET id = "+ str(your_score) 
                db.execute(insert)
                db.commit()

            WIN.blit(loser,(0,0))

        # Updating screen every second
        pygame.display.update()

    # Updating your score based on how many hearts you have left
    def score_inc(self):
        global your_score
        if player_hearts>=3:
            your_score +=30

        elif player_hearts>=2:
            your_score +=15
        
        elif player_hearts>=1:
            your_score +=5

    # Main function which controls everything
    def main(self):
        global guess_bool,grass1,grass2,grass3,grass4,grass5,grass6,grass7,grass8,wolf_hearts,player_hearts
        while True:
            # Mouse position
            x,y = pygame.mouse.get_pos()
            # Checking events
            for event in pygame.event.get():
                # Checking if the game is quit
                if event.type==pygame.QUIT:
            
                    pygame.quit()

                # Checking which bush is clicked and reducing heart according to it
                if event.type== pygame.MOUSEBUTTONDOWN:
                    if x >=113 and x<=168 and y>=367 and y<=415:
                        grass1 = False
                        if guess == 1:
                            wolf_hearts -=1
                            self.score_inc()
                        else:
                            player_hearts -=1
                    elif x >=216 and x<=269 and y>=320 and y<=367:
                        grass2 = False
                        if guess == 2:
                            wolf_hearts -=1
                            self.score_inc()
                        else:
                            player_hearts -=1
                        
                    elif x >=315 and x<=369 and y>=420 and y<=467:
                        grass3 = False
                        if guess == 3:
                            self.score_inc()
                            wolf_hearts -=1
                        else:
                            player_hearts -=1
                    elif x >=415 and x<=468 and y>=367 and y<=415:
                        grass4 = False
                        if guess == 4:
                            self.score_inc()
                            wolf_hearts -=1
                        else:
                            player_hearts -=1
                    elif x >=516 and x<=568 and y>=317 and y<=368:
                        grass5 = False
                        if guess == 5:
                            self.score_inc()
                            wolf_hearts -=1
                        else:
                            player_hearts -=1
                    elif x >=616 and x<=668 and y>=417 and y<=469:
                        grass6 = False
                        if guess == 6:
                            self.score_inc()
                            wolf_hearts -=1
                        else:
                            player_hearts -=1
                    elif x >=716 and x<=768 and y>=370 and y<=415:
                        grass7 = False
                        if guess == 7:
                            self.score_inc()
                            wolf_hearts -=1
                        else:
                            player_hearts -=1
                    elif x >=816 and x<=868 and y>=417 and y<=469:
                        grass8 = False
                        if guess == 8:
                            self.score_inc()
                            wolf_hearts -=1
                        else:
                            player_hearts -=1    
            self.window()