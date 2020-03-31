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


def print_gameboard():
    for row in gameboard:
        print(row)
    print()
    print()


def update_gameboard():
    # Resets the board
    for x in range(0, len(gameboard)):
        for y in range(0, len(gameboard[0])):
            gameboard[x][y] = 0

    # Adds each block to the board
    for element in blocks:
        coords = element.get_coords()
        for xy in coords:
            gameboard[xy[0]][xy[1]] = 1


pygame.init()

# Keeps track of blocks
gameboard = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
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
blocks = []

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
    blocks.append(block)

    # Runs each "turn" for a block i.e. from when it spawns to when it stops
    while not block.done:
        update_gameboard()
        print_gameboard()

        block.move_down()

        for event in pygame.event.get():

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    print("right arrow pressed")
                elif event.key == pygame.K_LEFT:
                    print("left arrow pressed")
                elif event.key == pygame.K_UP:
                    print("up arrow pressed")
                elif event.key == pygame.K_DOWN:
                    print("down arrow pressed")

            elif event.type == pygame.QUIT:
                sys.exit()

        clock.tick(2)

        pygame.display.update()
