import math
import pygame

from config import ZOMBIE_ATTACK, ZOMBIE_GOALS, ZOMBIE_HP, ZOMBIE_SPEED
from image import ZOMBIE_IMAGE
from obejcts.ui.hp_bar import HpBar
from state import CASTLE


class Zombie(pygame.sprite.Sprite):
  def __init__(self, zombie_type, x, y):
    super().__init__()
    self.image = ZOMBIE_IMAGE[zombie_type]
    self.image = pygame.transform.scale(self.image, (100, 100))
    self.orig_image = self.image
    self.x = x
    self.y = y
    self.hp = ZOMBIE_HP[zombie_type]
    self.max_hp = self.hp
    self.attack = ZOMBIE_ATTACK[zombie_type]
    self.speed = ZOMBIE_SPEED[zombie_type]
    self.goals = ZOMBIE_GOALS.copy()
    self.rect = self.image.get_rect()
    self.rect.center = (x, y)
    self.angle = 0

  def rotate(self):
    self.image = pygame.transform.rotozoom(self.orig_image, self.angle, 1)
    self.rect = self.image.get_rect(center=self.rect.center)

  def update(self):
    if self.hp <= 0:
      self.kill()
      return

    if len(self.goals) == 0:
      CASTLE.sub_hp(self.attack)
      self.kill()
      return
    goal = self.goals[0]
    
    self.angle = self.get_angle(goal)
    self.rotate()
    self.rect.center = (self.x, self.y)

    radian = math.radians(self.angle)
    self.x += self.speed * math.cos(radian)
    self.y -= self.speed * math.sin(radian)

    if goal[0] - self.speed <= self.x <= goal[0] + self.speed and goal[1] - self.speed <= self.y <= goal[1] + self.speed:
      self.goals.pop(0)
    
    HpBar(self.x - 35, self.y - 60, 70, 15, self.max_hp, self.hp).draw(pygame.display.get_surface())

  def get_angle(self, goal):
    dx = goal[0] - self.x
    dy = goal[1] - self.y
    radian = math.atan2(-dy, dx)
    degree = math.degrees(radian)
    return degree