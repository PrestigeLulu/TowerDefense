import pygame

from obejcts.ui.icon_button import IconButton
from obejcts.ui.shop_item import ShopItem
from util import ICE_CANNON, NORMAL_CANNON, ROCEKT_CANNON, SNIPER_CANNON, WHITE


class ShopModal:
  def __init__(self, close_callback, castle, set_build_mode):
    self.close_callback = close_callback
    self.castle = castle
    self.set_build_mode = set_build_mode

  def draw(self, screen):
    rect = pygame.Rect(200, 100, 1000, 600)
    pygame.draw.rect(screen, WHITE, rect)
    topright = rect.topright
    IconButton(topright[0] - 25, topright[1] + 25, 50, 50, 70, 70, "./imgs/ui/close.png", WHITE, 0, self.close_callback).draw(screen)
    ShopItem(700 - 300, 150, NORMAL_CANNON, 1, 'normal', self.castle, self.set_build_mode).draw(screen)
    ShopItem(700 - 300, 400, SNIPER_CANNON, 1, 'sniper', self.castle, self.set_build_mode).draw(screen)
    ShopItem(700 + 100, 150, ROCEKT_CANNON, 1, 'rocket', self.castle, self.set_build_mode).draw(screen)
    ShopItem(700 + 100, 400, ICE_CANNON, 1, 'ice', self.castle, self.set_build_mode).draw(screen)