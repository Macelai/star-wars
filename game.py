import pygame
from pygame.locals import *

pygame.init()

display_widht = 600
display_height = 360

spaceship_widht = 84
spaceship_height = 50

shots_x = [999]
shots_y = [999]

gameDisplay = pygame.display.set_mode((display_widht, display_height))
pygame.display.set_caption('The battle of death')
clock = pygame.time.Clock()

spaceshipImg = pygame.image.load('spaceship.png')
backgroundImg = pygame.image.load('background.png')
laserImg = pygame.image.load('laser.png')

def spaceship(x,y):
    gameDisplay.blit(spaceshipImg, (x,y))

def shot(x,y):
    x += 4
    gameDisplay.blit(laserImg, (x,y))
    gameDisplay.blit(laserImg, (x, y + spaceship_height - 7))
    shots_x.append(x)
    shots_y.append(y)

def move_shoots():
    for i in range(len(shots_x)):
        shots_x[i] += 8
        if shots_x[i] < display_widht:
            gameDisplay.blit(laserImg, (shots_x[i],shots_y[i]))
            gameDisplay.blit(laserImg, (shots_x[i],shots_y[i] + spaceship_height - 7))

def game_loop():
    x = 0
    y = display_height * 0.5
    x_change = 0
    y_change = 0
    gameExit = False

    while not gameExit:
        gameDisplay.blit(backgroundImg, (0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    x_change = 4
                if event.key == pygame.K_LEFT:
                    x_change = -4
                if event.key == pygame.K_UP:
                    y_change = -4
                if event.key == pygame.K_DOWN:
                    y_change = 4
                if event.key == pygame.K_SPACE:
                    shot(x,y)

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                    x_change = 0
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    y_change = 0

        x += x_change
        y += y_change
        if y > display_height - spaceship_height:
            y = display_height - spaceship_height
        if x > display_widht - spaceship_widht:
            x = display_widht - spaceship_widht
        if x < 0:
            x = 0
        if y < 0:
            y = 0

        spaceship(x,y)
        move_shoots()
        pygame.display.update()
        clock.tick(60)

game_loop()
pygame.quit()
quit()
