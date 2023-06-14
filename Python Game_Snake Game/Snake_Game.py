#Created By Satrio Bintang (Alt5chm3rz)
#https://github.com/satriobintang
#June 2023

import pygame
import random

# Initialize Pygame
pygame.init()

# Screen width and height
screen_width = 640
screen_height = 480

# Color
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

# Create a game screen
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Snake Game")

# Game speed
clock = pygame.time.Clock()
fps = 10

# Block size and scale
block_size = 20
scale = screen_width // block_size

# Function to run the game
def draw_snake(snake_body):
    for block in snake_body:
        pygame.draw.rect(screen, white, [block[0], block[1], block_size, block_size])

# Fungsi untuk menjalankan permainan
def game_loop():
    game_over = False
    game_close = False

    # The initial coordinates of the snake's head
    x = screen_width // 2
    y = screen_height // 2

    # The initial movement of the snake
    x_change = 0
    y_change = 0

    # Snake Body
    snake_body = []
    snake_length = 1

    # Food
    food_x = round(random.randrange(0, screen_width - block_size) / block_size) * block_size
    food_y = round(random.randrange(0, screen_height - block_size) / block_size) * block_size
    
    # Lives
    lives = 3
    
    # Score
    score = 0

    while not game_over:

        while game_close:
            screen.fill(black)
            font = pygame.font.SysFont(None, 40)
            text = font.render("Game Over! Press SPACE to play again", True, red)
            screen.blit(text, (screen_width // 2 - text.get_width() // 2, screen_height // 2 - text.get_height() // 2))
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                    game_close = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and x_change != block_size:
                    x_change = -block_size
                    y_change = 0
                elif event.key == pygame.K_RIGHT and x_change != -block_size:
                    x_change = block_size
                    y_change = 0
                elif event.key == pygame.K_UP and y_change != block_size:
                    x_change = 0
                    y_change = -block_size
                elif event.key == pygame.K_DOWN and y_change != -block_size:
                    x_change = 0
                    y_change = block_size

        if x >= screen_width or x < 0 or y >= screen_height or y < 0:
            lives -= 1
            if lives == 0:
                game_close = True
            else:
                x = screen_width // 2
                y = screen_height // 2

        x += x_change
        y += y_change
        screen.fill(black)
        pygame.draw.rect(screen, red, [food_x, food_y, block_size, block_size])
        snake_head = []
        snake_head.append(x)
        snake_head.append(y)
        snake_body.append(snake_head)
        if len(snake_body) > snake_length:
            del snake_body[0]

        for block in snake_body[:-1]:
            if block == snake_head:
                lives -= 1
                if lives == 0:
                    game_close = True
                else:
                    x = screen_width // 2
                    y = screen_height // 2
                    snake_body.clear()
                    snake_length = 1

        draw_snake(snake_body)

        pygame.display.update()

        if x == food_x and y == food_y:
            food_x = round(random.randrange(0, screen_width - block_size) / block_size) * block_size
            food_y = round(random.randrange(0, screen_height - block_size) / block_size) * block_size
            snake_length += 1
            score += 1

        # Display lives and score
        font = pygame.font.SysFont(None, 20)
        lives_text = font.render("Lives: " + str(lives), True, white)
        score_text = font.render("Score: " + str(score), True, white)
        screen.blit(lives_text, (10, 10))
        screen.blit(score_text, (screen_width - score_text.get_width() - 10, 10))

        clock.tick(fps)

    pygame.quit()

# Running games
game_loop()
