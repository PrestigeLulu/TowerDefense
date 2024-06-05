import time
import pygame


from obejcts.game.zombie import Zombie
from obejcts.game.cannon import Cannon
from obejcts.ui.background import Background
from obejcts.ui.icon_button import IconButton
from obejcts.ui.shop_modal import ShopModal
from obejcts.ui.text_button import TextButton
from obejcts.ui.money_info import MoneyInfo
from obejcts.ui.hp_bar import HpBar
from obejcts.ui.text import Text
from obejcts.game.castle import Castle
from util import BLACK, GRID_SIZE, ICE_CANNON, MONEY, NORMAL_CANNON, RED, ROCEKT_CANNON, SNIPER_CANNON, WHITE


size = [1400, 800]

clock = pygame.time.Clock()

# 실행 전 초기화
pygame.init()
# 타이틀 설정
pygame.display.set_caption("Tower Defense")
# 화면 크기 설정
screen = pygame.display.set_mode(size)

zombies = pygame.sprite.Group()
cannons = pygame.sprite.Group()
sprites = pygame.sprite.Group()
is_start = False
is_game_over = False
is_open_shop = False
is_build_mode = False
build = None

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
  zombies.add(normal_zombie)
  zombies.add(iron_zombie)
  zombies.add(speed_zombie)


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
  MoneyInfo(50, 50, screen.get_width() - 80, 30, castle.money).draw(screen)
  # 현재 웨이브
  Text(700, 60, f"Wave: {castle.wave}", 60, WHITE).draw(screen)
  if(is_build_mode):
    return
  # 상점 버튼
  IconButton(80, screen.get_height() - 80, 100, 100, 75, 75, "./imgs/ui/shop.png", WHITE, 0, open_shop).draw(screen)
  # 다음 웨이브 버튼
  next_wave_button.draw(screen)
  if next_wave_button.is_clicked():
    next_wave_button.click()


def open_shop():
  global is_open_shop
  is_open_shop = True

def set_build_mode(item_type):
  global is_build_mode, build, can_build, is_open_shop
  is_build_mode = True
  is_open_shop = False
  build = item_type
  time.sleep(0.1)
  can_build = True


def game_over():
  global is_start, is_game_over, is_open_shop, is_build_mode, build
  is_start = False
  is_game_over = True
  is_open_shop = False
  is_build_mode = False
  build = None
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
  ShopModal(close_shop, castle, set_build_mode).draw(screen)


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
  zombies.update()
  cannons.update()
  # 모든 스프라이트 그리기
  sprites.draw(screen)
  zombies.draw(screen)
  cannons.draw(screen)


  # 시작전 메인화면
  if not is_start:
    intro_ui(screen)
    continue

  draw_ui(screen)

  if is_build_mode:
    mouse_pos = pygame.mouse.get_pos()
    image = None
    if build == 'normal':
      image = NORMAL_CANNON
    elif build == 'sniper':
      image = SNIPER_CANNON
    elif build == 'rocket':
      image = ROCEKT_CANNON
    elif build == 'ice':
      image = ICE_CANNON
    image = pygame.transform.scale(image, (100, 100))
    if build == 'sniper':
      image = pygame.transform.scale(image, (150, 150))

    # 마우스 좌표를 가장 가까운 격자 좌표로 변환
    grid_x = (mouse_pos[0] // GRID_SIZE) * GRID_SIZE
    grid_y = (mouse_pos[1] // GRID_SIZE) * GRID_SIZE

    # 격자 좌표를 화면 좌표로 변환
    screen_x = grid_x + GRID_SIZE // 2
    screen_y = grid_y + GRID_SIZE // 2

    # 화면에 이미지 그리기
    if build == 'sniper':
      screen.blit(image, (screen_x - 75, screen_y - 75))
    else:
      screen.blit(image, (screen_x - 50, screen_y - 50))

    # 마우스 클릭시
    if not can_build:
      continue
    click = pygame.mouse.get_pressed()
    if click[0]:
      time.sleep(0.1)
      is_build_mode = False
      can_build = False
      if build == 'normal':
        cannons.add(Cannon(NORMAL_CANNON, screen_x, screen_y, zombies))
      elif build == 'sniper':
        sprites.add(Cannon(SNIPER_CANNON, screen_x, screen_y, zombies))
      elif build == 'rocket':
        sprites.add(Cannon(ROCEKT_CANNON, screen_x, screen_y, zombies))
      elif build == 'ice':
        sprites.add(Cannon(ICE_CANNON, screen_x, screen_y, zombies))

  if is_open_shop and not is_build_mode:
    show_shop(screen)

  if castle.hp <= 0:
    game_over()