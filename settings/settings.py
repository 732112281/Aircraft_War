#coding:utf-8
import pygame
from sys import path
path.append('../')
class Settings():
    """储存《飞机大战》中所有设置的类"""
    def __init__(self):
        """初始化游戏的静态设置"""
    
        '''游戏设置'''
    
        #游戏最高帧率
        self.hightest_FPS = 80
        #游戏最高分数据存储文件名
        self.hightest_score_filename = "saves/hightest_score.awr"
        #游戏最高分图片
        self.hightest_score_image = pygame.image.load\
                                        ("images/hightest_score.png")
        #游戏分数图片
        self.score_image = pygame.image.load("images/scores.png")
        #游戏标题图片
        self.title_image = pygame.image.load("images/title.png")
        #增加难度间隔运行时间
        self.increase_hard_interval = 150
    
        ''' 窗口设置'''
    
        #窗口底色
        self.bg_color = (195, 200, 201)
        #窗口标题
        self.title = "Aircraft war"
        #设置窗口图标
        self.gamephoto = pygame.image.load("images/GamePhoto.png")
    
        '''背景设置'''
    
        #背景移动速度
        self.background_speed_factor = 0.5
        #背景图片
        self.background_image = pygame.image.load("images/background.png")
    
        '''按钮设置'''
    
        #按钮尺寸
        self.button_width, self.button_height = 100, 52
        #按钮颜色
        self.button_up_color = (195, 200, 201)
        #按钮中文本颜色
        self.button_text_color = (99, 102, 103)
        #按钮字体种类
        self.button_font_kind = None
        #按钮中文本大小
        self.button_font_size = 60
        '''PLAY按钮'''
        #PLAY按钮ID
        self.play_button_ID = 0
        #PLAY按钮文字内容
        self.play_button_msg = "PLAY"
        #PLAY按钮落下按钮颜色
        self.play_button_down_bg_color = (155, 155, 155)
        '''暂停按钮'''
        #暂停按钮ID
        self.stop_button_ID = 1
        #暂停按钮抬起图片
        self.stop_button_up_image = pygame.image.load\
                                    ("images/stop_button_up.png")
        #暂停按钮落下图片
        self.stop_button_down_image = pygame.image.load\
                                    ("images/stop_button_down.png")
        '''继续按钮'''
        #继续按钮ID
        self.continue_button_ID = 2
        #继续按钮抬起图片
        self.continue_button_up_image = pygame.image.load\
                                    ("images/continue_button_up.png")
        #继续按钮落下图片
        self.continue_button_down_image = pygame.image.load\
                                    ("images/continue_button_down.png")
    
        '''计分板设置'''
    
        #计分板字体颜色
        self.scoreboard_text_color = (230, 230, 230)
        #计分板字体种类
        self.scoreboard_font_kind = None
        #计分板字体大小
        self.scoreboard_font_size =48

    
        '''飞船设置'''
        
        #飞船被击中时闪烁动画每帧持续时间
        self.ship_Invincible_everyticktime = 10
        #飞船爆炸动画每帧持续时间
        self.ship_bomb_everyticktime = 5
        #射击间隔
        self.shoot_interval = 10
        '飞船图片'
        #飞船本体图片
        self.ship_image = pygame.image.load("images/ship.png")
        #飞船图片列表
        self.ship_images=[]
        #飞船图片
        self.ship_images.append(pygame.image.load("images/hero1.png"))
        self.ship_images.append(pygame.image.load("images/hero2.png"))
        #飞船爆炸图片列表
        self.ship_down_images=[]
        #飞船爆炸图片
        self.ship_down_images.append(pygame.image.load\
                                     ("images/hero_down1.png"))
        self.ship_down_images.append(pygame.image.load\
                                     ("images/hero_down2.png"))
        self.ship_down_images.append(pygame.image.load\
                                     ("images/hero_down3.png"))
        self.ship_down_images.append(pygame.image.load\
                                     ("images/hero_down4.png"))
    
        '''子弹设置'''
    
        #多行子弹最外侧两行之间间距
        self.bullets_spacing = 50
        '子弹图片'
        #子弹图片列表
        self.bullet_images=[]
        #子弹图片
        self.bullet_images.append(pygame.image.load("images/bullet1.png"))
        self.bullet_images.append(pygame.image.load("images/bullet2.png"))
    
        '''道具设置'''
        
        #生成道具间隔时间
        self.spawn_ufo_interval = 100
        '道具图片'
        #道具图片列表
        self.ufo_images = []
        #道具图片
        self.ufo_images.append(pygame.image.load("images/ufo1.png"))
        self.ufo_images.append(pygame.image.load("images/ufo2.png"))

        '''敌飞船设置'''
    
        #生成敌飞船初始时间间隔
        self.spawn_enemy_interval=50
    
        #敌飞船移动动画每帧持续时间
        self.enemy_move_everyticktime = 20
        #敌飞船被击中动画每帧持续时间
        self.enemy2_beenhit_everyticktime = self.enemy3_beenhit_everyticktime \
                                          = 10
        #敌飞机爆炸动画每帧持续时间
        self.enemy1_bomb_everyticktime = self.enemy2_bomb_everyticktime \
                                       = self.enemy3_bomb_everyticktime = 5
        '敌飞船1图片'
        #敌飞船1图片
        self.enemy1_images=[]
        self.enemy1_images.append(pygame.image.load("images/enemy1.png"))
        #敌飞船1爆炸图片
        self.enemy1_down_images=[]
        self.enemy1_down_images.append(pygame.image.load\
                                       ("images/enemy1_down1.png"))
        self.enemy1_down_images.append(pygame.image.load\
                                       ("images/enemy1_down2.png"))
        self.enemy1_down_images.append(pygame.image.load\
                                       ("images/enemy1_down3.png"))
        self.enemy1_down_images.append(pygame.image.load\
                                       ("images/enemy1_down4.png"))
        '敌飞船2图片'
        #敌飞船2图片
        self.enemy2_images=[]
        self.enemy2_images.append(pygame.image.load("images/enemy2.png"))
        self.enemy2_images.append(pygame.image.load("images/enemy2_hit.png"))
        #敌飞船2爆炸图片
        self.enemy2_down_images=[]
        self.enemy2_down_images.append(pygame.image.load\
                                       ("images/enemy2_down1.png"))
        self.enemy2_down_images.append(pygame.image.load\
                                       ("images/enemy2_down2.png"))
        self.enemy2_down_images.append(pygame.image.load\
                                       ("images/enemy2_down3.png"))
        self.enemy2_down_images.append(pygame.image.load\
                                       ("images/enemy2_down4.png"))
        '敌飞船3图片'
        #敌飞船3图片
        self.enemy3_images=[]
        self.enemy3_images.append(pygame.image.load("images/enemy3_1.png"))
        self.enemy3_images.append(pygame.image.load("images/enemy3_2.png"))
        self.enemy3_images.append(pygame.image.load("images/enemy3_hit.png"))
        #敌飞船3爆炸图片
        self.enemy3_down_images=[]
        self.enemy3_down_images.append(pygame.image.load\
                                       ("images/enemy3_down1.png"))
        self.enemy3_down_images.append(pygame.image.load\
                                       ("images/enemy3_down2.png"))
        self.enemy3_down_images.append(pygame.image.load\
                                       ("images/enemy3_down3.png"))
        self.enemy3_down_images.append(pygame.image.load\
                                       ("images/enemy3_down4.png"))
        self.enemy3_down_images.append(pygame.image.load\
                                       ("images/enemy3_down5.png"))
        self.enemy3_down_images.append(pygame.image.load\
                                       ("images/enemy3_down6.png"))
    
        self.initialize_dynamic_settings()
    def initialize_dynamic_settings(self):
        """初始化随游戏进行而变化的设置"""
        
        '''游戏设置'''
        
        #游戏初始进行速率
        self.rander_speed = 1
        #游戏初始最高帧数
        self.hightest_ticks = 75
        
        '''窗口设置'''
        
        #初始窗口大小
        self.screen_width, self.screen_height = 960, 652 
        
        '''飞船设置'''
        
        #飞船初始移动速度
        self.ship_speed_factor = 3
        #无敌时间
        self.ship_Invincible_time = 60
        #飞船初始生命值
        self.lifes = 3
        #初始分数
        self.scores = 0
        
        '''子弹设置'''
        
        #子弹移动速度
        self.bullet_speed_factor=4
        #子弹伤害初始值
        self.bullet_damage = 1
        #子弹行数初始值
        self.bullet_line = 1
        
        '''道具设置'''
        
        #道具1移动速度
        self.ufo1_speed_factor = 0.5
        #道具2移动速度
        self.ufo2_speed_factor = 0.5
        #道具1持续时间
        self.ufo1_keeptime = 30
        #道具2持续时间
        self.ufo2_keeptime = 30
        
        '''敌飞船设置'''
        
        #敌飞船生命值
        self.enemy1_life = 1
        self.enemy2_life = 8
        self.enemy3_life = 20
        #敌飞船分数
        self.enemy1_score = 1
        self.enemy2_score = 7
        self.enemy3_score = 15
        #敌飞船移动速度
        self.enemy_speed_factor1 = 2
        self.enemy_speed_factor2 = 2.5

if __name__ == '__main__':
    settings = Settings()