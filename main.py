# Importing libraries
import pygame
import random
import time
import sqlite3 as sq#
#import your controller
from src.game import Game
from src.game import Controller
def main():
    pygame.init()
    #Create an instance on your controller object
    controller = Game()
    #Call your mainloop
    controller.mainloop()
    
    
    ###### NOTHING ELSE SHOULD GO IN main(), JUST THE ABOVE 3 LINES OF CODE ######

# https://codefather.tech/blog/if-name-main-python/
if __name__ == '__main__':
    main()
