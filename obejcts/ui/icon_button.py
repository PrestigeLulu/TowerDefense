import pygame


class IconButton:
  def __init__(self, x, y, width, height, image_width, image_height, image, button_color, cooldown, action=None):
    x = x - width // 2
    y = y - height // 2
    self.rect = pygame.Rect(x, y, width, height)
    self.width = width
    self.height = height
    self.image = image
    self.image = pygame.transform.scale(self.image, (image_width, image_height))
    self.button_color = button_color
    self.last = pygame.time.get_ticks()
    self.cooldown = cooldown
    self.action = action
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if self.rect.collidepoint(mouse) and click[0] and action is not None:
      action()

  def draw(self, screen):
    pygame.draw.rect(screen, self.button_color, self.rect)
    pos = (self.rect.x + self.rect.width // 2 - self.image.get_width() // 2, self.rect.y + self.rect.height // 2 - self.image.get_height() // 2)
    screen.blit(self.image, pos)

  def is_clicked(self):
    x, y = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    return self.rect.collidepoint(x, y) and click[0] and pygame.time.get_ticks() - self.last >= self.cooldown
  
  def click(self):
    self.last = pygame.time.get_ticks()
    self.action()