#coding:utf-8
import pygame
from sys import path
path.append('../')
class Settings():
    """储存《飞机大战》中所有设置的类"""
    
    '''游戏设置'''
    
    #游戏速率
    rander_speed = 1
    hightest_ticks = 75
    hightest_FPS = 100
    
    ''' 窗口设置'''
    
    #窗口大小
    screen_width, screen_height = 960, 652 
    #窗口底色
    bg_color = (195, 200, 201)
    #窗口标题
    title = "Aircraft war"
    
    '''背景设置'''
    
    #背景移动速度
    background_speed_factor = 0.5
    #背景图片
    background_image = pygame.image.load("images/background.png")
    
    '''按钮设置'''
    
    #按钮尺寸
    button_width, button_height = 100, 52
    #按钮颜色
    button_up_color = (195, 200, 201)
    #按钮中文本颜色
    button_text_color = (99, 102, 103)
    #按钮字体种类
    button_font_kind = None
    #按钮中文本大小
    button_font_size = 60
    
    '''计分板设置'''
    
    #计分板字体颜色
    scoreboard_text_color = (230, 230, 230)
    #计分板字体种类
    scoreboard_font_kind = None
    #计分板字体大小
    scoreboard_font_size =48
    #飞船初始生命值
    lifes = 3
    #初始分数
    scores = 0
    
    '''飞船设置'''
    
    #飞船移动速度
    ship_speed_factor = 3
    #射击间隔
    shoot_interval = 10
    #飞船爆炸动画每帧持续时间
    ship_bomb_everyticktime = 5
    '飞船图片'
    #飞船图片列表
    ship_images=[]
    #飞船图片
    ship_images.append(pygame.image.load("images/hero1.png"))
    ship_images.append(pygame.image.load("images/hero2.png"))
    #飞船爆炸图片列表
    ship_down_images=[]
    #飞船爆炸图片
    ship_down_images.append(pygame.image.load("images/hero_down1.png"))
    ship_down_images.append(pygame.image.load("images/hero_down2.png"))
    ship_down_images.append(pygame.image.load("images/hero_down3.png"))
    ship_down_images.append(pygame.image.load("images/hero_down4.png"))
    
    '''子弹设置'''
    
    #子弹移动速度
    bullet_speed_factor=4
    #子弹伤害初始值
    bullet_damage = 1
    #子弹行数初始值
    bullet_line = 1
    #多行子弹最外侧两行之间间距
    bullets_spacing = 50
    '子弹图片'
    #子弹图片列表
    bullet_images=[]
    #子弹图片
    bullet_images.append(pygame.image.load("images/bullet1.png"))
    bullet_images.append(pygame.image.load("images/bullet2.png"))
    
    '''道具设置'''
    
    #道具1移动速度
    ufo1_speed_factor = 0.5
    #道具2移动速度
    ufo2_speed_factor = 0.5
    #生成道具间隔时间
    spawn_ufo_interval = 100
    #道具1持续时间
    ufo1_keeptime = 30
    #道具2持续时间
    ufo2_keeptime = 30
    '道具图片'
    #道具图片列表
    ufo_images = []
    #道具图片
    ufo_images.append(pygame.image.load("images/ufo1.png"))
    ufo_images.append(pygame.image.load("images/ufo2.png"))

    '''敌飞船设置'''
    
    #敌飞船移动速度
    enemy_speed_factor1=2
    enemy_speed_factor2=2.5
    #生成敌飞船初始时间间隔
    spawn_enemy_interval=50
    #敌飞船生命值
    enemy1_life=1
    enemy2_life=8
    enemy3_life=20
    #敌飞船分数
    enemy1_score=1
    enemy2_score=7
    enemy3_score=15
    #敌飞船移动动画每帧持续时间
    enemy_move_everyticktime = 20
    #敌飞船被击中动画每帧持续时间
    enemy2_beenhit_everyticktime = enemy3_beenhit_everyticktime = 10
    #敌飞机爆炸动画每帧持续时间
    enemy1_bomb_everyticktime = enemy2_bomb_everyticktime \
    = enemy3_bomb_everyticktime = 5
    '敌飞船1图片'
    #敌飞船1图片
    enemy1_images=[]
    enemy1_images.append(pygame.image.load("images/enemy1.png"))
    #敌飞船1爆炸图片
    enemy1_down_images=[]
    enemy1_down_images.append(pygame.image.load("images/enemy1_down1.png"))
    enemy1_down_images.append(pygame.image.load("images/enemy1_down2.png"))
    enemy1_down_images.append(pygame.image.load("images/enemy1_down3.png"))
    enemy1_down_images.append(pygame.image.load("images/enemy1_down4.png"))
    '敌飞船2图片'
    #敌飞船2图片
    enemy2_images=[]
    enemy2_images.append(pygame.image.load("images/enemy2.png"))
    enemy2_images.append(pygame.image.load("images/enemy2_hit.png"))
    #敌飞船2爆炸图片
    enemy2_down_images=[]
    enemy2_down_images.append(pygame.image.load("images/enemy2_down1.png"))
    enemy2_down_images.append(pygame.image.load("images/enemy2_down2.png"))
    enemy2_down_images.append(pygame.image.load("images/enemy2_down3.png"))
    enemy2_down_images.append(pygame.image.load("images/enemy2_down4.png"))
    '敌飞船3图片'
    #敌飞船3图片
    enemy3_images=[]
    enemy3_images.append(pygame.image.load("images/enemy3_1.png"))
    enemy3_images.append(pygame.image.load("images/enemy3_2.png"))
    enemy3_images.append(pygame.image.load("images/enemy3_hit.png"))
    #敌飞船3爆炸图片
    enemy3_down_images=[]
    enemy3_down_images.append(pygame.image.load("images/enemy3_down1.png"))
    enemy3_down_images.append(pygame.image.load("images/enemy3_down2.png"))
    enemy3_down_images.append(pygame.image.load("images/enemy3_down3.png"))
    enemy3_down_images.append(pygame.image.load("images/enemy3_down4.png"))
    enemy3_down_images.append(pygame.image.load("images/enemy3_down5.png"))
    enemy3_down_images.append(pygame.image.load("images/enemy3_down6.png"))

if __name__ == '__main__':
    settings = Settings()