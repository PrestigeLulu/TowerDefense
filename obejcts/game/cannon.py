import math
import pygame

from config import BULLET_DAMAGE, BULLET_SPEED, CANNON_DISTANCE, CANNON_SPEED
from image import CANNON_IMAGE
from obejcts.game.bullet import Bullet
from state import BULLETS, ZOMBIES


class Cannon(pygame.sprite.Sprite):
  def __init__(self, cannon_type, x, y):
    super().__init__()
    self.type = cannon_type
    self.image = CANNON_IMAGE[cannon_type]
    self.image = pygame.transform.scale(self.image, (100, 100))
    if cannon_type == 'sniper':
      self.image = pygame.transform.scale(self.image, (150, 150))
    self.orig_image = self.image
    self.x = x
    self.y = y
    self.angle = 0
    self.rect = self.image.get_rect()
    self.rect.center = (x, y)
    self.distance = CANNON_DISTANCE[cannon_type]
    self.tick = 0
    self.speed = CANNON_SPEED[cannon_type]
    self.damage = BULLET_DAMAGE[cannon_type]
    self.bullet_speed = BULLET_SPEED[cannon_type]

  def rotate(self):
    self.image = pygame.transform.rotozoom(self.orig_image, self.angle - 90, 1)
    self.rect = self.image.get_rect(center=self.rect.center)

  def update(self):
    self.tick += 1
    closest_zombie = None
    closest_dist = self.distance
    for zombie in ZOMBIES:
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
    bullet = Bullet(self.type, zombie, pos[0], pos[1], 20, self.bullet_speed, self.damage)
    BULLETS.add(bullet)