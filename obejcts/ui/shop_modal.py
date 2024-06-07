import time
import pygame

from color import WHITE
from config import CANNON_COST
from image import CANNON_IMAGE, CLOSE_IMAGE
from obejcts.ui.icon_button import IconButton
from obejcts.ui.shop_item import ShopItem
from state import set_build_mode, set_build_type, set_can_build, set_open_shop

def build(item_type):
  set_open_shop(False)
  set_build_mode(True)
  set_build_type(item_type)
  time.sleep(0.1)
  set_can_build(True)

def close():
  set_open_shop(False)

class ShopModal:
  def __init__(self):
    pass

  def draw(self, screen):
    rect = pygame.Rect(200, 100, 1000, 600)
    pygame.draw.rect(screen, WHITE, rect)
    topright = rect.topright
    IconButton(topright[0] - 25, topright[1] + 25, 50, 50, 70, 70, CLOSE_IMAGE, WHITE, 0, close).draw(screen)
    data = [
      ('normal', 700 - 300, 150),
      ('sniper', 700 - 300, 400),
      ('rocket', 700 + 100, 150),
      ('ice', 700 + 100, 400)
    ]
    for item in data:
      ShopItem(item[1], item[2], CANNON_IMAGE[item[0]], CANNON_COST[item[0]], item[0], build).draw(screen)