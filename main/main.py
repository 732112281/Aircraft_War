#coding:utf-8
import pygame
from pygame.sprite import Group
from time import time
from sys import path
path.append('../')
from settings.settings import Settings
from settings.game_starts import GameStarts
#from moudle.button import Button
from moudle.background import Background
from moudle.hero import Hero
import main.game_functions as gf

def main():
    """初始化设置、游戏统计信息、窗口、背景、飞船、子弹和敌飞船对象，并开始游戏主循环"""
    pygame.init()
    '''初始化游戏设置'''
    #创建一个用于储存游戏设置的实例
    settings = Settings()
    '''初始化窗口'''
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height),
                                     pygame.RESIZABLE)
    #设置窗口标题
    pygame.display.set_caption(settings.title)
    #设置窗口图标
    gamephoto = pygame.image.load("images/GamePhoto.png")
    pygame.display.set_icon(gamephoto)
    '''创建Play按钮'''
    #play_button = Button(settings, screen, msg="PLAY")
    '''初始化游戏统计信息'''
    #创建一个用于储存游戏统计信息的实例
    game_starts = GameStarts(settings)
    '''初始化背景'''
    #创建一个用于储存背景的实例
    bg = Background(settings,screen)
    '''初始化飞船、子弹、敌飞船'''
    hero = Hero(settings, screen)
    #创建一艘飞船、一个子弹编组和一个敌飞船编组
    bullets = Group()
    enemies = Group()
    down_enemies = Group()
    buttons = Group()
    ufos = Group()
    active_ufos = Group()

    """开启游戏主循环"""
    while True:
        start_time = time()
        gf.surface(screen, bg, hero, bullets, enemies, down_enemies, ufos, active_ufos)
        gf.check_events(hero)
        gf.update(game_starts, bg, hero, bullets, enemies, down_enemies, ufos, active_ufos)
        gf.shoot(settings, game_starts, screen, hero, bullets)
        gf.spawn_enemy(settings, screen, enemies)
        gf.spawn_ufo(settings, screen, ufos)
        gf.check_collide(game_starts, hero, enemies, down_enemies, bullets, ufos, active_ufos)
        gf.set_PFS(game_starts, screen, 1.0 / (time() - start_time))