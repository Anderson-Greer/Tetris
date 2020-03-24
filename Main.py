# Created by Anderson Greer in September of 2019
# This is the game Tetris

import pygame
import random
import sys
import Shapes

def selectBlock():
    b = Shapes.straightBlock(screen, 25, colors["Cyan"])
    return b

# pygame.draw.rect(screen, BLUE, (sx, sy, snake_size, snake_size))

pygame.init()

width = 250
height = 500
rect_size = 25
gameBoard = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

gameover = False

colors = {
    "Cyan" : (0, 255, 255),
    "Yellow" : (255, 255, 0),
    "Purple" : (128, 0, 128),
    "Green" : (0, 255, 0),
    "Red" : (255, 0, 0),
    "Blue" : (0, 0, 255)
}

screen = pygame.display.set_mode((width, height))
screen.fill((0, 0, 0))

clock = pygame.time.Clock()  # Creates the fps clock to slow the snake

while not gameover:

    block = selectBlock()

    while not block.done:
        screen.fill((0, 0, 0))

        block.move()

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                sys.exit()

        clock.tick(2)

        pygame.display.update()
