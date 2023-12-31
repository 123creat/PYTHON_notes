class Settings():
	#存储《外星人入侵》的所有设置的类
	
	def __init__(self):
		self.screen_width = 1200
		self.screen_height = 800
		self.bg_color = (221,160,221)
		
		self.bullet_speed_factor = 1
		self.bullet_width = 10
		self.bullet_height = 10
		self.bullet_color = 60,60,60
		self.bullets_allowed = 3
		#外星人设置
		self.fleet_drop_speed =5		
		#初始化岁游戏进行而变化的设置
		self.speedup_scale = 1.2
		#外星人点数的提高速度
		self.score_scale = 1.5
		self.initialize_dynamic_settings()
		
	def initialize_dynamic_settings(self):
		#飞船的设置
		self.ship_speed_factor = 0.8
		#飞船的生命值
		self.ship_limit = 3
		#外星人的设置
		self.alien_speed_factor = 1
		
		#fleet_direction为1表示向右移动，为-1表示向左移动
		self.fleet_direction =1
		#记分
		self.alien_points  = 50
		
	def increase_speed(self):
		self.ship_speed_factor *= self.speedup_scale
		self.bullet_speed_factor *= self.speedup_scale
		self.alien_speed_factor *= self.speedup_scale
		
		self.alien_points = int(self.alien_points * self.score_scale)
		print(self.alien_points)
		

