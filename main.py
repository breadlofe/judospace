# Judo Space Main
# March 15, 2022
# Dustin S, Dylan G, and Zachary H

import pygame
import random
from Enemy import Control_AI
from background import Space
import projectile as pro
import title_screen

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
PLAYER_SPEED = 300
BULLET_LIFE = 3
BULLET_COLOR = (200, 0, 0)

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) # Dylan, you can change if you want.
finished = False

clock = pygame.time.Clock()

player_x = SCREEN_WIDTH / 2
player_y = (SCREEN_HEIGHT / 2) + (SCREEN_HEIGHT / 3)
S = Space(100, 400) # The bigger the first number, the bigger the space between stars
AI = Control_AI()
# The bigger the second number, the faster the stars
P = pro.Projectile()
title = title_screen.Title_Screen(SCREEN_WIDTH, SCREEN_HEIGHT)
title_click = False

while not finished:
    #Update
    delta_time = clock.tick() / 1000
    player_x = player_x
    player_y = player_y
    P.update(delta_time, screen, BULLET_COLOR)
    S.update(delta_time, SCREEN_WIDTH, SCREEN_HEIGHT)
    AI.update(delta_time)

    if player_x <= 0:
        player_x = 0
    if player_x >= SCREEN_WIDTH:
        player_x = SCREEN_WIDTH
    if player_y <= 0:
        player_y = 0
    if player_y >= SCREEN_HEIGHT:
        player_y = SCREEN_HEIGHT

    # Input
    event = pygame.event.poll()
    if event.type == pygame.quit:
        done = True
    all_keys = pygame.key.get_pressed()     #This is the key inputs
    if all_keys[pygame.K_ESCAPE]:
        finished = True

    if all_keys[pygame.K_a]:     #Left
        player_x -= PLAYER_SPEED * delta_time
    if all_keys[pygame.K_d]:     #Right
        player_x += PLAYER_SPEED * delta_time
    if all_keys[pygame.K_w]:     #Up
        player_y -= PLAYER_SPEED * delta_time
    if all_keys[pygame.K_s]:     #Down
        player_y += PLAYER_SPEED * delta_time
    if all_keys[pygame.K_e]:     #Dash
        player_y -= (PLAYER_SPEED * 2) * delta_time

    #Dustin can insert what's needed for imputing the projectile commands
    if event.type == pygame.MOUSEBUTTONDOWN:
        P.spawn(player_x, player_y, BULLET_LIFE)

    # Add a Basic AI Enemy
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_x:
            temp_var = random.randint(0, SCREEN_WIDTH)
            AI.add_basic_enemy(10, 200, temp_var)

    # Remove the title screen
    if all_keys[pygame.K_SPACE]:
        title_click = True
        # TO DO: ZDH Make a visible UI Button
    # Drawing
    screen.fill((0, 0, 0))
    S.draw(screen)
    AI.draw(screen)

    #This is to test a player movement to begin with:
    pygame.draw.circle(screen, (255, 200, 0), (player_x, player_y), 15)
    P.draw(screen, BULLET_COLOR)
    if title_click == False:
        title.draw(screen)
        #title.desplay_level_one(screen)

    pygame.display.flip()

pygame.display.quit()