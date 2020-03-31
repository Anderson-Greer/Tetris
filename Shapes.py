# Created by Anderson Greer in September of 2019
# These are the shapes for Tetris

import pygame


class Block:

    def __init__(self, color):
        self.width = 250
        self.height = 500
        self.screen = pygame.display.set_mode((self.width, self.height))  # Creates the GUI for the game
        self.done = False  # Tracks if the block is finished or not
        self.color = color  # Color of each block
        self.RECT_SIZE = 25  # Constant for the size of each "pixel"
        self.coordinates = [[]]  # A list of ordered pairs corresponding to points on the game board

        self.screen.fill((0, 0, 0))  # Makes the screen black

    def is_done(self):
        for coord in self.coordinates:
            if coord[0] == 19:
                self.done = True
            else:
                self.done = False

    def move_down(self):
        self.screen.fill((0, 0, 0))  # Makes the screen black

        for i in range(0, len(self.coordinates)):
            pygame.draw.rect(self.screen, self.color, (self.coordinates[i][1] * 25, self.coordinates[i][0] * 25,
                                                       self.RECT_SIZE, self.RECT_SIZE))

        self.is_done()
        for coord in self.coordinates:
            if not self.done:
                coord[0] += 1

    def get_coords(self):
        return self.coordinates


class StraightBlock(Block):
    y_value = 0
    starting_x = 0

    def __init__(self, color):
        super(StraightBlock, self).__init__(color)
        self.coordinates = [[0, 3], [0, 4], [0, 5], [0, 6]]


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
