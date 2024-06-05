import pygame


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
GRAY = (128, 128, 128)
YELLOW = (255, 255, 0)
ORANGE = (255, 165, 0)

GRID_SIZE = 50

NORMAL_CANNON_DISTANCE = 200
SNIPER_CANNON_DISTANCE = 700
ROCKET_CANNON_DISTANCE = 300
ICE_CANNON_DISTANCE = 400

NORMAL_CANNON_COST = 100
SNIPER_CANNON_COST = 200
ROCKET_CANNON_COST = 300
ICE_CANNON_COST = 400

NORMAL_CANNON = pygame.image.load('imgs/game/normal_cannon.png')
SNIPER_CANNON = pygame.image.load('imgs/game/sniper_cannon.png')
ROCEKT_CANNON = pygame.image.load('imgs/game/rocket_cannon.png')
ICE_CANNON = pygame.image.load('imgs/game/ice_cannon.png')
MONEY = pygame.image.load('imgs/ui/money.png')