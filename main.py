# Judo Space Main
# March 15, 2022
# Dustin S, Dylan G, and Zachary H

import pygame
import random
import time
import vector
from Enemy import Control_AI
from background import Space
from lifebar import Lifebar
from lifebar import Boss_Lifebar
import projectile as pro
import collision as col
import title_screen
from player import Player
import health_drop as h_drop
import Score
import jukebox
from Enemy import Boss_Arms

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
PLAYER_SPEED = 300
BULLET_LIFE = 3
BULLET_COLOR = (200, 0, 0)
ENEMY_BULLET_COLOR = (255, 0, 0)
PLAYER_LIFE = 100
PLAYER_RADIUS = 15
h_i_spawn_set = 10
health_item_spawn_timer = h_i_spawn_set

boss_attacking = False
change_attack = 0
attack_type = 0
boss_timer = 0
reset_timer = 0
continue_attack = 0
temp = 0
shoot_timer = .25
First = True
Game = False

# This is a bunch of variables required for the Level God to function. The reason its all 0 is just so that we don't
# get a bunch of bugs saying values are undefined.
Current_Elites = 0
Elite_Count = 0
Current_Basic_Enemy = 0
Current_Tracker_Enemy = 0
Basic_Enemy_Count = 0
Tracker_Enemy_Count = 0
spawn_rate = 0
tracker_rate = 0
tracker_set_rate = 0
elite_set_rate = 0
elite_rate = 0
enemy_total = 0


pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) # Dylan, you can change if you want.
finished = False

clock = pygame.time.Clock()

# Sound
J = jukebox.Jukebox()

Level = 0
player_x = SCREEN_WIDTH / 2
player_y = (SCREEN_HEIGHT / 2) + (SCREEN_HEIGHT / 3)
S = Space(100, 400) # The bigger the first number, the bigger the space between stars
AI = Control_AI()
# The bigger the second number, the faster the stars
P = pro.Projectile()
E = pro.Enemy_Projectile()
T = pro.Tracker_Projectile()
H = h_drop.Health()
score = Score.Score(SCREEN_WIDTH, SCREEN_HEIGHT, 0)

spawn_timer = 0
game_over_timer = 3
level_complete_timer = 2
level_complete_general = False
warning_timer = 2.5
warning_timer_done = False
end_timer = 5

# Create the Player entity
Player = Player(player_x, player_y, PLAYER_RADIUS, PLAYER_LIFE, PLAYER_SPEED)

life = Lifebar()
boss_life = Boss_Lifebar()
title = title_screen.Title_Screen(SCREEN_WIDTH, SCREEN_HEIGHT)
title_click = False
show_credits = False
show_logline = False

J.music("menu")

while not finished:
    #Update
    # if not Player.parried:
    delta_time = clock.tick() / 1000
    if Player.parried:
        delta_time = clock.tick() * 0
        pygame.time.wait(50)  # Milliseconds just to show the player they parried.
        Player.parried = False
    S.update(delta_time, SCREEN_WIDTH, SCREEN_HEIGHT)
    if title_click == True and show_credits == False and show_logline == False:
        P.update(delta_time, screen, BULLET_COLOR)
        E.update(delta_time, screen, ENEMY_BULLET_COLOR)
        T.update(delta_time)
        AI.update(delta_time)
        H.update(delta_time)
    if title_click == True and show_credits == False and show_logline == False:
        Player.update(delta_time)
        life.update(Player.life)
        if Level == 10 and not level_complete_general:
            for i in AI.Boss_List:
                if i.Dog_Tag == "Left Arm":
                    boss_life.update_left(AI.get_boss_life(0))
                if i.Dog_Tag == "Boss Body":
                    boss_life.update_middle(AI.get_boss_life(1))
                if i.Dog_Tag == "Right Arm":
                    boss_life.update_right(AI.get_boss_life(2))

    # Collision between player bullet and enemy (DAS):
    for b in P.bullet_list:
        point_1 = (b[0][0], b[0][1])
        for e in AI.AI_List:
            point_2 = (e.x, e.y)
            if col.Collision(point_1, point_2, 5, e.radius).collide():
                b[1] = 0
                e.life_value -= 1
                J.sfx("e_hit")
                # Below is for Level God tracking purpose
                if e.life_value <= 0 and e.Dog_Tag == "Basic":
                    Current_Basic_Enemy -= 1
                    Basic_Enemy_Count -= 1
                    enemy_total -= 1
                    score.add_to_score(10)
                if e.life_value <= 0 and e.Dog_Tag == "Tracker":
                    Current_Tracker_Enemy -= 1
                    Tracker_Enemy_Count -= 1
                    score.add_to_score(30)
                    enemy_total -= 1
                if e.life_value <= 0 and e.Dog_Tag == "Elite":
                    Current_Elites -= 1
                    Elite_Count -= 1
                    score.add_to_score(50)
                    enemy_total -= 1

    # Enemies shooting (DAS):
    shoot_timer -= delta_time
    if shoot_timer <= 0:
        shoot_timer = .25
        for e in AI.AI_List:
            e.aggression -= 1
            if e.aggression <= 0:
                if e.Dog_Tag == "Basic":
                        e.aggression = 3
                        if e.dodge:
                            E.spawn(e.x, e.y, e.life_value)
                if e.Dog_Tag == "Tracker":
                    e.aggression = 3
                    if e.gattling_track > 0:
                        e.aggression = 1
                        e.gattling_track -= 1
                    else:
                        e.gattling_track = 2
                    gattling_track = True
                    if e.dodge:
                        P_Vec = vector.Vector(Player.x, Player.y)
                        T_Vec = vector.Vector(e.x, e.y)
                        Q = P_Vec - T_Vec
                        Value = Q / Q.norm(2)
                        bullet_vel = Value * 500
                        T.spawn(e.x, e.y, 20, bullet_vel[0], bullet_vel[1], 5)
                if e.Dog_Tag == "Elite":
                    e.aggression = 1
                    if e.dodge:
                        P_Vec = vector.Vector(Player.x, Player.y)
                        T_Vec = vector.Vector(e.x, e.y)
                        Q = P_Vec - T_Vec
                        Value = Q / Q.norm(2)
                        bullet_vel = Value * 500
                        T.spawn(e.x, e.y, 20, bullet_vel[0], bullet_vel[1], 5)

    # Boss Attacking System

    if Level == 10 and not level_complete_general:

        if not boss_attacking:
            change_attack -= delta_time
            if change_attack <= 0:
                attack_type = random.randint(0, 1)
                boss_attacking = True
                if attack_type == 0:
                    boss_timer = .2
                    reset_timer = boss_timer
                    continue_attack = 7
                if attack_type == 1:
                    boss_timer = .05
                    reset_timer = boss_timer
                    continue_attack = 5
        if boss_attacking:
            for i in AI.Boss_List:
                if attack_type == 0:
                    boss_timer -= delta_time
                    if boss_timer <= 0:
                        boss_timer = reset_timer
                        if i.Dog_Tag == "Right Arm" or i.Dog_Tag == "Left Arm":
                            P_Vec = vector.Vector(Player.x, Player.y)
                            T_Vec = vector.Vector(i.x, i.y)
                            Q = P_Vec - T_Vec
                            Value = Q / Q.norm(2)
                            bullet_vel = Value * 500
                            T.spawn(i.x, i.y, 20, bullet_vel[0], bullet_vel[1], 5)
                if attack_type == 1:
                    boss_timer -= delta_time
                    if boss_timer <= 0:
                        boss_timer = reset_timer
                        if i.Dog_Tag == "Boss Body":
                            P_Vec = vector.Vector(Player.x, Player.y)
                            T_Vec = vector.Vector(i.x, i.y)
                            Q = P_Vec - T_Vec
                            Value = Q / Q.norm(2)
                            bullet_vel = Value * 500
                            T.spawn(i.x, i.y, 50, bullet_vel[0], bullet_vel[1], 50)

                continue_attack -= delta_time
                if continue_attack <= 0:
                    boss_attacking = False
                    change_attack = 2





    # Collision between player and enemy bullet (DAS):
    for u in E.bullet_list:
        point_3 = (u[0][0], u[0][1])
        if col.Collision(point_3, (Player.x, Player.y), 5, Player.r).collide() and Player.life > 0 and \
                not Player.is_dashing:
            u[1] = 0
            Player.got_hit = True
            Player.life -= 10 * Player.chip
            # Player.got_hit = False
    for u in T.bullet_list:
        point_3 = (u[0][0], u[0][1])
        if col.Collision(point_3, (Player.x, Player.y), 5, Player.r).collide() and Player.life > 0 and \
                not Player.is_dashing:
            u[1] = 0
            Player.got_hit = True
            Player.life -= 10 * Player.chip

    # Health Item Spawning (DAS):
    if title_click == True and show_credits == False and show_logline == False:
        health_item_spawn_timer -= delta_time
        # print(health_item_spawn_timer)
        if health_item_spawn_timer <= 0:
            h_random = random.randint(1, 5) # Every {spawn_timer} seconds, it rolls a die to see if it spawns.
            # print(f"RANDOM VAL = {h_random}")
            if h_random == 1:
                H.spawn(15, 1, 35)
            health_item_spawn_timer = h_i_spawn_set

    # Health item collision with player bullet and player (DAS):
    for h in H.health_drop_list:
        point_4 = (h[0][0], h[0][1])
        for b in P.bullet_list:
            point_5 = (b[0][0], b[0][1])
            if col.Collision(point_4, point_5, 5, h[3]).collide():
                h[1] = 0
                b[1] = 0
                J.sfx("h_hit")
        if col.Collision(point_4, (Player.x, Player.y), h[3], Player.r).collide() and h[5] == True:
            h[0][0] = 901
            J.sfx("h_get")
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

    if title_click == True and show_credits == False and show_logline == False and Player.life > 0:
        Player.handle_input(all_keys, event, delta_time)

    if title_click == True and show_credits == False and show_logline == False:
        #Dustin can insert what's needed for imputing the projectile commands
        if event.type == pygame.MOUSEBUTTONDOWN and not Player.blocking and Player.life > 0 and event.button == 1:    # Player can't shoot while blocking.
            P.spawn(Player.x, Player.y, BULLET_LIFE)

    # Add a Basic AI Enemy
    # if title_click == True and show_credits == False and show_logline == False:
    #     if event.type == pygame.KEYDOWN:
    #         if event.key == pygame.K_x:
    #             # Do NOT make the radius bigger than the lowest potential value of the temp_var
    #             temp_var = random.randint(30, SCREEN_WIDTH - 30)
    #             AI.add_basic_enemy(15, 200, temp_var)
    #         if event.key == pygame.K_t:
    #             temp_var = random.randint(100, SCREEN_WIDTH - 100)
    #             AI.add_tracker(20, temp_var, 5)
    #         if event.key == pygame.K_q:
    #             temp_var = random.randint(100, SCREEN_WIDTH - 100)
    #             AI.add_elite(20, temp_var, 10)
    #         if event.key == pygame.K_b:
    #             AI.spawn_boss()

    mouse_pos = pygame.mouse.get_pos()
    mouse_x = mouse_pos[0]
    mouse_y = mouse_pos[1]
    mouse_rect = pygame.Rect(mouse_x - 1, mouse_y - 1, 2, 2)

    if title_click == False:
        #if show_logline == False:
        if mouse_rect.colliderect(title.circle_rect_c) and event.type == pygame.MOUSEBUTTONDOWN:
            J.sfx("menu")
            show_credits = True     #Credits button
            title_click = True
        show_logline = False
        if mouse_rect.colliderect(title.circle_rect_p) and event.type == pygame.MOUSEBUTTONDOWN:
            # J.sfx("menu")
            # show_credits = False  # Play button
            # title_click = True
            # J.music("level_one")
            # Level = 10  # Change this value IF you wish to jump to test other levels.
            # First = True
            # Game = True
            show_logline = True
            title_click = True
        if mouse_rect.colliderect(title.circle_rect_e) and event.type == pygame.MOUSEBUTTONDOWN:
            J.sfx("quit")
            finished = True     #Exit button
    elif show_credits == True:
        if mouse_rect.colliderect(title.credits_back_rect) and event.type == pygame.MOUSEBUTTONDOWN:
            J.sfx("menu")
            show_credits = False    #Back button (in the credits)
            title_click = False
            show_logline = False
    if show_logline == True:
        title_click = True
        show_credits = False
        if mouse_rect.colliderect(title.logline_continue_rect) and event.type == pygame.MOUSEBUTTONDOWN:
            J.sfx("menu")
            show_credits = False  # Play button
            show_logline = False
            title_click = True
            J.music("level_one")
            Level = 1  # Change this value IF you wish to jump to test other levels.
            First = True
            Game = True

    # Below is the LEVEL GOD, that controls the Levels
    if Game:
        # So this will check to see which level it is, and then if this is the first time its run through the level
        # If it is, then it sets the values for the level (How many enemies, how fast they spawn, etc.
        if First:
            if Level == 1:
                Basic_Enemy_Count = 4
                Current_Basic_Enemy = 0
                spawn_rate = 3

            if Level == 2:
                Basic_Enemy_Count = 6
                Current_Basic_Enemy = 0
                spawn_rate = 2

            if Level == 3:
                Basic_Enemy_Count = 6
                Tracker_Enemy_Count = 1
                spawn_rate = 2
                tracker_set_rate = 6

            if Level == 4:
                Basic_Enemy_Count = 6
                Tracker_Enemy_Count = 2
                spawn_rate = 1.5
                tracker_set_rate = 5

            if Level == 5:
                Basic_Enemy_Count = 8
                Tracker_Enemy_Count = 2
                spawn_rate = 1.5
                tracker_set_rate = 4.5

            if Level == 6:
                Basic_Enemy_Count = 8
                Tracker_Enemy_Count = 2
                spawn_rate = 1
                tracker_set_rate = 4
                elite_set_rate = 12
                Elite_Count = 1

            if Level == 7:
                Basic_Enemy_Count = 10
                Tracker_Enemy_Count = 3
                spawn_rate = 1
                tracker_set_rate = 4
                elite_set_rate = 12
                Elite_Count = 1

            if Level == 8:
                Basic_Enemy_Count = 15
                Tracker_Enemy_Count = 4
                spawn_rate = 0.5
                tracker_set_rate = 4
                elite_set_rate = 12
                Elite_Count = 2

            if Level == 9:
                Basic_Enemy_Count = 20
                Tracker_Enemy_Count = 5
                spawn_rate = 0.5
                tracker_set_rate = 3
                elite_set_rate = 12
                Elite_Count = 2

            if Level == 10:
                AI.spawn_boss()
                #Basic_Enemy_Count = 2
                #spawn_rate = 0.5
                #Dylan or Dustin, you can change this placeholder battle for the boss   ~ZDH

            elite_rate = elite_set_rate
            tracker_rate = tracker_set_rate
            spawn_timer = 0
            enemy_total = Basic_Enemy_Count + Elite_Count + Tracker_Enemy_Count
            First = False
            level_complete_general = False

        spawn_timer -= delta_time
        if spawn_timer <= 0:
            spawn_timer = spawn_rate
            if Current_Basic_Enemy < Basic_Enemy_Count:
                # Do NOT make the radius bigger than the lowest potential value of the temp_var
                temp_var = random.randint(30, SCREEN_WIDTH - 30)
                AI.add_basic_enemy(15, 200, temp_var)
                Current_Basic_Enemy += 1

        if 0 < Tracker_Enemy_Count:
            tracker_rate -= delta_time
            if tracker_rate <= 0 and Current_Tracker_Enemy < Tracker_Enemy_Count:
                temp_var = random.randint(80, SCREEN_WIDTH - 80)
                AI.add_tracker(20, temp_var, 5)
                tracker_rate = tracker_set_rate
                Current_Tracker_Enemy += 1

        if 0 < Elite_Count:
            elite_rate -= delta_time
            if elite_rate <= 0 and Current_Elites < Elite_Count:
                temp_var = random.randint(80, SCREEN_WIDTH - 80)
                AI.add_elite(30, temp_var, 5)
                elite_rate = elite_set_rate
                Current_Elites += 1

        # Boss collision
        if Level == 10:
            #print(Player.x)
            for i in AI.Boss_List:
                if i.Dog_Tag == "Right Arm":
                    i.rotate(Player.x, Player.y)
                    pass
                elif i.Dog_Tag == "Left Arm":
                    i.rotate(Player.x, Player.y)
                    pass
            for b in P.bullet_list:
                point = (b[0][0], b[0][1])
                for i in AI.Boss_List:
                    if i.Dog_Tag == "Right Arm" or i.Dog_Tag == "Left Arm":
                        temp = col.AlphaCollision(i.bounder, b[0][0], b[0][1])
                    elif i.Dog_Tag == "Boss Body":
                        point_2 = (i.x, i.y)
                        if col.Collision(point, point_2, 5, i.radius).collide():
                            b[1] = 0
                            i.life_value -= 20
                            J.sfx("b_a_hit")
                    if i.Dog_Tag == "Right Arm" or i.Dog_Tag == "Left Arm":
                        if temp.collide():
                            J.sfx("b_a_hit")
                            i.life_value -= 20
                            b[1] = 0

                    if i.life_value <= 0:
                        AI.Boss_List.remove(i)


    #Drawing
    screen.fill((0, 0, 0))
    S.draw(screen)
    if title_click == True and show_credits == False and show_logline == False:
        E.draw(screen, ENEMY_BULLET_COLOR)
        T.draw(screen, ENEMY_BULLET_COLOR)
        P.draw(screen, BULLET_COLOR)
        AI.draw(screen)
    if title_click == True and show_credits == False and show_logline == False:
        if Player.life > 0:
            Player.draw(screen)
        H.draw(screen)
        life.draw(screen)
        if Level == 10:
            boss_life.draw(screen)

        #Boolean needed for false and false:    ~ZDH
        if Level == 1 and not level_complete_general:
            #title.display_level_one(screen)
            title.level_text_ren(Level)
            title.display_level(screen)
            if enemy_total == 0:
                #title.display_level_one_completed(screen)
                title.complete_text(Level)
                title.display_level_completed(screen)
                level_complete_timer -= delta_time
                if level_complete_timer <= 0:
                    level_complete_timer = 2
                    Level = 2
                    First = True
                    level_complete_general = True

        #Boolean needed for true and false:     ~ZDH
        if Level == 2 and not level_complete_general:
            #title.display_level_two(screen)
            title.level_text_ren(Level)
            title.display_level(screen)
            if enemy_total == 0:
                #title.display_level_two_completed(screen)
                title.complete_text(Level)
                title.display_level_completed(screen)
                level_complete_timer -= delta_time
                if level_complete_timer <= 0:
                    Level = 3
                    level_complete_timer = 2
                    First = True
                    level_complete_general = True

        #Boolean needed for true and true:      ~ZDH
        if Level == 3 and not level_complete_general:
            # This needs to be updated and fixed so that the complete and the passive level are shown
            #title.display_level_three(screen)
            title.level_text_ren(Level)
            title.display_level(screen)
            if enemy_total == 0:
                #title.display_level_three_completed(screen)
                title.complete_text(Level)
                title.display_level_completed(screen)
                level_complete_timer -= delta_time
                if level_complete_timer <= 0:
                    level_complete_timer = 2.5
                    Level = 4
                    First = True
                    level_complete_general = True

        # Below is the level transitions, we just need to add all of the screen stuff. Soooo do that when you can - DG
        if Level == 4 and not level_complete_general:
            # title.display
            title.level_text_ren(Level)
            title.display_level(screen)
            if enemy_total == 0:
                title.complete_text(Level)
                title.display_level_completed(screen)
                level_complete_timer -= delta_time
                if level_complete_timer <= 0:
                    level_complete_timer = 2.5
                    Level = 5
                    First = True
                    level_complete_general = True

        if Level == 5 and not level_complete_general:
            # title.display
            title.level_text_ren(Level)
            title.display_level(screen)
            if enemy_total == 0:
                title.complete_text(Level)
                title.display_level_completed(screen)
                level_complete_timer -= delta_time
                if level_complete_timer <= 0:
                    level_complete_timer = 2.5
                    Level = 6
                    First = True
                    level_complete_general = True

        if Level == 6 and not level_complete_general:
            # title.display
            title.level_text_ren(Level)
            title.display_level(screen)
            if enemy_total == 0:
                title.complete_text(Level)
                title.display_level_completed(screen)
                level_complete_timer -= delta_time
                if level_complete_timer <= 0:
                    level_complete_timer = 2.5
                    Level = 7
                    First = True
                    level_complete_general = True

        if Level == 7 and not level_complete_general:
            # title.display
            title.level_text_ren(Level)
            title.display_level(screen)
            if enemy_total == 0:
                title.complete_text(Level)
                title.display_level_completed(screen)
                level_complete_timer -= delta_time
                if level_complete_timer <= 0:
                    level_complete_timer = 2.5
                    Level = 8
                    First = True
                    level_complete_general = True

        if Level == 8 and not level_complete_general:
            # title.display
            title.level_text_ren(Level)
            title.display_level(screen)
            if enemy_total == 0:
                title.complete_text(Level)
                title.display_level_completed(screen)
                level_complete_timer -= delta_time
                if level_complete_timer <= 0:
                    level_complete_timer = 2.5
                    Level = 9
                    First = True
                    level_complete_general = True

        if Level == 9 and not level_complete_general:
            # title.display
            title.level_text_ren(Level)
            title.display_level(screen)
            if enemy_total == 0:
                title.complete_text(Level)
                title.display_level_completed(screen)
                level_complete_timer -= delta_time
                if level_complete_timer <= 0:
                    level_complete_timer = 2.5
                    Level = 10
                    First = True
                    level_complete_general = True

        if Level == 10 and not level_complete_general:
            if warning_timer > 0: #and warning_timer_done == False:
                warning_timer -= delta_time
                title.display_thebosswarning(screen)
                warning_timer_done = True
            if warning_timer <= 0 and warning_timer_done == True:
                #title.level_text_ren(Level)
                #title.display_level(screen)
                title.display_bosslevel(screen)

                #Arms_Right.draw(screen)   # LOOK HERE
                #Arms_Left.draw(screen)    # LOOK HERE


                # BOSS COLLISION

                warning_timer = 0
                if AI.get_boss_life("hi") <= 0:    #placeholder boolean till the boss' health bar. ~ZDH
                    if level_complete_timer > 0:
                        title.display_bossdefeated(screen)
                        level_complete_timer -= delta_time
                    if level_complete_timer <= 0:
                        level_complete_timer = 0
                        title.display_final_credits(screen)
                        end_timer -= delta_time
                        if end_timer <= 0:
                            Player.life = 0  # Resets game and keeps score! DAS

        #If we do get a boss, we'd need one for the boss too.   ~ZDH
    if title_click == False and show_logline == False:
        title.draw(screen)
    if show_credits == True and show_logline == False:
        title.display_credits(screen)
        #title.display_final_credits(screen)
        #title.display_logline(screen)
    if show_logline == True and title_click == True:
        title.display_logline(screen)
    if Player.life <= 0: #and title_click == True:
        score.permanent_score(score.score)
        title.display_game_over(screen)
        game_over_timer -= delta_time
        if game_over_timer <= 0:

            #for e in range(enemy_total):
            for e in AI.AI_List:
                if Basic_Enemy_Count > 0:
                    e.life_value = 0
                if Tracker_Enemy_Count > 0:
                    e.life_value = 0
                if Elite_Count > 0:
                    e.life_value = 0
            enemy_total = 0
            for b in E.bullet_list:
                b[1] = 0
                E.update(delta_time, screen, [0,0,0])

            #finished = True
            Player.life = 100
            Level = 0
            show_credits = False
            show_logline = False
            Game = False
            title_click = False
            PLAYER_SPEED = 300
            BULLET_LIFE = 3
            BULLET_COLOR = (200, 0, 0)
            ENEMY_BULLET_COLOR = (255, 0, 0)
            PLAYER_LIFE = 100
            PLAYER_RADIUS = 15
            h_i_spawn_set = 10
            health_item_spawn_timer = h_i_spawn_set
            boss_attacking = False
            change_attack = 0
            attack_type = 0
            boss_timer = 0
            reset_timer = 0
            continue_attack = 0
            temp = 0
            shoot_timer = .25
            First = True
            Current_Elites = 0
            Elite_Count = 0
            Current_Basic_Enemy = 0
            Current_Tracker_Enemy = 0
            Basic_Enemy_Count = 0
            Tracker_Enemy_Count = 0
            spawn_rate = 0
            tracker_rate = 0
            tracker_set_rate = 0
            elite_set_rate = 0
            elite_rate = 0
            enemy_total = 0
            spawn_timer = 0
            game_over_timer = 3
            level_complete_timer = 2
            level_complete_general = False
            warning_timer = 2.5
            warning_timer_done = False
            end_timer = 5
            J = jukebox.Jukebox()
            player_x = SCREEN_WIDTH / 2
            player_y = (SCREEN_HEIGHT / 2) + (SCREEN_HEIGHT / 3)
            S = Space(100, 400)  # The bigger the first number, the bigger the space between stars
            AI = Control_AI()
            # The bigger the second number, the faster the stars
            P = pro.Projectile()
            E = pro.Enemy_Projectile()
            T = pro.Tracker_Projectile()
            H = h_drop.Health()
            score = Score.Score(SCREEN_WIDTH, SCREEN_HEIGHT, 0)
            life = Lifebar()
            boss_life = Boss_Lifebar()
            title = title_screen.Title_Screen(SCREEN_WIDTH, SCREEN_HEIGHT)
            J.music("menu")

            #Figure out a way to erase everything and return Level to 0.    ~ZDH.
            # Clutched it out ~DAS
    if title_click == True and show_credits == False and show_logline == False:
        score.display_score(screen)
        #ZDH TO DO: look three lines up and get the game over to a title screen.

    pygame.display.flip()

pygame.display.quit()