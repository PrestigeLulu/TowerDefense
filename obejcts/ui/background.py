import pygame


class Background:
  def __init__(self, image_path, screen_width, screen_height):
    # 이미지 로드
    self.image = pygame.image.load(image_path)
    # 화면 크기에 맞게 이미지 크기 조정
    self.image = pygame.transform.scale(self.image, (screen_width, screen_height))
    # 이미지의 경계 사각형 가져오기
    self.rect = self.image.get_rect()
    # 이미지의 초기 위치 설정
    self.rect.topleft = (0, 0)

  def draw(self, surface):
    # 이미지 그리기
    surface.blit(self.image, self.rect)