import pygame
import random
import copy
pygame.init()
screen = pygame.display.set_mode((600, 600))
clock = pygame.time.Clock()
pygame.display.set_caption("Snake Game")

direction = -1

snake_head = [15, 15]
snake_positions = [[15,15]]
apples_positions = []
to_append= False
APPLES = 4
for i in range(APPLES):

    apple = [0, 0]
    while apple in snake_positions or apple in apples_positions:
        apple = [random.randint(0, 29), random.randint(0, 29)]

    apples_positions.append(apple)
while True:
    for x in range(30):
        for y in range(30):
            rect = pygame.Rect(x * 20, y * 20, 20, 20)
            if [x,y] in snake_positions:
                pygame.draw.rect(screen, (255, 255, 255), rect)
            elif [x, y] in apples_positions:
                pygame.draw.rect(screen, (255, 0, 0), rect)
            else: pygame.draw.rect(screen, (0, 0, 0), rect)

    # checking events
    for event in pygame.event.get():

        if event.type == pygame.QUIT or pygame.key.get_pressed()[pygame.K_q]:
            pygame.quit()
            exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                direction = 0
            elif event.key == pygame.K_DOWN:
                direction = 1
            elif event.key == pygame.K_LEFT:
                direction = 2
            elif event.key == pygame.K_RIGHT:
                direction = 3
    pygame.display.flip()

    old_positions = copy.deepcopy(snake_positions)

    if to_append:
        snake_positions.append(old_positions[-1])
        to_append = False

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

    if snake_positions[0] in apples_positions:
        apples_positions.remove(snake_positions[0])
        apple = [0, 0]
        while apple in snake_positions or apple in apples_positions:
            apple = [random.randint(0, 29), random.randint(0, 29)]
        apples_positions.append(apple)
        to_append = True
    clock.tick(15)
