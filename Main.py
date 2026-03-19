import random
from bdb import effective
from tkinter.constants import NORMAL
import pygame
import time
# Set the base of each variable
state = 0  # 1 - Selection / 2 - Battle / 3 - Won / 4 - Loss


#Attack Damage


pygame.init()
screen = pygame.display.set_mode((1400, 900))
clock = pygame.time.Clock()
show_popup = True

# Colour and text System
white = (255, 255, 255)
blue = (50, 150, 255)
gray = (200, 200, 200)
green = (0, 255, 0)
black = (0, 0, 0)

# Base variable set up
X = 10
Y = 770
MoveX = 7
MoveY = 5
PlayerSize = 50

# Image loading (State 1)
ui_img = pygame.image.load("nothing.png")

player_img = pygame.image.load("test.png").convert_alpha()
resized_player = pygame.transform.scale(player_img, (PlayerSize,PlayerSize))

unknown_img = pygame.image.load("nothing.png").convert_alpha()

background_img = pygame.image.load("Background.png").convert_alpha()
resized_background = pygame.transform.scale(background_img, (1400, 900))

Level_img = pygame.image.load("Level 1.png").convert_alpha()
resized_Level = pygame.transform.scale(Level_img, (1400, 900))

LevelBox_img = pygame.image.load("Level 1 (Hitbox).png").convert_alpha()
resized_LevelBox = pygame.transform.scale(LevelBox_img, (1400, 900))

player_hitbox = resized_player.get_rect()

pygame.display.set_caption('Proto-Zillama Reborn')

#program_img = pygame.image.load("Logo.png")
#pygame.display.set_icon(program_img)

# Music
#pygame.mixer.music.load("")

#Running of games
running = True
while running:
    screen.fill((0, 0, 0))
    current_time = pygame.time.get_ticks()
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                quit()
    old_X, old_Y = X, Y
    key = pygame.key.get_pressed()
    if key[pygame.K_UP]:
        Y = Y - MoveY
    if key[pygame.K_DOWN]:
        Y = Y + MoveY
    if key[pygame.K_LEFT]:
        X = X - MoveX
    if key[pygame.K_RIGHT]:
        X = X + MoveX
    # Update hitbox position to match player X and Y
    player_hitbox.topleft = (X, Y)

    wall_color = (100, 170, 150)

    # We check the pixel on the 'resized_Level' surface at player's center
    try:
        if resized_LevelBox.get_at((int(X + PlayerSize / 2), int(Y + PlayerSize / 2))) == wall_color:
            X, Y = old_X, old_Y  # Move them back if they hit a wall
    except IndexError:
        X, Y = old_X, old_Y  # Keep them on screen if they go out of bounds


    screen.blit(resized_background, (0, 0))
    screen.blit(resized_LevelBox, (0, 0))
    screen.blit(resized_Level, (0, 0))
    screen.blit(resized_player, (X, Y))
    pygame.draw.rect(screen, (0, 255, 0), player_hitbox, 2)

    pygame.display.flip()
    clock.tick(60)


