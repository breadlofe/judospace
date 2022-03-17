# Judo Space Main
# March 15, 2022
# Dustin S, Dylan G, and Zachary H

import pygame

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) # Dylan, you can change if you want.
finished = False

clock = pygame.time.Clock()

player_x = SCREEN_WIDTH / 2
player_y = (SCREEN_HEIGHT / 2) + (SCREEN_HEIGHT / 3)

while not finished:
    #Update
    delta_time = clock.tick() / 1000
    player_x = player_x
    player_y = player_y

    # Input
    event = pygame.event.poll()
    if event.type == pygame.quit:
        done = True
    all_keys = pygame.key.get_pressed()     #This is the key inputs
    if all_keys[pygame.K_ESCAPE]:
        finished = True

    if all_keys[pygame.K_a]:     #Left
        player_x -= 100 * delta_time
    if all_keys[pygame.K_d]:     #Right
        player_x += 100 * delta_time
    if all_keys[pygame.K_w]:     #Up
        player_y -= 100 * delta_time
    if all_keys[pygame.K_s]:     #Down
        player_y += 100 * delta_time
    if all_keys[pygame.K_e]:     #Dash
        player_y -= 200 * delta_time

    #Dustin can insert what's needed for imputing the bullet commands
    all_mouse_buttons = pygame.mouse.get_pressed()
    #ZDH TO-DO: Find the code for left mouse click
    if all_keys[pygame.K_SPACE]:    #Fire Bullet
        pass

    # Drawling
    screen.fill((0, 0, 0))

    pygame.display.flip()

pygame.display.quit()