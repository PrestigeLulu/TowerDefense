import pygame


class Text:
    def __init__(self, x, y, text, text_size, text_color):
        self.text = text
        self.font = pygame.font.Font(None, text_size)
        self.text_color = text_color
        self.x = x
        self.y = y

    def draw(self, screen):
        text = self.font.render(self.text, True, self.text_color)
        text_rect = text.get_rect(center=(self.x, self.y))
        screen.blit(text, text_rect)