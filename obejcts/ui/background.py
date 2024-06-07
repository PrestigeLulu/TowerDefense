import pygame

from image import BACKGROUND_IMAGE


class Background:
  def __init__(self, size):
    self.image = BACKGROUND_IMAGE
    self.image = pygame.transform.scale(self.image, size)
    self.rect = self.image.get_rect()
    self.rect.topleft = (0, 0)

  def draw(self, surface):
    surface.blit(self.image, self.rect)