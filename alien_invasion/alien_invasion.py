import pygame 
from settings import Settings
from Dog import Ship
import game_functions as gf
from pygame.sprite import Group
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard



def run_game():
	#初始化背景设置
	pygame.init()
	
	#将设置类进行实例化
	ai_settings = Settings()
	
	#设置窗口
	screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
	pygame.display.set_caption("Dog and Mouses")
	
	
	#创建存储游戏统计信息的实例，并创建记分牌
	#创建一个用于存储游戏统计信息的实例
	stats = GameStats(ai_settings)

	# 记分牌
	sb = Scoreboard(ai_settings,screen,stats)
	
	#创建飞船
	ship = Ship(ai_settings,screen)

	#创建一个用于存储子弹的编组
	bullets = Group()

	#创建外星人编组
	aliens = Group()

	#创建外星人群
	gf.create_fleet(ai_settings,screen,ship,aliens)
	
	#创建按钮
	play_button = Button(ai_settings,screen,"Welcome The Game")
	
	# while 循环来控制游戏
	while True:
		gf.check_events(ai_settings,screen,stats,sb,play_button,ship,aliens,bullets)
		if stats.game_active:
			ship.update()
			gf.update_bullets(ai_settings,screen,stats,sb,ship,aliens,bullets)
			gf.update_aliens(ai_settings,screen,stats,sb,ship,aliens,bullets)
		
		bullets.update()
		gf.update_screen(ai_settings,screen,stats,sb,ship,aliens,bullets,play_button)
		
run_game()

