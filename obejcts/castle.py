import pygame

# TODO : 체력바 보이게 하기
class Castle(pygame.sprite.Sprite):
    def __init__(self, image_path, width, height, hp, x, y):
        super().__init__()
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (width, height))
        self.hp = hp
        self.x = x
        self.y = y
        self.rect = self.image.get_rect(topleft=(x, y))
    
    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))
    
    def take_damage(self, damage):
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0

   # 체력바 그리기        
    def draw_health_bar(self, surface):
        bar_length = 100
        bar_height = 10
        fill = (self.hp / self.max_hp) * bar_length
        pygame.draw.rect(surface, WHITE, (self.x, self.y - 20, bar_length, bar_height))
        pygame.draw.rect(surface, (255, 0, 0), (self.x, self.y - 20, bar_length - fill, bar_height))

        #이것만 하면 되니
        #화면 업데이트 이런것도 표시해놔야 하나
        #체력 5%씩 깎이는건??