import config
import random
import pygame

class BallClass:
    def __init__(self):
        self.w = 10
        self.h = 10
        self.off_screen = False
        self.reset_pos()


    def reset_pos(self):
        self.x = random.randint((config.width//4), config.width-(config.width//4))
        self.y = config.height // 2
        self.xspeed = random.choice([-1, 1])
        self.yspeed = random.choice([1])


    def movement(self):
        self.x += self.xspeed
        self.y += self.yspeed

        # Ball And Left Bar Collision
        if self.x < (config.left_bar_x + (config.bars_default_width//2)):
            self.xspeed *= -1
        # Ball And Right Bar Collision
        if (self.x + self.w) > (config.right_bar_x - (config.bars_default_width//2)):
            self.xspeed *= -1
        # Ball And Top Bar Collision
        if self.y < (config.bars_top_y + (config.bars_default_width//2)):
            self.yspeed *= -1

        # Ball Goes Beyond Screen
        if self.y > config.height:
            self.off_screen = True
            self.reset_pos()


    def show(self, surface):
        pygame.draw.rect(surface, (0,120,255), (self.x, self.y, self.w, self.h))
