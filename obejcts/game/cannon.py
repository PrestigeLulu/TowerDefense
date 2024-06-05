import math
import pygame

from util import SNIPER_CANNON


class Cannon(pygame.sprite.Sprite):
  def __init__(self, image, x, y, zombies, distance=200):
    super().__init__()
    self.image = image
    self.image = pygame.transform.scale(self.image, (100, 100))
    if image == SNIPER_CANNON:
      self.image = pygame.transform.scale(self.image, (150, 150))
    self.orig_image = self.image
    self.x = x
    self.y = y
    self.zombies = zombies
    self.angle = 0
    self.rect = self.image.get_rect()
    self.rect.center = (x, y)
    self.distance = distance

  def rotate(self):
    self.image = pygame.transform.rotozoom(self.orig_image, self.angle - 90, 1)
    self.rect = self.image.get_rect(center=self.rect.center)

  def update(self):
    closest_zombie = None
    closest_dist = self.distance
    for zombie in self.zombies:
        dist = math.hypot(zombie.x - self.x, zombie.y - self.y)
        if dist < closest_dist:
          closest_dist = dist
          closest_zombie = zombie
    if closest_zombie:
      self.angle = self.get_angle((closest_zombie.x, closest_zombie.y))
      self.rotate()

  def get_angle(self, goal):
    dx = goal[0] - self.x
    dy = goal[1] - self.y
    radian = math.atan2(-dy, dx)
    degree = math.degrees(radian)
    return degree