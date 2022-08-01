import pygame
from sprite import *
pygame.init()


def gamequit():
    pass


def default():
    fish.y = 245
    fish.isjump = False
    fish.isdive = False
    fish.isduck = False
    fish.j_vel = 22
    fish.j_resist = 1.08
    fish.d_vel = 1
    fish.d_resist = 1
    fish.duck = 5.9


def get_input():
    if not fish.isdive:
        if fish.y >= 245:
            default()

    if fish.isdive:
        fish.y = 313

    if fish.isjump:
        fish.y -= fish.j_vel
        fish.j_vel = fish.j_vel - fish.j_resist

    if fish.isduck:
        fish.j_vel = fish.duck

    if fish.isdive:
        fish.y += fish.d_vel
        fish.d_vel = fish.d_vel - fish.d_resist

    for event in pygame.event.get():
        # Keyboard key down input
        if event.type == pygame.KEYDOWN:
            # Jumping
            if event.key == pygame.K_UP or pygame.K_SPACE:
                fish.isjump = True
            # Ducking and Diving
            if event.key == pygame.K_DOWN or pygame.K_LSHIFT:
                if fish.isjump:
                    fish.isduck = True
                else:
                    fish.isdive = True
        # Keyboard key up input
        if event.type == pygame.KEYUP:
            # Undiving
            if event.key == pygame.K_DOWN or pygame.K_LSHIFT:
                fish.isdive = False
        # Mouse button down input
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Jumping
            if event.button == 1:
                fish.isjump = True
            # Ducking and diving
            if event.button == 3:
                if fish.isjump:
                    fish.isduck = True
                else:
                    fish.isdive = True
