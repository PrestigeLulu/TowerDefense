import time
import pygame


from color import BLACK, RED, WHITE
from config import BULLET_DAMAGE, BULLET_SPEED, CANNON_DISTANCE, CANNON_SPEED, GRID_SIZE, SCREEN_SIZE, TITLE
from image import CANNON_IMAGE, NEXT_IMAGE, SHOP_IMAGE
from obejcts.game.zombie import Zombie
from obejcts.game.cannon import Cannon
from obejcts.ui.background import Background
from obejcts.ui.icon_button import IconButton
from obejcts.ui.shop_modal import ShopModal
from obejcts.ui.text_button import TextButton
from obejcts.ui.money_info import MoneyInfo
from obejcts.ui.hp_bar import HpBar
from obejcts.ui.text import Text
from state import *


clock = pygame.time.Clock()

# 실행 전 초기화
pygame.init()
# 타이틀 설정
pygame.display.set_caption(TITLE)
# 화면 크기 설정
screen = pygame.display.set_mode(SCREEN_SIZE)

def init_game():
  SPRITES.add(CASTLE)
  set_start(True)
  set_game_over(False)


def lobby(screen):
  Text(
    700, 200,
    "Tower Defense" if not IS_GAME_OVER else "Game Over", 72,
    WHITE if not IS_GAME_OVER else RED
    ).draw(screen)
  TextButton(
    700, 450,
    150, 60,
    "START" if not IS_GAME_OVER else "RESTART", 36,
    BLACK, WHITE, init_game
    ).draw(screen)
  

def next_wave():
  CASTLE.wave += 1
  normal_zombie = Zombie('normal', 1350, 100)
  iron_zombie = Zombie('iron', 1350, 100)
  speed_zombie = Zombie('speed', 1350, 100)
  ZOMBIES.add(normal_zombie)
  ZOMBIES.add(iron_zombie)
  ZOMBIES.add(speed_zombie)


next_wave_button = IconButton(
  screen.get_width() - 80,
  screen.get_height() - 80,
  100,
  100,
  75,
  75,
  NEXT_IMAGE,
  WHITE,
  200,
  next_wave)

def draw_ui(screen):
  # 체력바
  HpBar(30, 30, 300, 40, CASTLE.max_hp, CASTLE.hp).draw(screen)
  # 돈 정보
  MoneyInfo(50, 50, screen.get_width() - 80, 30, CASTLE.money).draw(screen)
  # 현재 웨이브
  Text(700, 60, f"Wave: {CASTLE.wave}", 60, WHITE).draw(screen)
  if get_build_mode():
    return
  # 상점 버튼
  IconButton(80, screen.get_height() - 80, 100, 100, 75, 75, SHOP_IMAGE, WHITE, 0, open_shop).draw(screen)
  # 다음 웨이브 버튼
  next_wave_button.draw(screen)
  if next_wave_button.is_clicked():
    next_wave_button.click()


def open_shop():
  set_open_shop(True)


def game_over():
  set_start(False)
  set_game_over(True)
  set_open_shop(False)
  set_build_mode(False)
  set_can_build(False)
  set_build_type(None)
  Text(
    700, 200,
    "Game Over", 72,
    RED
    ).draw(screen)
  CASTLE.reset()
  SPRITES.empty()
  ZOMBIES.empty()
  CANNONS.empty()
  BULLETS.empty()

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
  Background(SCREEN_SIZE).draw(screen)
  
  # 모든 스프라이트 업데이트
  SPRITES.update()
  ZOMBIES.update()
  BULLETS.update()
  CANNONS.update()
  # 모든 스프라이트 그리기
  SPRITES.draw(screen)
  ZOMBIES.draw(screen)
  BULLETS.draw(screen)
  CANNONS.draw(screen)


  # 시작전 메인화면
  if not get_start():
    lobby(screen)
    continue

  draw_ui(screen)

  if get_build_mode():
    BUILD_TYPE = get_build_type()
    mouse_pos = pygame.mouse.get_pos()
    image = CANNON_IMAGE[BUILD_TYPE]
    image = pygame.transform.scale(image, (100, 100))
    if BUILD_TYPE == 'sniper':
      image = pygame.transform.scale(image, (150, 150))

    # 마우스 좌표를 가장 가까운 격자 좌표로 변환
    grid_x = (mouse_pos[0] // GRID_SIZE) * GRID_SIZE
    grid_y = (mouse_pos[1] // GRID_SIZE) * GRID_SIZE

    # 격자 좌표를 화면 좌표로 변환
    screen_x = grid_x + GRID_SIZE // 2
    screen_y = grid_y + GRID_SIZE // 2

    # 화면에 이미지 그리기
    if BUILD_TYPE == 'sniper':
      screen.blit(image, (screen_x - 75, screen_y - 75))
    else:
      screen.blit(image, (screen_x - 50, screen_y - 50))

    if not get_can_build():
      continue

    # 마우스 클릭시
    click = pygame.mouse.get_pressed()
    if click[0]:
      time.sleep(0.1)
      set_build_mode(False)
      set_can_build(False)
      Cannon(
        BUILD_TYPE,
        screen_x,
        screen_y
        ).add(CANNONS)
  
  if get_open_shop():
    ShopModal().draw(screen)

  if CASTLE.hp <= 0:
    game_over()