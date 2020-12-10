from ball import BallClass
from brick import BrickClass
from paddle import PaddleClass
import config
import pygame
pygame.init()

screen = pygame.display.set_mode((config.width,config.height))

clock = pygame.time.Clock()

text_font = pygame.font.Font("freesansbold.ttf", 32)

# score and properties
score_value = 0
score_text_x = (config.width//4)

def show_score():
    score_text = text_font.render(f"{score_value:03}", True, config.bars_color)
    screen.blit(score_text, (score_text_x, 10))

# player lives and properties
player_lives = 3
lives_text_x = config.width - (config.width//4)

def show_lives():
    lives_text = text_font.render(f"{player_lives:1}", True, config.bars_color)
    screen.blit(lives_text, (lives_text_x, 10))


# bars' properties
col = config.bars_color
lx = config.left_bar_x
rx = config.right_bar_x
uy = config.bars_top_y
dy = config.bars_bottom_y
bw = config.bars_default_width


paddle = PaddleClass()

def key_pressed():
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            paddle.x -= 3
        if event.key == pygame.K_RIGHT:
            paddle.x += 3


ball = BallClass()


# bricks
red, orange, yellow, green, blue = [], [], [], [], []


def make_brick_row(y, color, list_name, brick_value):
    for i in range(config.num_of_bricks):
        brick = BrickClass(i, y, color, brick_value)
        brick.x = (i*brick.w) + bw
        list_name.append(brick)


bricks_y = uy + 100
make_brick_row(bricks_y, (255,0,0), red, 9)

bricks_y += config.brick_h
make_brick_row(bricks_y, (255,100,0), orange, 7)

bricks_y += config.brick_h
make_brick_row(bricks_y, (255,255,0), yellow, 5)

bricks_y += config.brick_h
make_brick_row(bricks_y, (0,255,0), green, 3)

bricks_y += config.brick_h
make_brick_row(bricks_y, (0,0,255), blue, 1)


def draw_bricks(bricks_list):
    global score_value
    for i in bricks_list:
        if i.has_collided == False:
            pygame.draw.rect(screen, i.color, (i.x, i.y, i.w, i.h))
            i.collision(ball)
        elif i.has_collided == True:
            if i.points_added == False:
                score_value += i.add_points
                i.points_added = True



# Game loop
running = True
while running:
    # framerate
    clock.tick(240)

    screen.fill(config.bg_color)

    # left bar
    pygame.draw.line(screen, col, (lx,uy), (lx,dy), bw)
    # right bar
    pygame.draw.line(screen, col, (rx,uy), (rx,dy), bw)
    # upper bar
    pygame.draw.line(screen, col, (0,uy), (config.width,uy), bw)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    # Drawing Bricks
    draw_bricks(red)
    draw_bricks(orange)
    draw_bricks(yellow)
    draw_bricks(green)
    draw_bricks(blue)

    key_pressed()

    paddle.restrict_movement()
    paddle.collision(ball)
    paddle.show(screen)


    if player_lives > 0:
        ball.movement()
        ball.show(screen)

        if ball.off_screen == True:
            player_lives -= 1
            ball.off_screen = False


    show_score()
    show_lives()

    pygame.display.update()
