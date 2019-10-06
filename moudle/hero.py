#coding:utf-8
class Hero():
    def __init__(self,settings, screen):
        """初始化飞船并设置其初始位置"""
        self.screen = screen
        self.settings = settings
        #加载飞船图片
        self.init_image()
        #获取飞船图片和screen实例的rect属性
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()
        #初始化飞船位置
        self.center_ship()
        #加载飞船移动速度
        self.speed_factor = settings.ship_speed_factor
        #用小数值存储飞船坐标
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        #移动标志
        self.offset={'move_left':0, 'move_right':0,
                     'move_up':0, 'move_down':0}
    def init_image(self):
        """初始化飞船图片"""
        for img in self.settings.ship_images:
            img=img.convert_alpha()
        self.images = self.settings.ship_images
        self.image = self.images[0]
        for down_image in self.settings.ship_down_images:
            down_image = down_image.convert_alpha()
        self.down_images = self.settings.ship_down_images
        
    def draw(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image, self.rect)
        
        
    def center_ship(self):
        """将飞船放在屏幕底部中央"""
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        
    def update(self):
        """更新飞船的rect属性"""
        self.rect = self.image.get_rect()
        """根据移动标志调整飞船"""
        #更新表示敌飞船位置的小数值
        self.x = self.x + self.offset['move_right'] - self.offset['move_left']
        self.y = self.y + self.offset['move_down'] - self.offset['move_up']
        #根据移动标志调整图片
        for value in self.offset.values():
            if value != 0:
                self.image = self.images[1]
            else:
                self.image =self.images[0]
        '''限制飞船活动范围'''
        #更新screen实例的rect属性
        self.screen_rect = self.screen.get_rect()
        #判断是否到了活动界限
        if self.x < 0:
            self.x = 0
        elif self.x + self.rect.width > self.screen_rect.width:
            self.x = self.screen_rect.width - self.rect.width
        if self.y < 0:
            self.y = 0
        elif self.y + self.rect.height > self.screen_rect.height:
            self.y = self.screen_rect.height - self.rect.height
        #更新表示飞船位置的rect属性
        self.rect.x = self.x
        self.rect.y = self.y