import pygame

from config import CASTLE_DEFAULT
from image import CASTLE_IMAGE


class Castle(pygame.sprite.Sprite):
  def __init__(self, size, x, y):
    super().__init__()
    self.hp = CASTLE_DEFAULT['hp']
    self.max_hp = self.hp
    self.money = CASTLE_DEFAULT['money']
    self.wave = 0
    self.image = CASTLE_IMAGE
    self.image = pygame.transform.scale(self.image, (size, size))
    self.x = x
    self.y = y
    self.rect = self.image.get_rect(topleft=(x, y))
    
  def draw(self, surface):
    surface.blit(self.image, (self.x, self.y))
    
  def set_hp(self, hp):
    self.hp = hp
    if self.hp < 0:
      self.hp = 0
    if self.hp > self.max_hp:
      self.hp = self.max_hp
  
  def add_hp(self, hp):
    self.hp += hp
    if self.hp < 0:
      self.hp = 0
    if self.hp > self.max_hp:
      self.hp = self.max_hp
  
  def sub_hp(self, hp):
    self.hp -= hp
    if self.hp < 0:
      self.hp = 0
    if self.hp > self.max_hp:
      self.hp = self.max_hp
  
  def set_money(self, money):
    self.money = money

  def add_money(self, money):
    self.money += money

  def sub_money(self, money):
    self.money -= money
    if self.money < 0:
      self.money = 0
  
  def can_buy(self, price):
    return self.money >= price
  
  def reset(self):
    self.hp = self.max_hp
    self.money = CASTLE_DEFAULT['money']
    self.wave = 0