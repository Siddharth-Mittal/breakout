import config
import pygame

class PaddleClass:
    def __init__(self):
        self.x = (config.width//2) - (config.paddle_w//2)
        self.y = config.paddle_y
        self.w = config.paddle_w
        self.h = config.paddle_h


    def restrict_movement(self):
        if self.x <= (0 + config.bars_default_width):
            self.x = config.bars_default_width

        if self.x >= (config.width - self.w - config.bars_default_width + 1):
            self.x = config.width - self.w - config.bars_default_width + 1



    def collision(self, ball):
        # Ball hits the top of the paddle
        if (ball.x + ball.w >= self.x) and (ball.x <= self.x + self.w):
            if (ball.y + ball.h >= self.y) and (ball.y + ball.h <= self.y + (self.h//2)):
                ball.y = self.y - ball.h
                ball.yspeed *= -1


        # Ball hits the side of the paddle
        if (ball.y + ball.h > self.y) and (ball.y < self.y + self.h):
            # Ball hits the Left Side of the Paddle
            if (ball.x + ball.w >= self.x) and (ball.x < self.x + (self.w//2)):
                # Ball moving towards the Left Side
                if ball.xspeed > 0:
                    ball.xspeed *= -1
                # Ball moving away from Left Side
                elif ball.xspeed < 0:
                    ball.xspeed += -1

            # Ball hits the Right Side of the Paddle
            if (ball.x <= self.x + self.w) and (ball.x + ball.w > self.x + (self.w//2)):
                # Ball moving towards the Right Side
                if ball.xspeed < 0:
                    ball.xspeed *= -1
                # Ball moving away from Right Side
                elif ball.xspeed > 0:
                    ball.xspeed += 1



    def show(self, surface):
        pygame.draw.rect(surface, (0,120,255), (self.x, self.y, self.w, self.h))
