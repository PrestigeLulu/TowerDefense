import pygame


from obejcts.game.zombie.zombie import Zombie
from obejcts.ui.background import Background
from obejcts.ui.icon_button import IconButton
from obejcts.ui.shop_modal import ShopModal
from obejcts.ui.text_button import TextButton
from obejcts.ui.money_info import MoneyInfo
from obejcts.ui.hp_bar import HpBar
from obejcts.ui.text import Text
from obejcts.game.castle import Castle
from util import BLACK, RED, WHITE


size = [1400, 800]

clock = pygame.time.Clock()

# 실행 전 초기화
pygame.init()
# 타이틀 설정
pygame.display.set_caption("Tower Defense")
# 화면 크기 설정
screen = pygame.display.set_mode(size)

sprites = pygame.sprite.Group()
is_start = False
is_game_over = False
is_open_shop = False


def init_game():
  global is_start, is_game_over
  sprites.add(castle)
  is_start = True
  is_game_over = False


def intro_ui(screen):
  Text(
    700, 200,
    "Tower Defense" if not is_game_over else "Game Over", 72,
    WHITE if not is_game_over else RED
    ).draw(screen)
  TextButton(
    700, 450,
    150, 60,
    "START" if not is_game_over else "RESTART", 36,
    BLACK, WHITE, init_game
    ).draw(screen)
  

def next_wave():
  castle.wave += 1
  normal_zombie = Zombie("./imgs/game/zombie.png", 1350, 100, castle)
  iron_zombie = Zombie("./imgs/game/iron_zombie.png", 1350, 100, castle, 200, 4)
  speed_zombie = Zombie("./imgs/game/speed_zombie.png", 1350, 100, castle, 50, 6)
  sprites.add(normal_zombie)
  sprites.add(iron_zombie)
  sprites.add(speed_zombie)


next_wave_button = IconButton(
  screen.get_width() - 80,
  screen.get_height() - 80,
  100,
  100,
  75,
  75,
  "./imgs/ui/next.png",
  WHITE,
  200,
  next_wave)

def draw_ui(screen):
  # 체력바
  HpBar(30, 30, 300, 40, castle.max_hp, castle.hp).draw(screen)
  # 돈 정보
  MoneyInfo("./imgs/ui/money.png", 50, 50, screen.get_width() - 80, 30, castle.money).draw(screen)
  # 현재 웨이브
  Text(700, 60, f"Wave: {castle.wave}", 60, WHITE).draw(screen)
  # 상점 버튼
  IconButton(80, screen.get_height() - 80, 100, 100, 75, 75, "./imgs/ui/shop.png", WHITE, 0, open_shop).draw(screen)
  # 다음 웨이브 버튼
  next_wave_button.draw(screen)
  if next_wave_button.is_clicked():
    next_wave_button.click()


def open_shop():
  global is_open_shop
  is_open_shop = True


def game_over():
  global is_start, is_game_over, is_open_shop
  is_start = False
  is_game_over = True
  is_open_shop = False
  Text(
    700, 200,
    "Game Over", 72,
    RED
    ).draw(screen)
  castle.reset()
  sprites.empty()


def close_shop():
  global is_open_shop
  is_open_shop = False


def show_shop(screen):
  ShopModal(close_shop).draw(screen)


background = Background("./imgs/ui/background.png", 1400, 800)
castle = Castle("./imgs/game/castle.png", 105, 100, 45, 500)

while True:
  df = clock.tick(60)
  for event in pygame.event.get():
    # 게임 종료
    if event.type == pygame.QUIT:
      pygame.quit()
  
  # 다음 프레임으로
  pygame.display.flip()
  # 60 프레임 고정
  clock.tick(60)

  # 배경 그리기
  background.draw(screen)
  
  # 모든 스프라이트 업데이트
  sprites.update()
  # 모든 스프라이트들 그리기
  sprites.draw(screen)

  # 시작전 메인화면
  if not is_start:
    intro_ui(screen)
    continue

  draw_ui(screen)

  if is_open_shop:
    show_shop(screen)

  if castle.hp <= 0:
    game_over()