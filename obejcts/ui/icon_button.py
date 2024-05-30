import pygame


class IconButton:
  def __init__(self, x, y, width, height, image_width, image_height, image_path, button_color, action=None):
    x = x - width // 2
    y = y - height // 2
    self.rect = pygame.Rect(x, y, width, height)
    self.width = width
    self.height = height
    self.image = pygame.image.load(image_path)
    self.image = pygame.transform.scale(self.image, (image_width, image_height))
    self.button_color = button_color
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + width > mouse[0] > x and y + height > mouse[1] > y:
      if click[0] and action is not None:
        action()

  def draw(self, screen):
    pygame.draw.rect(screen, self.button_color, self.rect)
    pos = (self.rect.x + self.rect.width // 2 - self.image.get_width() // 2, self.rect.y + self.rect.height // 2 - self.image.get_height() // 2)
    screen.blit(self.image, pos)