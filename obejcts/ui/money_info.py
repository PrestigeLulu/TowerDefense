import pygame


from obejcts.ui.text import Text
from util import YELLOW


class MoneyInfo:
  def __init__(self, image_path, width, height, x, y, money):
    self.image = pygame.image.load(image_path)
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
      YELLOW,
      "midright"
      ).draw(surface)
    surface.blit(self.image, (self.x, self.y))
  
  def set_money(self, money):
    self.money = money