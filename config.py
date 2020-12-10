width = 800
height = 640

bg_color = (0,0,0)

paddle_w = 100
paddle_h = 14
paddle_y = height - 40


bars_color = (200,200,200)
bars_default_width = 31 # Keeping the line width an odd integer, due to the way lines with odd width are drawn in pygame

left_bar_x = (bars_default_width//2)
right_bar_x = width - (bars_default_width//2)

bars_top_y = height // 10
bars_bottom_y = paddle_y + paddle_h - 1


num_of_bricks = 18
brick_w = (width - (bars_default_width*2)) // num_of_bricks
brick_h = 26
