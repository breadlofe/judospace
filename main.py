# Judo Space Main
# March 15, 2022
# Dustin S, Dylan G, and Zachary H

import pygame
import projectile
from background import Space

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) # Dylan, you can change if you want.
finished = False

clock = pygame.time.Clock()

player_x = SCREEN_WIDTH / 2
player_y = (SCREEN_HEIGHT / 2) + (SCREEN_HEIGHT / 3)
S = Space(100, 400) # The bigger the first number, the bigger the space between stars
# The bigger the second number, the faster the stars

proj = projectile.Projectile(player_x, player_y)

while not finished:
    #Update
    delta_time = clock.tick() / 1000
    player_x = player_x
    player_y = player_y

    S.update(delta_time, SCREEN_WIDTH, SCREEN_HEIGHT)

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

    #Dustin can insert what's needed for imputing the projectile commands
    all_mouse_buttons = pygame.mouse.get_pressed()
    if all_mouse_buttons[0]:    #Fire Projectiles
        pass

    # Drawing
    screen.fill((0, 0, 0))
    S.draw(screen)

    #This is to test a player movement to begin with:
    pygame.draw.circle(screen, (255, 200, 0), (player_x, player_y), 15)

    pygame.display.flip()

pygame.display.quit()