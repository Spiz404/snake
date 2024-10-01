import pygame
import copy
pygame.init()
screen = pygame.display.set_mode((600, 600))
clock = pygame.time.Clock()
pygame.display.set_caption("Snake Game")

direction = -1
# 30 x 30 grid for snake
#positions = [[0 for i in range(30)] for j in range(30)]
#positions[15][15] = 1

snake_head = [15, 15]
snake_positions = [[15,15], [15,14], [15, 13], [15, 12], [15, 11]]
while True:
    for x in range(30):
        for y in range(30):
            rect = pygame.Rect(x * 20, y * 20, 20, 20)
            if [x,y] in snake_positions:
                pygame.draw.rect(screen, (255, 255, 255), rect)
            else: pygame.draw.rect(screen, (0, 0, 0), rect)

    # checking events
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                direction = 0
            if event.key == pygame.K_DOWN:
                direction = 1
            if event.key == pygame.K_LEFT:
                direction = 2
            if event.key == pygame.K_RIGHT:
                direction = 3
    pygame.display.flip()

    old_positions = copy.deepcopy(snake_positions)

    if direction != -1:
        for i in range(1, len(snake_positions)):
            snake_positions[i] = old_positions[i-1]

    match direction:

        case 0:
            if snake_positions[0][1] == 0: snake_positions[0][1] = 29
            else: snake_positions[0][1] -= 1
        case 1:
            if snake_positions[0][1] == 29: snake_positions[0][1] = 0
            else: snake_positions[0][1] += 1
        case 2:
            if snake_positions[0][0] == 0: snake_positions[0][0] = 29
            else: snake_positions[0][0] -= 1
        case 3:
            if snake_positions[0][0] == 29: snake_positions[0][0] = 0
            else: snake_positions[0][0] += 1

    if snake_positions[0] in snake_positions[1:]:
        print("game over")
        pygame.quit()
        exit()
    clock.tick(15)
