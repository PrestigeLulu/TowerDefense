import math
import pygame

from obejcts.ui.hp_bar import HpBar


class Zombie(pygame.sprite.Sprite):
  def __init__(self, image_path, x, y, castle, hp = 100, speed = 5, attack = 10):
    super().__init__()
    self.image_path = image_path
    self.image = pygame.image.load(image_path)
    self.image = pygame.transform.scale(self.image, (100, 100))
    self.orig_image = self.image
    self.x = x
    self.y = y
    self.hp = hp
    self.max_hp = hp
    self.castle = castle
    self.attack = attack
    self.angle = 0
    self.rect = self.image.get_rect()
    self.rect.center = (x, y)
    self.speed = speed
    self.goals = [
      (580, 100),
      (480, 150),
      (480, 250),
      (810, 360),
      (900, 440),
      (900, 560),
      (800, 610),
      (270, 610),
      (140, 550)
    ]

  def rotate(self):
    self.image = pygame.transform.rotozoom(self.orig_image, self.angle, 1)
    self.rect = self.image.get_rect(center=self.rect.center)

  def update(self):
    if len(self.goals) == 0:
      self.castle.sub_hp(self.attack)
      self.kill()
      return
    goal = self.goals[0]
    
    self.angle = self.get_angle(goal)
    self.rotate()
    self.rect.center = (self.x, self.y)

    if self.x < goal[0]:
      self.x += self.speed
    elif self.x > goal[0]:
      self.x -= self.speed
    if self.y < goal[1]:
      self.y += self.speed
    elif self.y > goal[1]:
      self.y -= self.speed
    if goal[0] - 3 < self.x < goal[0] + 3 and goal[1] - 3 < self.y < goal[1] + 3:
      self.goals.pop(0)
    
    HpBar(self.x - 35, self.y - 60, 70, 15, self.max_hp, self.hp).draw(pygame.display.get_surface())

  def get_angle(self, goal):
    dx = goal[0] - self.x
    dy = goal[1] - self.y
    radian = math.atan2(-dy, dx)
    degree = math.degrees(radian)
    return degree