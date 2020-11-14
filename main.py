import pygame
import sys

pygame.init()


def check_winner():
    

FPS = 60
COUNT_BLOCKS = 3
SIZE_BLOCK = 200
MARGIN = 3
BG_COLOR = (12, 12, 204)
COLOR_BLOCK = (73, 73, 222)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
resolution = (COUNT_BLOCKS * SIZE_BLOCK + MARGIN * (COUNT_BLOCKS - 1),
              COUNT_BLOCKS * SIZE_BLOCK + MARGIN * (COUNT_BLOCKS - 1))
field = [[None] * COUNT_BLOCKS for i in range(COUNT_BLOCKS)]
screen = pygame.display.set_mode(resolution)
pygame.display.set_caption("Cross-zero")
pygame.display.set_icon(pygame.image.load("icon.png"))
clock = pygame.time.Clock()
player_value_turn = 'x'

while True:
    screen.fill(BG_COLOR)
    for row in range(COUNT_BLOCKS):
        for column in range(COUNT_BLOCKS):
            x = column * (MARGIN + SIZE_BLOCK)
            y = row * (MARGIN + SIZE_BLOCK)
            width = height = SIZE_BLOCK
            pygame.draw.rect(screen, COLOR_BLOCK, (x, y, width, height))
            if field[row][column] == 'x':
                pygame.draw.line(screen, RED, (x + 0.2 * SIZE_BLOCK, y + 0.2 * SIZE_BLOCK),
                                 (x + 0.8 * SIZE_BLOCK, y + 0.8 * SIZE_BLOCK), 15)
                pygame.draw.line(screen, RED, (x + 0.2 * SIZE_BLOCK, y + 0.8 * SIZE_BLOCK),
                                 (x + 0.8 * SIZE_BLOCK, y + 0.2 * SIZE_BLOCK), 15)
            elif field[row][column] == 'o':
                pygame.draw.circle(screen, BLUE, (x + (SIZE_BLOCK // 2), y + (SIZE_BLOCK // 2)),
                                   0.8 * SIZE_BLOCK / 2, 10)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            click_x, click_y = event.pos
            column = click_x // SIZE_BLOCK
            row = click_y // SIZE_BLOCK
            if field[row][column] is None:
                field[row][column] = player_value_turn
            else:
                print("Field isn't empty!")
            if player_value_turn == 'x':
                player_value_turn = 'o'
            else:
                player_value_turn = 'x'
    clock.tick(FPS)
    pygame.display.update()
