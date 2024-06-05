import pygame

from obejcts.ui.money_info import MoneyInfo
from util import WHITE


class ShopItem:
  def __init__(self, x, y, image, money, item_type, castle, action=None):
    self.x = x
    self.y = y
    self.width = 200
    self.height = 230
    self.money = money
    self.image = image
    self.image = pygame.transform.scale(self.image, (200, 170))

    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + self.width > mouse[0] > x and y + self.height > mouse[1] > y:
      if click[0] and castle.can_buy(money) and action is not None:
        castle.sub_money(money)
        action(item_type)
  
  def draw(self, screen):
    rect = pygame.Rect(self.x, self.y, self.width, self.height)
    pygame.draw.rect(screen, WHITE, rect)
    # 테두리
    pygame.draw.rect(screen, (0, 0, 0), rect, 3)
    # Draw item image
    screen.blit(self.image, (self.x, self.y))
    MoneyInfo(50, 50, self.x + 100, self.y + 170, self.money).draw(screen)
