import pygame

from obejcts.background import Background
from obejcts.ui.button import Button
from obejcts.ui.text import Text
from obejcts.castle import Castle

size = [1400, 800]
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

clock = pygame.time.Clock()

# 실행 전 초기화
pygame.init()
# 타이틀 설정
pygame.display.set_caption("Tower Defense")
# 화면 크기 설정
screen = pygame.display.set_mode(size)

background = Background("./imgs/background.png", 1400, 800)
castle = Castle("./imgs/castle.png", 105, 100, 100, 45, 500)

sprites = pygame.sprite.Group()
sprites.add(background)

is_start = False

def init_game():
  global is_start
  sprites.add(castle)
  is_start = True  

while True:
  df = clock.tick(60)
  for event in pygame.event.get():
    # 게임 종료
    if event.type == pygame.QUIT:
      pygame.quit()
  
  # 모든 스프라이트 업데이트
  sprites.update()
  # 모든 스프라이트들 그리기
  sprites.draw(screen)

  # 시작전 메인화면
  if not is_start:
    Text(
      700, 200,
      "Tower Defense", 72,
      WHITE
      ).draw(screen)
    Button(
      700, 450,
      150, 60,
      "START", 36,
      BLACK, WHITE, init_game
      ).draw(screen)

  # 다음 프레임으로
  pygame.display.flip()
  # 60 프레임 고정
  clock.tick(60)