import pygame

CANNON_IMAGE = {
  'normal': pygame.image.load('imgs/game/normal_cannon.png'),
  'sniper': pygame.image.load('imgs/game/sniper_cannon.png'),
  'rocket': pygame.image.load('imgs/game/rocket_cannon.png'),
  'ice': pygame.image.load('imgs/game/ice_cannon.png')
}

ZOMBIE_IMAGE = {
  'normal': pygame.image.load('imgs/game/normal_zombie.png'),
  'iron': pygame.image.load('imgs/game/iron_zombie.png'),
  'speed': pygame.image.load('imgs/game/speed_zombie.png')
}

BULLET_IMAGE = {
  'normal': pygame.image.load('imgs/game/bullet.png'),
  'sniper': pygame.image.load('imgs/game/bullet.png'),
  'rocket': pygame.image.load('imgs/game/rocket_bullet.png'),
  'ice': pygame.image.load('imgs/game/ice_bullet.png')
}

BACKGROUND_IMAGE = pygame.image.load('imgs/ui/background.png')

MONEY_IMAGE = pygame.image.load('imgs/ui/money.png')
CASTLE_IMAGE = pygame.image.load('imgs/game/castle.png')
SHOP_IMAGE = pygame.image.load('imgs/ui/shop.png')
NEXT_IMAGE = pygame.image.load('imgs/ui/next.png')
CLOSE_IMAGE = pygame.image.load('imgs/ui/close.png')