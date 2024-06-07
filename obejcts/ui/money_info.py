import pygame

from color import ORANGE
from image import MONEY_IMAGE
from obejcts.ui.text import Text


class MoneyInfo:
  def __init__(self, width, height, x, y, money):
    self.image = MONEY_IMAGE
    self.image = pygame.transform.scale(self.image, (width, height))
    self.width = width
    self.height = height
    self.x = x
    self.y = y
    self.money = money

  def draw(self, surface):
    Text(
      self.x - 10, self.y + self.height // 2,
      f"{self.money}", 36,
      ORANGE,
      "midright"
      ).draw(surface)
    surface.blit(self.image, (self.x, self.y))
  
  def set_money(self, money):
    self.money = money