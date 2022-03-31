# Judo Space Main
# March 15, 2022
# Dustin S, Dylan G, and Zachary H

import pygame
import random
import time
from Enemy import Control_AI
from background import Space
from lifebar import Lifebar
import projectile as pro
import collision as col
import title_screen
from player import Player
import health_drop as h_drop


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
PLAYER_SPEED = 300
BULLET_LIFE = 3
BULLET_COLOR = (200, 0, 0)
ENEMY_BULLET_COLOR = (0, 0, 200)
PLAYER_LIFE = 100
PLAYER_RADIUS = 15
h_i_spawn_set = 10
health_item_spawn_timer = h_i_spawn_set

shoot_timer = .25
First = True
Current_Basic_Enemy = 0
Basic_Enemy_Count = 0
spawn_rate = 0

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) # Dylan, you can change if you want.
finished = False

clock = pygame.time.Clock()

Level = 0
shoot_aggression = 1500
player_x = SCREEN_WIDTH / 2
player_y = (SCREEN_HEIGHT / 2) + (SCREEN_HEIGHT / 3)
S = Space(100, 400) # The bigger the first number, the bigger the space between stars
AI = Control_AI()
# The bigger the second number, the faster the stars
P = pro.Projectile()
E = pro.Enemy_Projectile()
H = h_drop.Health()

spawn_timer = 0

# Create the Player entity
Player = Player(player_x, player_y, PLAYER_RADIUS, PLAYER_LIFE, PLAYER_SPEED)

life = Lifebar()
title = title_screen.Title_Screen(SCREEN_WIDTH, SCREEN_HEIGHT)
title_click = False
show_credits = False

while not finished:
    #Update
    delta_time = clock.tick() / 1000
    P.update(delta_time, screen, BULLET_COLOR)
    E.update(delta_time, screen, ENEMY_BULLET_COLOR)
    S.update(delta_time, SCREEN_WIDTH, SCREEN_HEIGHT)
    AI.update(delta_time)
    H.update(delta_time)
    if title_click == True and show_credits == False:
        life.update(Player.life)

    # Collision between player bullet and enemy (DAS):
    for b in P.bullet_list:
        point_1 = (b[0][0], b[0][1])
        for e in AI.AI_List:
            point_2 = (e.x, e.y)
            if col.Collision(point_1, point_2, 5, e.radius).collide():
                b[1] = 0
                e.life_value -= 1
                # Below is for Level God tracking purpose
                if e.life_value <= 0 and e.Dog_Tag == "Basic":
                    Current_Basic_Enemy -= 1
                    Basic_Enemy_Count -= 1

    # Enemies shooting (DAS):
    shoot_timer -= delta_time
    if shoot_timer <= 0:
        shoot_timer = .25
        for e in AI.AI_List:
            if e.Dog_Tag == "Basic":
                e.aggression -= 1
                if e.aggression <= 0:
                    e.aggression = 3
                    if e.dodge:
                        E.spawn(e.x, e.y, e.life_value)

    # Collision between player and enemy bullet (DAS):
    for u in E.bullet_list:
        point_3 = (u[0][0], u[0][1])
        if col.Collision(point_3, (Player.x, Player.y), 5, Player.r).collide():
            u[1] = 0
            Player.life -= 10

    # Health Item Spawning (DAS):
    if title_click:
        health_item_spawn_timer -= delta_time
        # print(health_item_spawn_timer)
        if health_item_spawn_timer <= 0:
            h_random = random.randint(1, 5) # Every {spawn_timer} seconds, it rolls a die to see if it spawns.
            # print(f"RANDOM VAL = {h_random}")
            if h_random == 1:
                H.spawn(15, 1, 15)
            health_item_spawn_timer = h_i_spawn_set

    # Health item collision with player bullet and player (DAS):
    for h in H.health_drop_list:
        point_4 = (h[0][0], h[0][1])
        for b in P.bullet_list:
            point_5 = (b[0][0], b[0][1])
            if col.Collision(point_4, point_5, 5, h[3]).collide():
                h[1] = 0
                b[1] = 0
        if col.Collision(point_4, (Player.x, Player.y), h[3], Player.r).collide() and h[5] == True:
            h[0][0] = 901
            if Player.life <= PLAYER_LIFE - h[2]: # Checks to see if healing will not make bar go over rect.
                Player.life += h[2]
            else: # If it will, then the bar will just go back to full.
                Player.life = PLAYER_LIFE

    #Handling Inputs
    event = pygame.event.poll()
    all_keys = pygame.key.get_pressed()  #This is the key inputs
    if event.type == pygame.quit:
        finished = True
    all_keys = pygame.key.get_pressed()  #This is the key inputs too
    if all_keys[pygame.K_ESCAPE]:
        finished = True

    if title_click == True and show_credits == False:
        Player.handle_input(all_keys, event, delta_time)

    if title_click == True and show_credits == False:
        #Dustin can insert what's needed for imputing the projectile commands
        if event.type == pygame.MOUSEBUTTONDOWN:
            P.spawn(Player.x, Player.y, BULLET_LIFE)

    # Add a Basic AI Enemy
    if title_click == True and show_credits == False:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_x:
                # Do NOT make the radius bigger than the lowest potential value of the temp_var
                temp_var = random.randint(30, SCREEN_WIDTH - 30)
                AI.add_basic_enemy(15, 200, temp_var)
            if event.key == pygame.K_t:
                temp_var = random.randint(100, SCREEN_WIDTH - 100)
                AI.add_tracker(20, temp_var, 10)

    mouse_pos = pygame.mouse.get_pos()
    mouse_x = mouse_pos[0]
    mouse_y = mouse_pos[1]
    mouse_rect = pygame.Rect(mouse_x - 1, mouse_y - 1, 2, 2)

    #Remove the title screen
    #if all_keys[pygame.K_SPACE]:
        #title_click = True

    if title_click == False:
        if mouse_rect.colliderect(title.circle_rect_c) and event.type == pygame.MOUSEBUTTONDOWN:
            show_credits = True     #Credits button
            title_click = True
        if mouse_rect.colliderect(title.circle_rect_p) and event.type == pygame.MOUSEBUTTONDOWN:
            show_credits = False    #Play button
            title_click = True
            Level = 1
            First = True
        if mouse_rect.colliderect(title.circle_rect_e) and event.type == pygame.MOUSEBUTTONDOWN:
            finished = True     #Exit button
    elif show_credits == True:
        if mouse_rect.colliderect(title.credits_back_rect) and event.type == pygame.MOUSEBUTTONDOWN:
            show_credits = False    #Back button (in the credits)
            title_click = False

    # Below is the LEVEL GOD, that controls the Levels

    if Level == 1:
        if First:
            Basic_Enemy_Count = 10
            Current_Basic_Enemy = 0
            spawn_rate = 5
            spawn_timer = 0
            shoot_aggression = 1000
            First = False

        spawn_timer -= delta_time
        if spawn_timer <= 0:
            spawn_timer = spawn_rate
            if Current_Basic_Enemy < Basic_Enemy_Count:
                # Do NOT make the radius bigger than the lowest potential value of the temp_var
                temp_var = random.randint(30, SCREEN_WIDTH - 30)
                AI.add_basic_enemy(15, 200, temp_var)
                Current_Basic_Enemy += 1

        if Basic_Enemy_Count == 0:
            print("Level Completed")







    #Drawing
    screen.fill((0, 0, 0))
    S.draw(screen)
    AI.draw(screen)
    P.draw(screen, BULLET_COLOR)
    E.draw(screen, ENEMY_BULLET_COLOR)
    if title_click == True and show_credits == False:
        Player.draw(screen)
        H.draw(screen)
        life.draw(screen)
        title.display_level_one(screen)
    if title_click == False:
        title.draw(screen)
    if show_credits == True:
        title.display_credits(screen)
    if Player.life <= 0:
        title.display_game_over(screen)
        pygame.display.flip()
        print("Game Over!")
        time.sleep(3)
        finished = True

    pygame.display.flip()

pygame.display.quit()