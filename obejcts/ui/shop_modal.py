import pygame

from obejcts.ui.icon_button import IconButton
from util import WHITE


class ShopModal:
    def __init__(self, close_callback):
        self.close_callback = close_callback
        pass

    def draw(self, screen):
        rect = pygame.Rect(200, 100, 1000, 600)
        pygame.draw.rect(screen, WHITE, rect)
        topright = rect.topright
        IconButton(topright[0] - 25, topright[1] + 25, 50, 50, 70, 70, "./imgs/ui/close.png", WHITE, 0, self.close_callback).draw(screen)