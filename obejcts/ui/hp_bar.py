import pygame

from color import GRAY, RED


class HpBar:
  def __init__(self, x, y, width, height, max_hp, hp):
    self.x = x
    self.y = y
    self.width = width
    self.height = height
    self.hp = hp
    self.max_hp = max_hp

  def draw(self, screen):
    pygame.draw.rect(screen, GRAY, [self.x, self.y, self.width, self.height])
    pygame.draw.rect(screen, RED, [self.x, self.y, self.width * (self.hp / self.max_hp), self.height])