import pygame

from color import WHITE
from obejcts.ui.money_info import MoneyInfo
from state import CASTLE


class ShopItem:
  def __init__(self, x, y, image, money, item_type, action=None):
    self.x = x
    self.y = y
    self.width = 200
    self.height = 230
    self.money = money
    self.image = image
    self.image = pygame.transform.scale(self.image, (200, 170))
    self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if self.rect.collidepoint(mouse) and click[0] and action is not None:
      if CASTLE.can_buy(money):
        CASTLE.sub_money(money)
        action(item_type)
  
  def draw(self, screen):
    pygame.draw.rect(screen, WHITE, self.rect)
    # 테두리
    pygame.draw.rect(screen, (0, 0, 0), self.rect, 3)
    # 아이템 이미지
    screen.blit(self.image, (self.x, self.y))
    # 돈 정보
    MoneyInfo(50, 50, self.x + 100, self.y + 170, self.money).draw(screen)
