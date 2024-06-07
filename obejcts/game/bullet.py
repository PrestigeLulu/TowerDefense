import math
import pygame

from image import BULLET_IMAGE
from state import ZOMBIES


class Bullet(pygame.sprite.Sprite):
  def __init__(self, bullet_type, zombie, x, y, size, speed, damage):
    super().__init__()
    self.image = BULLET_IMAGE[bullet_type]
    self.image = pygame.transform.scale(self.image, (size, size))
    self.x = x
    self.y = y
    self.zombie = zombie
    self.speed = speed
    self.damage = damage
    self.rect = self.image.get_rect()
    self.rect.center = (x, y)
  
  def update(self):
    self.rect.center = (self.x, self.y)
    zombies = ZOMBIES
    for zombie in zombies:
      if pygame.sprite.collide_rect(self, zombie):
        zombie.hp -= self.damage
        self.kill()
        return

    goal = (self.zombie.x, self.zombie.y)
    angle = self.get_angle(goal)
    radian = math.radians(angle)
    self.x += self.speed * math.cos(radian)
    self.y -= self.speed * math.sin(radian)

  def get_angle(self, goal):
    dx = goal[0] - self.x
    dy = goal[1] - self.y
    radian = math.atan2(-dy, dx)
    degree = math.degrees(radian)
    return degree