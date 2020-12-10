import config
import pygame

class BrickClass:
    def __init__(self, x, y, color, brick_value):
        self.x = x
        self.y = y
        self.w = config.brick_w
        self.h = config.brick_h
        self.color = color
        self.add_points = brick_value
        self.has_collided = False
        self.points_added = False


    def collision(self, ball):
        if (ball.x >= self.x)  and  (ball.x + ball.w) <= (self.x + self.w):
            # Ball Hits Brick From The Bottom
            if ball.y <= (self.y+self.h)  and  ball.y >= (self.y+(self.h//2)):
                ball.yspeed *= -1
                self.has_collided = True

            # Ball Hits Brick From The Top
            if (ball.y + ball.h) >= self.y  and  (ball.y + ball.h) <= (self.y+(self.h//2)):
                ball.yspeed *= -1
                self.has_collided = True
