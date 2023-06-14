#Created By Satrio Bintang (Alt5chm3rz)
#https://github.com/satriobintang
#June 2023

import pygame
import sys

# Initialize Pygame
pygame.init()

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Screen size
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 400

# Grid size
GRID_SIZE = 3
GRID_WIDTH = SCREEN_WIDTH // GRID_SIZE
GRID_HEIGHT = SCREEN_HEIGHT // GRID_SIZE

# Initialize the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Tic Tac Toe")

# Board representation
board = [['', '', ''],
         ['', '', ''],
         ['', '', '']]

# Active player ('X' or 'O')
current_player = 'X'

# Game status
game_over = False
winner = None


def draw_grid():
    # Draw vertical lines
    for x in range(1, GRID_SIZE):
        pygame.draw.line(screen, BLACK, (x * GRID_WIDTH, 0), (x * GRID_WIDTH, SCREEN_HEIGHT), 2)

    # Draw horizontal lines
    for y in range(1, GRID_SIZE):
        pygame.draw.line(screen, BLACK, (0, y * GRID_HEIGHT), (SCREEN_WIDTH, y * GRID_HEIGHT), 2)


def draw_markers():
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            marker = board[row][col]
            if marker != '':
                x_pos = col * GRID_WIDTH + GRID_WIDTH // 2
                y_pos = row * GRID_HEIGHT + GRID_HEIGHT // 2
                font = pygame.font.SysFont(None, 80)

                if marker == 'X':
                    text = font.render(marker, True, RED)
                else:
                    text = font.render(marker, True, BLUE)

                text_rect = text.get_rect(center=(x_pos, y_pos))
                screen.blit(text, text_rect)


def check_win():
    global game_over, winner

    # Check rows
    for row in range(GRID_SIZE):
        if board[row][0] == board[row][1] == board[row][2] != '':
            winner = board[row][0]
            game_over = True

    # Check columns
    for col in range(GRID_SIZE):
        if board[0][col] == board[1][col] == board[2][col] != '':
            winner = board[0][col]
            game_over = True

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != '':
        winner = board[0][0]
        game_over = True

    if board[2][0] == board[1][1] == board[0][2] != '':
        winner = board[2][0]
        game_over = True

    # Check for a tie
    if all(board[row][col] != '' for row in range(GRID_SIZE) for col in range(GRID_SIZE)):
        game_over = True


def draw_winner(winner):
    font = pygame.font.SysFont(None, 60)
    if winner == 'X':
        text = font.render("Player X wins!", True, BLACK)
    else:
        text = font.render("Player O wins!", True, BLACK)

    text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
    screen.blit(text, text_rect)


def restart_game():
    global board, current_player, game_over, winner
    board = [['', '', ''],
             ['', '', ''],
             ['', '', '']]
    current_player = 'X'
    game_over = False
    winner = None


# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            mouse_pos = pygame.mouse.get_pos()
            col = mouse_pos[0] // GRID_WIDTH
            row = mouse_pos[1] // GRID_HEIGHT

            if board[row][col] == '':
                board[row][col] = current_player
                check_win()
                if not game_over:
                    current_player = 'O' if current_player == 'X' else 'X'

        elif event.type == pygame.KEYDOWN and game_over:
            if event.key == pygame.K_SPACE:
                restart_game()

    # Drawing
    screen.fill(WHITE)
    draw_grid()
    draw_markers()

    if game_over:
        draw_winner(winner)

    # Update the display
    pygame.display.flip()
