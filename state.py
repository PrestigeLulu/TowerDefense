import pygame

from obejcts.game.castle import Castle


IS_START = False
IS_GAME_OVER = False
IS_OPEN_SHOP = False
IS_BUILD_MODE = False
CAN_BUILD = False
BUILD_TYPE = None

def set_start(data):
  global IS_START
  IS_START = data

def set_game_over(data):
  global IS_GAME_OVER
  IS_GAME_OVER = data

def set_open_shop(data):
  global IS_OPEN_SHOP
  IS_OPEN_SHOP = data

def set_build_mode(data):
  global IS_BUILD_MODE
  IS_BUILD_MODE = data

def set_can_build(data):
  global CAN_BUILD
  CAN_BUILD = data

def set_build_type(data):
  global BUILD_TYPE
  BUILD_TYPE = data

def get_start():
  return IS_START

def get_game_over():
  return IS_GAME_OVER

def get_open_shop():
  return IS_OPEN_SHOP

def get_build_mode():
  return IS_BUILD_MODE

def get_can_build():
  return CAN_BUILD

def get_build_type():
  return BUILD_TYPE

CASTLE = Castle(100, 45, 500)

ZOMBIES = pygame.sprite.Group()
CANNONS = pygame.sprite.Group()
BULLETS = pygame.sprite.Group()
SPRITES = pygame.sprite.Group()