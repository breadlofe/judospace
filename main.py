# Judo Space Main
# March 15, 2022
# Dustin, Dylan, and Zach



import pygame

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) # Dylan, you can change if you want.
finished = False


clock = pygame.time.Clock()

player_x = 240
player_y = 600

while not finished:
    #Update
    delta_time = clock.tick() / 1000

    # Input
    event = pygame.event.poll()
    if event.type == pygame.quit:
        done = True
    all_keys = pygame.key.get_pressed()
    if all_keys[pygame.K_ESCAPE]:
        finished = True

    # Drawling
    screen.fill((0, 0, 0))

    pygame.display.flip()

pygame.display.quit()