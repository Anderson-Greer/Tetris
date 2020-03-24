# Created by Anderson Greer in September of 2019
# These are the shapes for Tetris

import pygame

# pygame.draw.rect(screen, BLUE, (sx, sy, snake_size, snake_size))
class block:
    rectSize = 25

class straightBlock:

    yvalue = 0
    startingx = 0
    done = False

    def __init__(self, screen, rectSize, color):
        self.screen = screen
        self.rect_size = rectSize
        self.color = color

    def drawShape(self):
        self.startingx = 200
        for i in range(0, 4):
            pygame.draw.rect(self.screen, self.color, (self.startingx + (25 * i), 0, self.rect_size, self.rect_size))

    def move(self):

        for i in range(0, 4):
            pygame.draw.rect(self.screen, self.color, ((75 + 25 * i), self.yvalue, self.rect_size, self.rect_size))

        self.yvalue += 25
        print(self.yvalue)


class leftL:
    pass

class rightL:
    pass

class square:
    pass

class leftZ:
    pass

class rightZ:
    pass