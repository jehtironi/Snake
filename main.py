##################################################
#Academicos: Jéssica Cristina Tironi,            #
#            Caio Halmenschlager Foresti e       #
#            Maria Julia Lamim Severino          #
#                                                #
#            JOGO DA COBRINHA(SNAKE)             #
##################################################

import pygame, random
from pygame.locals import *


WINDOW_SIZE = (600, 600)
PIXEL_SIZE = 10
cont = 0

pygame.init()
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption('Snake')

snake_pos = [(250, 50), (260, 50), (270, 50)]
snake_surface = pygame.Surface((PIXEL_SIZE, PIXEL_SIZE))
snake_surface.fill((0, 250, 164))
snake_direction = K_LEFT

apple_surface = pygame.Surface((PIXEL_SIZE, PIXEL_SIZE))
apple_surface.fill((255, 0, 0))

font = pygame.font.Font('freesansbold.ttf', 18)

def random_on_grid():
    x = random.randint(0, WINDOW_SIZE[0])
    y = random.randint(0, WINDOW_SIZE[1])
    return x // PIXEL_SIZE * PIXEL_SIZE, y // PIXEL_SIZE * PIXEL_SIZE


def restart_game():
    global snake_pos
    global apple_pos
    global snake_direction
    snake_pos = [(250, 50), (260, 50), (270, 50)]
    snake_direction = K_LEFT
    apple_pos = random_on_grid()


def collision(pos1, pos2):
    return pos1 == pos2


def off_limits(pos):
    if 0 <= pos[0] < WINDOW_SIZE[0] and 0 <= pos[1] < WINDOW_SIZE[1]:
        return False
    else:
        return True

apple_pos = random_on_grid()

while True:

    if cont < 5:
        pygame.time.Clock().tick(10)
    elif cont < 25:
        pygame.time.Clock().tick(15)
    elif cont < 50:
        pygame.time.Clock().tick(20)
    elif cont < 75:
        pygame.time.Clock().tick(25)
    elif cont < 100:
        pygame.time.Clock().tick(30)
    elif cont < 125:
        pygame.time.Clock().tick(35)
    elif cont < 150:
        pygame.time.Clock().tick(40)
    elif cont < 175:
        pygame.time.Clock().tick(45)
    elif cont < 200:
        pygame.time.Clock().tick(50)
    elif cont < 225:
        pygame.time.Clock().tick(55)
    elif cont < 250:
        pygame.time.Clock().tick(60)
    elif cont < 275:
        pygame.time.Clock().tick(65)
    elif cont < 300:
        pygame.time.Clock().tick(70)
    elif cont < 325:
        pygame.time.Clock().tick(75)
    elif cont < 350:
        pygame.time.Clock().tick(80)
    elif cont < 375:
        pygame.time.Clock().tick(85)
    elif cont < 400:
        pygame.time.Clock().tick(90)
    elif cont < 425:
        pygame.time.Clock().tick(95)
    elif cont < 450:
        pygame.time.Clock().tick(100)

    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            quit()

        elif event.type == KEYDOWN:
            if event.key in [K_UP, K_DOWN, K_LEFT, K_RIGHT]:
                snake_direction = event.key

    screen.blit(apple_surface, apple_pos)

    score_font = font.render('Score: %s' % (cont), True, (255, 255, 255))
    score_rect = score_font.get_rect()
    score_rect.topleft = (600 - 120, 10)
    screen.blit(score_font, score_rect)

    if collision(apple_pos, snake_pos[0]):
        snake_pos.append((-10,0))
        cont = cont + 1
        apple_pos = random_on_grid()

    for pos in snake_pos:
        screen.blit(snake_surface, pos)

    for i in range(len(snake_pos)-1, 0, -1):
        if collision(snake_pos[0], snake_pos[i]):
            cont = 0
            restart_game()

        snake_pos[i] = snake_pos[i-1]

    if off_limits(snake_pos[0]):
        cont = 0
        restart_game()


    if snake_direction == K_UP:
        snake_pos[0] = (snake_pos[0][0], snake_pos[0][1] - PIXEL_SIZE)

    elif snake_direction == K_DOWN:
        snake_pos[0] = (snake_pos[0][0], snake_pos[0][1] + PIXEL_SIZE)

    elif snake_direction == K_LEFT:
        snake_pos[0] = (snake_pos[0][0] - PIXEL_SIZE, snake_pos[0][1])

    elif snake_direction == K_RIGHT:
        snake_pos[0] = (snake_pos[0][0] + PIXEL_SIZE, snake_pos[0][1])

    pygame.display.update()

