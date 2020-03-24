# Created by Anderson Greer in September of 2019
# This is the game Tetris

import pygame
import random
import sys
import Shapes


# Selects a random block to spawn
def select_block():
    b = Shapes.StraightBlock(colors["Cyan"])
    return b


pygame.init()

# Keeps track of blocks
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

game_over = False

# Dictionary of colors for the blocks
colors = {
    "Cyan": (0, 255, 255),
    "Yellow": (255, 255, 0),
    "Purple": (128, 0, 128),
    "Green": (0, 255, 0),
    "Red": (255, 0, 0),
    "Blue": (0, 0, 255)
}

# Creates the fps clock to give a sense of movement
clock = pygame.time.Clock()

while not game_over:
    block = select_block()

    # Runs each "turn" for a block i.e. from when it spawns to when it stops
    while not block.done:
        block.move()

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                sys.exit()

        clock.tick(2)

        pygame.display.update()
