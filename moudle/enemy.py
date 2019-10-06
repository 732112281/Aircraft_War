#coding:utf-8
from pygame.sprite import Sprite
class Enemy(Sprite):
    """表示单个敌人的类"""
    def __init__(self, settings, screen, randint, type):
        """初始化敌飞船并设置其初始位置"""
        #调用父类的初始化方法
        super().__init__()
        '''初始化设置'''
        self.screen = screen
        self.settings = settings
        self.type = type
        #初始化敌飞船设置
        self.init(randint)
        #设置敌飞船被击中图片更改时间和爆炸时间初始值
        self.hit_ticks = self.bomb_ticks = 0
        #设置被击中索引
        self.been_hit = False
        #获取敌飞船图片和screen对象的rect属性
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()
        #每个敌飞船最初的坐标
        if self.screen_rect.width > self.rect.width:
            self.rect.x = randint(0, self.screen_rect.width - self.rect.width)
        else:
            self.rect.x = 0
        self.rect.y -= self.rect.height
        #用小数值存储敌飞船坐标
        self.y = float(self.rect.y)
        
    def init(self,randint):
        """初始化敌飞船各项属性"""
        if self.type == 1:
            #敌飞船1速度
            self.speed_factor = self.settings.enemy_speed_factor1
            #敌飞船1生命
            self.life = self.settings.enemy1_life
            #敌飞船1分数
            self.score = self.settings.enemy1_score
            #敌飞船1图片
            for img in self.settings.enemy1_images:
                img = img.convert_alpha()
            self.images = self.settings.enemy1_images
            self.image = self.images[0]
            #敌飞船1爆炸图片
            self.down_images = self.settings.enemy1_down_images
            for down_image in self.down_images:
                down_image = down_image.convert_alpha()
            self.bomb_time = self.settings.enemy1_bomb_everyticktime
        elif self.type == 2:
            #敌飞船2速度
            self.speed_factor = self.settings.enemy_speed_factor2
            #敌飞船2生命
            self.life = self.settings.enemy2_life
            #敌飞船2分数
            self.score = self.settings.enemy2_score
            #敌飞船2图片
            for img in self.settings.enemy2_images:
                img = img.convert_alpha()
            self.images = self.settings.enemy2_images
            self.image = self.images[0]
            #敌飞船2被击中图片更改持续时间
            self.hit_change_time = self.settings.enemy2_beenhit_everyticktime
            #敌飞船2爆炸图片
            self.down_images = self.settings.enemy2_down_images
            for down_image in self.down_images:
                down_image = down_image.convert_alpha()
            self.bomb_time = self.settings.enemy2_bomb_everyticktime
        elif self.type == 3:
            #敌飞船3速度
            self.speed_factor = self.settings.enemy_speed_factor1
            #敌飞船3生命
            self.life = self.settings.enemy3_life
            #敌飞船3分数
            self.score = self.settings.enemy3_score
            #敌飞船3图片
            for img in self.settings.enemy3_images:
                img = img.convert_alpha()
            self.images = self.settings.enemy3_images
            self.image = self.images[0]
            #敌飞船3被击中图片更改持续时间
            self.hit_change_time = self.settings.enemy3_beenhit_everyticktime
            #敌飞船3爆炸图片
            self.down_images = self.settings.enemy3_down_images
            for down_image in self.down_images:
                down_image = down_image.convert_alpha()
            self.bomb_time = self.settings.enemy3_bomb_everyticktime
        #设置敌飞船移动动画每帧持续时间
        if len(self.images) > 2:
            self.enemy_move_everyticktime = \
            self.settings.enemy_move_everyticktime
            #设置敌飞船移动动画时间初始值
            self.move_tick = 0
    
    def update(self):
        """调用各个update方法"""
        self.hit_update()
        """向下移动敌飞船"""
        #更新screen实例的rect属性
        self.screen_rect = self.screen.get_rect()
        #更新表示敌飞船位置的小数值
        self.y += self.speed_factor
        #更新表示敌飞船位置的rect属性
        self.rect.y = self.y
        #删除消失的敌飞船
        if self.rect.top > self.screen_rect.height or \
            self.rect.x > self.screen_rect.width:
            self.kill()
    
    def hit_update(self):
        """被击中动画"""
        if self.been_hit:
            self.hit_ticks += 1
            if self.hit_ticks < self.hit_change_time:
                self.image = self.images[-1]
            elif self.hit_ticks == self.hit_change_time:
                self.image = self.images[0]
                self.been_hit =False
                self.hit_ticks = 0
            
    def bomb_update(self):
        """爆炸动画"""
        self.bomb_ticks += 1
        if self.bomb_ticks % self.bomb_time == 0:
            try:
                self.image = self.down_images[self.bomb_ticks
                                               // self.bomb_time - 1]
            except IndexError:
                self.kill()
    
    def enemy3_image_update(self):
        if len(self.images) > 2:
            if not self.been_hit:
                self.move_tick += 1
                if self.move_tick == self.enemy_move_everyticktime:
                    self.image = self.images[0]
                    self.move_tick = 0
                elif self.move_tick == self.enemy_move_everyticktime // 2:
                    self.image = self.images[1]