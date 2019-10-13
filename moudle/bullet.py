#coding:utf-8
from pygame.sprite import Sprite
class Bullet(Sprite):
    """一个对飞船发射的子弹进行管理的类"""
    def __init__(self, settings, game_starts, screen, hero, difference, new_bullet_centerx):
        """在飞船所处的位置创建一个子弹对象"""
        #调用父类的初始化方法
        super().__init__()
        '''初始化设置'''
        self.screen = screen
        self.settings = settings
        self.game_starts = game_starts
        #初始化子弹设置
        self.init(game_starts, hero ,difference, new_bullet_centerx)
        #加载子弹移动速度
        self.speed_factor = game_starts.bullet_speed_factor
        #用小数值存储子弹坐标
        self.rect.centerx = self.centerx
        self.y = float(self.rect.y)
        
    def init(self, game_starts, hero ,difference, new_bullet_centerx):
        """初始化子弹各属性"""
        #加载图片
        if game_starts.bullet_line == 1:
            self.image = self.settings.bullet_images[0].convert_alpha()
        else:
            self.image = self.settings.bullet_images[1].convert_alpha()
        #获取子弹图片的rect属性
        self.rect = self.image.get_rect()
        self.centerx = float(hero.x + difference + new_bullet_centerx)
        self.rect.top = hero.rect.top
        
    def update(self):
        """向上移动子弹"""
        #更新screen实例的rect属性
        self.screen_rect = self.screen.get_rect()
        #更新表示子弹位置的小数值
        self.y -= self.speed_factor
        #更新表示子弹位置的rect属性
        self.rect.y = self.y
        #删除消失的子弹
        if self.rect.bottom < 0:
            self.kill()