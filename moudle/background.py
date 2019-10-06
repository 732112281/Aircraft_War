#coding:utf-8
class Background():
    def __init__(self, settings, screen):
        """初始化飞船并设置其位置"""
        self.screen = screen
        self.settings = settings
        #加载背景图像并获取其外接矩形
        self.image = settings.background_image.convert()
        
        self.rect = self.image.get_rect()
        #用小数表示两张背景图纵坐标
        self.y1 = 0
        self.y2 =- self.rect.height
        #加载背景移动速度
        self.speed_factor = self.settings.background_speed_factor
    def draw(self):
        """在指定位置绘制背景"""
        self.screen_rect = self.screen.get_rect()
        if self.screen_rect.width % self.rect.width != 0:
            self.number = self.screen_rect.width // self.rect.width + 1
        else:
            self.number = self.screen_rect.width // self.rect.width
        for x in range(self.number):
            self.x = x * self.rect.width
            self.screen.blit(self.image, (self.x, self.y1))
            self.screen.blit(self.image, (self.x, self.y2))
    def update(self):
        """让背景开始移动"""
        self.y1 += self.speed_factor
        self.y2 += self.speed_factor
        #当图片顶端超出窗口底部，重置横坐标
        if self.y1 > self.rect.height:
            self.y1 =- self.rect.height
        if self.y2 > self.rect.height:
            self.y2 =- self.rect.height
        