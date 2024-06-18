import pygame

def init():
    pygame.init()

def getKey(key):
    # Check for key press
    keys = pygame.key.get_pressed()
    if key == "LEFT":
        return keys[pygame.K_LEFT]
    elif key == "RIGHT":
        return keys[pygame.K_RIGHT]
    elif key == "UP":
        return keys[pygame.K_UP]
    elif key == "DOWN":
        return keys[pygame.K_DOWN]
    elif key == "w":
        return keys[pygame.K_w]
    elif key == "s":
        return keys[pygame.K_s]
    elif key == "a":
        return keys[pygame.K_a]
    elif key == "d":
        return keys[pygame.K_d]
    elif key == "q":
        return keys[pygame.K_q]
    elif key == "e":
        return keys[pygame.K_e]
    elif key == "z":
        return keys[pygame.K_z]
    else:
        return False