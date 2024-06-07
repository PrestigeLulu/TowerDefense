import math
import pygame

from obejcts.game.bullet import Bullet
from util import BULLETS, SNIPER_CANNON, ZOMBIES


class Cannon(pygame.sprite.Sprite):
  def __init__(self, image, x, y, distance, speed, bullet_speed,damage):
    super().__init__()
    self.image = image
    self.image = pygame.transform.scale(self.image, (100, 100))
    if image == SNIPER_CANNON:
      self.image = pygame.transform.scale(self.image, (150, 150))
    self.orig_image = self.image
    self.x = x
    self.y = y
    self.zombies = ZOMBIES
    self.angle = 0
    self.rect = self.image.get_rect()
    self.rect.center = (x, y)
    self.distance = distance
    self.tick = 0
    self.speed = speed
    self.damage = damage
    self.bullet_speed = bullet_speed

  def rotate(self):
    self.image = pygame.transform.rotozoom(self.orig_image, self.angle - 90, 1)
    self.rect = self.image.get_rect(center=self.rect.center)

  def update(self):
    self.tick += 1
    self.zombies = ZOMBIES
    closest_zombie = None
    closest_dist = self.distance
    for zombie in self.zombies:
        dist = math.hypot(zombie.x - self.x, zombie.y - self.y)
        if dist < closest_dist:
          closest_dist = dist
          closest_zombie = zombie
    if not closest_zombie:
      return
    self.angle = self.get_angle((closest_zombie.x, closest_zombie.y))
    self.rotate()
    if self.tick % self.speed == 0:
      self.shoot(closest_zombie)
      
  def get_angle(self, goal):
    dx = goal[0] - self.x
    dy = goal[1] - self.y
    radian = math.atan2(-dy, dx)
    degree = math.degrees(radian)
    return degree
  
  def shoot(self, zombie):
    pos = self.rect.center
    x = pos[0]
    y = pos[1]
    bullet = Bullet(zombie, x, y, 20, self.bullet_speed, self.damage)
    BULLETS.add(bullet)