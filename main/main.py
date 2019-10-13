#coding:utf-8
import pygame
from pygame.sprite import Group
from time import time
from sys import path
path.append('../')
from settings.settings import Settings
from settings.game_starts import GameStarts
from moudle.button import Button
from moudle.background import Background
from moudle.hero import Hero
from moudle.scoreboard import Scoreboard
import main.game_functions as gf

def main():
    """初始化设置、游戏统计信息、窗口、背景、飞船、子弹和敌飞船对象，并开始游戏主循环"""
    pygame.init()
    '''初始化游戏设置'''
    #创建一个用于储存游戏设置的实例
    settings = Settings()
    '''初始化窗口'''
    screen = pygame.display.set_mode((settings.screen_width, 
                                      settings.screen_height),pygame.RESIZABLE)
    #设置窗口标题
    pygame.display.set_caption(settings.title)
    #设置窗口图标
    pygame.display.set_icon(settings.gamephoto.convert_alpha())
    '''创建按钮'''
    #play按钮
    play_button = Button(settings, screen, ID=settings.play_button_ID, 
                         msg=settings.play_button_msg, 
                         down_bg_color=settings.play_button_down_bg_color)
    #暂停按钮
    stop_button = Button(settings, screen, ID=settings.stop_button_ID, 
                         active_blit=True, stop_blit=False,
                         up_image=settings.stop_button_up_image,
                         down_image=settings.stop_button_down_image)
    #继续按钮
    continue_button = Button(settings, screen, ID=settings.continue_button_ID, 
                             active_blit=True,
                             up_image=settings.continue_button_up_image,
                             down_image=settings.continue_button_down_image)
    #创建一艘飞船、一个子弹编组和一个敌飞船编组
    bullets = Group()
    enemies = Group()
    down_enemies = Group()
    ufos = Group()
    active_ufos = Group()
    buttons = []
    buttons.append(play_button)
    buttons.append(stop_button)
    buttons.append(continue_button)
    '''初始化游戏统计信息'''
    #创建一个用于储存游戏统计信息的实例
    game_starts = GameStarts(settings, bullets, enemies, 
                        down_enemies, ufos, active_ufos)
    '''初始化背景'''
    #创建一个用于储存背景的实例
    bg = Background(settings,screen)
    '''初始化计分板'''
    #创建一个计分板实例
    scoreboard = Scoreboard(settings, screen, game_starts)
    '''初始化敌飞船'''
    #创建一个飞船实例
    hero = Hero(settings, game_starts, screen)

    """开启游戏主循环"""
    while True:
        start_time = time()
        gf.surface(settings, game_starts, screen, bg, hero, bullets, enemies, 
                   down_enemies, ufos, active_ufos, scoreboard, buttons)
        gf.check_events(settings, game_starts, scoreboard, hero, buttons)
        if not game_starts.game_active or game_starts.game_stop:
            continue
        gf.update(game_starts, bg, hero, bullets, enemies, down_enemies,
                   ufos, active_ufos)
        gf.shoot(settings, game_starts, screen, hero, bullets)
        gf.spawn_enemy(settings, game_starts, screen, enemies)
        gf.spawn_ufo(settings, game_starts, screen, ufos)
        gf.check_collide(settings, game_starts, hero, enemies, down_enemies,
                         bullets, ufos, active_ufos)
        if time() - start_time <= 0:
            continue
        gf.set_PFS(settings, game_starts, screen, 1.0 / (time() - start_time))