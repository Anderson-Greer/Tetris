# Created by Anderson Greer in September of 2019
# These are the shapes for Tetris

import pygame


class Block:

    def __init__(self, color):
        self.width = 250
        self.height = 500
        self.screen = pygame.display.set_mode((self.width, self.height))  # Creates the GUI for the game
        self.color = color  # Color of each block
        self.RECT_SIZE = 25  # Constant for the size of each "pixel"
        self.coordinates = []  # A list of tuples corresponding to points on the game board
        self.num_of_blocks = 0

        self.screen.fill((0, 0, 0))  # Makes the screen black

    def move_down(self):
        self.screen.fill((0, 0, 0))  # Makes the screen black

        for i in range(0, self.num_of_blocks):
            pygame.draw.rect(self.screen, self.color, (self.coordinates[i][1] * 25, self.coordinates[i][0] * 25,
                                                       self.RECT_SIZE, self.RECT_SIZE))

        for coord in self.coordinates:
            coord[1] += 1


class StraightBlock(Block):

    y_value = 0
    starting_x = 0
    done = False

    def move(self):
        self.screen.fill((0, 0, 0))
        for i in range(0, 4):
            pygame.draw.rect(self.screen, self.color, ((75 + 25 * i), self.y_value, self.RECT_SIZE, self.RECT_SIZE))

        self.y_value += 25
        print(self.y_value)


class LeftL:
    pass


class RightL:
    pass


class Square:
    pass


class LeftZ:
    pass


class RightZ:
    pass