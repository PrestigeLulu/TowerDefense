import pygame
import math


# 타워 클래스 정의
class Tower(pygame.sprite.Sprite):
  def __init__(self, x, y):
    super().__init__()

    self.image = pygame.Surface((50, 50))  # 타워 이미지 크기 설정
    self.image.fill((255, 0, 0))  # 타워 색상 설정
    self.rect = self.image.get_rect(center=(x, y))  # 타워 위치 설정

    self.level = 1  # 타워 레벨 초기화
    self.attack_range = 150  # 타워의 공격 범위 설정
    self.base_damage = 3  # 타워의 기본 공격력 설정
    self.damage_per_level = 2 * self.level**1.8  # 레벨 당 공격력 증가량

    self.update_attributes()  # 속성 업데이트

  def update(self):
    pass  # 타워의 상태 업데이트 (필요한 경우)

  def draw(self, screen):
    screen.blit(self.image, self.rect)  # 타워를 화면에 그림

  def update_attributes(self):
    # 레벨에 따라 속성 업데이트
    self.damage = self.base_damage + self.damage_per_level

  def attack(self, target):
    # 타워가 공격할 대상을 받아서 공격 실행
    distance = math.sqrt((self.rect.centerx - target.rect.centerx) ** 2 +
                         (self.rect.centery - target.rect.centery) ** 2)
    if distance <= self.attack_range:
      target.health -= self.damage  # 대상에게 데미지 입힘