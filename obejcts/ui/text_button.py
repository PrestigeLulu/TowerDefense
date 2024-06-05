import pygame


class TextButton:
  def __init__(self, x, y, width, height, text, text_size, text_color, button_color, action=None):
    x = x - width // 2
    y = y - height // 2
    self.rect = pygame.Rect(x, y, width, height)
    self.text = text
    self.font = pygame.font.Font(None, text_size)
    self.text_color = text_color
    self.button_color = button_color
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + width > mouse[0] > x and y + height > mouse[1] > y:
      if click[0] and action is not None:
        action()

  def draw(self, screen):
    pygame.draw.rect(screen, self.button_color, self.rect)
    text = self.font.render(self.text, True, self.text_color)
    text_rect = text.get_rect(center=self.rect.center)
    screen.blit(text, text_rect)