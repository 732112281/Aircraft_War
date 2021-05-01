#coding:utf-8
from pygame.sprite import Sprite
class Ufo(Sprite):
    def __init__(self, settings, game_starts, screen, randint, type):
        super().__init__()
        self.type = type
        self.settings = settings
        self.game_starts = game_starts
        self.screen = screen
        self.activetime = 0
        #初始化道具设置
        self.init(randint)
        #获取道具图片和screen对象的rect属性
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()
        #每个道具最初的坐标
        if self.screen_rect.width > self.rect.width:
            self.rect.x = randint(0, self.screen_rect.width - self.rect.width)
        else:
            self.rect.x = 0
        self.rect.y -= self.rect.height
        #用小数值存储道具坐标
        self.y = float(self.rect.y)
        
    def init(self, randint):
        """初始化道具各项属性"""
        if self.type == 1:
            #道具1速度
            self.speed_factor = self.game_starts.ufo1_speed_factor
            #道具1图片
            self.image = self.settings.ufo_images[0].convert_alpha()
            #道具1效果持续时间
            self.keeptime = self.game_starts.ufo1_keeptime * 30
        elif self.type == 2:
            #道具2速度
            self.speed_factor = self.game_starts.ufo2_speed_factor
            #道具2图片
            self.image = self.settings.ufo_images[1].convert_alpha()
            #道具2效果持续时间
            self.keeptime = self.game_starts.ufo2_keeptime * 30
    
    def update(self):
        """向下移动道具"""
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
    
    def active_effect(self, game_starts):
        """道具激活后的效果"""
        if self.activetime > self.keeptime:
            self.reset(game_starts)
            self.kill()
        if self.activetime == 0:
            if self.type == 1:
                game_starts.bullet_damage *= 4
            elif self.type == 2:
                game_starts.bullet_line += 2
            self.activetime = 1
        elif self.activetime > 0:
            self.activetime +=1
    
    def reset(self, game_starts):
        """重置被效果更改后的设置"""
        if self.type == 1:
#            game_starts.bullet_damage = self.settings.bullet_damage
            game_starts.bullet_damage /= 4
        elif self.type == 2:
#            game_starts.bullet_line = self.settings.bullet_line
            game_starts.bullet_line -= 2