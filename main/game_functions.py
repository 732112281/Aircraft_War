#coding:utf-8
import pygame
from pygame.locals import *
from random import randint
from sys import exit,path
path.append('../')
from moudle.bullet import Bullet
from moudle.enemy import Enemy
from moudle.ufo import Ufo

spawn_enemy_ticks = shoot_ticks = spawn_ufo_ticks = 0
def check_keydown(event, ship):
    """检测键盘被按下"""
    #英雄机移动
    if event.key == K_a or event.key == K_LEFT:
        ship.offset['move_left'] = ship.speed_factor
    if event.key == K_d or event.key == K_RIGHT:
        ship.offset['move_right'] = ship.speed_factor
    if event.key == K_w or event.key == K_UP:
        ship.offset['move_up'] = ship.speed_factor
    if event.key == K_s or event.key == K_DOWN:
        ship.offset['move_down'] = ship.speed_factor
    #游戏处理
    if event.key == K_ESCAPE:
        pygame.quit()
        exit() 
        
def check_keyup(event, ship):
    """检测键盘空闲"""
    if event.key == K_a or event.key == K_LEFT:
        ship.offset['move_left'] = 0
    if event.key == K_d or event.key == K_RIGHT:
        ship.offset['move_right'] = 0
    if event.key == K_w or event.key == K_UP:
        ship.offset['move_up'] = 0
    if event.key == K_s or event.key == K_DOWN:
        ship.offset['move_down'] = 0
        
def check_events(ship):
    """监听键盘事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        #监听键盘被按下
        if event.type == pygame.KEYDOWN:
            check_keydown(event, ship)
        #监听键盘空闲
        elif event.type == pygame.KEYUP:
            check_keyup(event, ship)
        if event.type == VIDEORESIZE:
            SCREEN_SIZE = event.size
            pygame.display.set_mode(SCREEN_SIZE, RESIZABLE)

def is_ActionTime(ticks, interval):
    """检测时间间隔"""
    return ticks % interval == 0

def shoot(settings, game_starts, screen, hero, bullets):
    """定时生成子弹"""
    global shoot_ticks
    shoot_ticks += 1
    if not is_ActionTime(shoot_ticks, settings.shoot_interval):
        return
    #在正确的位置创建子弹
    spacing = settings.bullets_spacing
    for bullet_centerx in range(game_starts.bullet_line):
        try:
            new_bullet_centerx = spacing * (bullet_centerx / 
                                            (game_starts.bullet_line - 1))
        except ZeroDivisionError:
            new_bullet_centerx = spacing / 2
        difference = (hero.rect.width - spacing) / 2
        new_bullet = Bullet(settings, game_starts, screen, hero, 
                            difference, new_bullet_centerx)
        bullets.add(new_bullet)

def spawn_enemy(settings, screen, enemies):
    """定时生成敌飞船"""
    global spawn_enemy_ticks
    spawn_enemy_ticks += 1
    screen_width = screen.get_width()
    if not is_ActionTime(spawn_enemy_ticks,
                (settings.spawn_enemy_interval*220//screen_width)):
        return
    n = randint(1,20)
    if n <= 16:
        new_enemy1=Enemy(settings, screen, randint, 1)
        enemies.add(new_enemy1)
    elif n > 16 and n <20: 
        new_enemy2=Enemy(settings, screen, randint, 2)
        enemies.add(new_enemy2)
    elif n == 20:
        new_enemy3=Enemy(settings, screen, randint, 3)
        if len(enemies) == 0 or not[enemy3 for enemy3 in enemies.sprites() 
                                     if enemy3.type == 3]:
            enemies.add(new_enemy3)
            
def spawn_ufo(settings, screen, ufos):
    """定时生成道具"""
    global spawn_ufo_ticks
    if len(ufos) > 4:
        return
    spawn_ufo_ticks += 1
    screen_width = screen.get_width()
    if not is_ActionTime(spawn_ufo_ticks,
                (settings.spawn_ufo_interval*4400//screen_width)):
        return
    n = randint(1,2)
    if n == 1:
        new_ufo1=Ufo(settings, screen, randint, 1)
        ufos.add(new_ufo1)
    if n == 2:
        new_ufo2=Ufo(settings, screen, randint, 2)
        ufos.add(new_ufo2)

def check_collide(game_starts, hero, enemies, down_enemies, 
                  bullets, ufos, active_ufos):
    """碰撞检测"""
    bm_collisions = pygame.sprite.groupcollide(enemies, bullets, False, True)
    for enemy in bm_collisions:
        enemy.life -= game_starts.bullet_damage
        if enemy.life <= 0:
            enemy.kill()
            down_enemies.add(enemy)
        elif enemy.life > 0:
            enemy.been_hit = True
            enemy.hit_ticks = 0
    hm_collisions = pygame.sprite.spritecollide(hero, enemies, True)
    for enemy in hm_collisions:
        down_enemies.add(enemy)
    hu_collisions = pygame.sprite.spritecollide(hero, ufos, True)
    for ufo in hu_collisions:
        same_ufos = [same_ufo for same_ufo in active_ufos 
                     if same_ufo.type == ufo.type]
        if same_ufos:
            for same_ufo in same_ufos:
                active_ufos.remove(same_ufo)
                active_ufos.add(ufo)
        else:
            active_ufos.add(ufo)
        
def surface(screen, bg, hero, bullets, 
            enemies, down_enemies, ufos, active_ufos):
    """绘制各个Group中对象"""
    bg.draw()
    bullets.draw(screen)
    hero.blitme()
    enemies.draw(screen)
    down_enemies.draw(screen)
    ufos.draw(screen)

def update(game_starts, bg, hero, bullets, 
           enemies, down_enemies, ufos, active_ufos):
    """调用各个Sprite及Group的update方法"""
    bg.update()
    hero.update()
    bullets.update()
    enemies.update()
    ufos.update()
    for ufo in active_ufos:
        ufo.active_effect(game_starts)
    for enemy in [enemy3 for enemy3 in enemies.sprites() if enemy3.type == 3]:
        enemy.enemy3_image_update()
    for enemy in down_enemies.sprites():
        enemy.bomb_update()
    pygame.display.flip()
    pygame.time.Clock().tick(game_starts.hightest_ticks 
                             * game_starts.rander_speed)

def set_PFS(game_starts, screen, FPS):
    """调整游戏帧率"""
    screen_width = screen.get_rect().width
    screen_height = screen.get_rect().height
    if FPS < game_starts.hightest_FPS * game_starts.rander_speed \
             + (screen_width // screen_height)^2:
        game_starts.hightest_ticks += 5
    elif FPS > game_starts.hightest_FPS * game_starts.rander_speed \
               + (screen_width // screen_height)^2:
        game_starts.hightest_ticks -= 5
    
    