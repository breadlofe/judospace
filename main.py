# Judo Space Main
# March 15, 2022
# Dustin S, Dylan G, and Zachary H

import pygame
import random
from Enemy import Control_AI
from background import Space
import projectile as pro
import collision as col
import title_screen
from player import Player

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
PLAYER_SPEED = 300
BULLET_LIFE = 3
BULLET_COLOR = (200, 0, 0)
ENEMY_BULLET_COLOR = (0,0,200)
PLAYER_LIFE = 100
PLAYER_RADIUS = 15

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
E = pro.Enemy_Projectile()

# Create the Player entity
Player = Player(player_x, player_y, PLAYER_RADIUS, PLAYER_LIFE, PLAYER_SPEED)

title = title_screen.Title_Screen(SCREEN_WIDTH, SCREEN_HEIGHT)
title_click = False

while not finished:
    #Update
    delta_time = clock.tick() / 1000
    P.update(delta_time, screen, BULLET_COLOR)
    E.update(delta_time, screen, ENEMY_BULLET_COLOR)
    S.update(delta_time, SCREEN_WIDTH, SCREEN_HEIGHT)
    AI.update(delta_time)

    # Collision between player bullet and enemy (DAS):
    for b in P.bullet_list:
        point_1 = (b[0][0], b[0][1])
        for e in AI.AI_List:
            point_2 = (e.x, e.y)
            if col.Collision(point_1, point_2, 5, e.radius).collide():
                b[1] = 0
                e.life_value = 0

    # Enemies shooting (DAS):
    bullet_shoot = random.randint(1, 1500)
    for e in AI.AI_List:
        if bullet_shoot == 1:
            E.spawn(e.x, e.y, e.life_value)

    # Handle Inputs
    event = pygame.event.poll()
    all_keys = pygame.key.get_pressed()  # This is the key inputs
    if event.type == pygame.quit:
        done = True
    if all_keys[pygame.K_ESCAPE]:
        finished = True

    Player.handle_input(all_keys, event, delta_time)


    #Dustin can insert what's needed for imputing the projectile commands
    if event.type == pygame.MOUSEBUTTONDOWN:
        P.spawn(Player.x, Player.y, BULLET_LIFE)

    # Add a Basic AI Enemy
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_x:
            # Do NOT make the radius bigger than the lowest potential value of the temp_var
            temp_var = random.randint(30, SCREEN_WIDTH - 30)
            AI.add_basic_enemy(15, 200, temp_var)

    # Remove the title screen
    if all_keys[pygame.K_SPACE]:
        title_click = True
        # TO DO: ZDH Make a visible UI Button

    # Drawing
    screen.fill((0, 0, 0))
    S.draw(screen)
    AI.draw(screen)
    P.draw(screen, BULLET_COLOR)
    E.draw(screen, ENEMY_BULLET_COLOR)
    Player.draw(screen)
    if title_click == False:
        title.draw(screen)
        #title.desplay_level_one(screen)

    pygame.display.flip()

pygame.display.quit()