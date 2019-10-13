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
def check_keydown(event, game_starts, sd, ship):
    """检测键盘被按下"""
    #英雄机移动
    if event.key == pygame.K_a or event.key == pygame.K_LEFT:
        ship.offset['move_left'] = ship.speed_factor
    if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
        ship.offset['move_right'] = ship.speed_factor
    if event.key == pygame.K_w or event.key == pygame.K_UP:
        ship.offset['move_up'] = ship.speed_factor
    if event.key == pygame.K_s or event.key == pygame.K_DOWN:
        ship.offset['move_down'] = ship.speed_factor
    #游戏处理
    if event.key == pygame.K_ESCAPE:
        pygame.quit()
        exit() 
    #按空格暂停,按任意键恢复
    if event.key == pygame.K_SPACE:
        if game_starts.game_active:
            game_starts.game_stop = not game_starts.game_stop
    elif game_starts.game_active and game_starts.game_stop:
        game_starts.game_stop = False
    #按R键重新开始
    if event.key == pygame.K_r:
        game_starts.reset_game()
        #重置飞船位置
        ship.center_ship()
        game_starts.game_active = True
        game_starts.game_stop = False
        game_starts.game_over = False
        sd.prep_score()
        sd.prep_life()
        
def check_keyup(event, ship):
    """检测键盘空闲"""
    #飞船移动
    if event.key == pygame.K_a or event.key == pygame.K_LEFT:
        ship.offset['move_left'] = 0
    if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
        ship.offset['move_right'] = 0
    if event.key == pygame.K_w or event.key == pygame.K_UP:
        ship.offset['move_up'] = 0
    if event.key == pygame.K_s or event.key == pygame.K_DOWN:
        ship.offset['move_down'] = 0
        
def check_events(settings, game_starts, sd, ship, buttons):
    mouse_x, mouse_y = pygame.mouse.get_pos()
    """监听键盘事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        #检测鼠标按下
        if event.type == pygame.MOUSEBUTTONDOWN:
            button_active(mouse_x, mouse_y, game_starts, sd, buttons, ship)
        #监听键盘被按下
        if event.type == pygame.KEYDOWN:
            check_keydown(event, game_starts, sd, ship)
        #监听键盘空闲
        elif event.type == pygame.KEYUP:
            check_keyup(event, ship)
        #检测屏幕宽度改变
        if event.type == pygame.VIDEORESIZE:
            SCREEN_SIZE = event.size
            pygame.display.set_mode(SCREEN_SIZE, RESIZABLE)
    #当鼠标在button上时,切换图像
    button_image_change(mouse_x, mouse_y, buttons)
    
def button_image_change(mouse_x, mouse_y, buttons):
    """按钮图片切换"""
    for button in [Button for Button in buttons 
                    if Button.down_msg_image or Button.down_image]:
        button_down = button.rect.collidepoint(mouse_x, mouse_y)
        button.change_image(button_down)
        
def button_active(mouse_x, mouse_y, game_starts, sd, buttons, ship):
    """按钮按下效果"""
    for button in buttons:
        if button.rect.collidepoint(mouse_x, mouse_y):
            if button.ID == 0 and \
                button.active_blit == game_starts.game_active:
                game_starts.game_active = True
                game_starts.game_stop = False
                game_starts.game_over = False
                game_starts.reset_game()
                #重置飞船位置
                ship.center_ship()
                sd.prep_score()
                sd.prep_life()
            elif button.ID == 1 and button.stop_blit == game_starts.game_stop:
                        game_starts.game_stop = True
            elif button.ID == 2 and button.stop_blit == game_starts.game_stop:
                game_starts.game_stop = False
            
def is_ActionTime(ticks, interval):
    """检测时间间隔"""
    return ticks % interval == 0

def shoot(settings, game_starts, screen, hero, bullets):
    """定时生成子弹"""
    global shoot_ticks
    shoot_ticks += 1    #子弹生成时间索引增加
    #判断是否到了生成子弹的时候
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
    shoot_ticks = 0 #重置子弹生成时间索引

def spawn_enemy(settings, game_starts, screen, enemies):
    """定时生成敌飞船"""
    global spawn_enemy_ticks
    spawn_enemy_ticks += 1  #敌机生成时间索引增加
    screen_width = screen.get_width()   #更新屏幕宽度
    #判断是否到了生成敌机的时候
    if not is_ActionTime(spawn_enemy_ticks,
                (settings.spawn_enemy_interval*220//screen_width)):
        return
    #随机生成敌机
    n = randint(1,20)
    if n <= 16:
        new_enemy1=Enemy(settings, game_starts, screen, randint, 1)
        enemies.add(new_enemy1)
    elif n > 16 and n <20: 
        new_enemy2=Enemy(settings, game_starts, screen, randint, 2)
        enemies.add(new_enemy2)
    elif n == 20:
        new_enemy3=Enemy(settings, game_starts, screen, randint, 3)
        if len(enemies) == 0 or not[enemy3 for enemy3 in enemies.sprites() 
                                     if enemy3.type == 3]:
            enemies.add(new_enemy3)
    spawn_enemy_ticks = 0   #重置敌机生成时间索引
            
def spawn_ufo(settings, game_starts, screen, ufos):
    """定时生成道具"""
    global spawn_ufo_ticks
    #限制道具上限
    if len(ufos) > 4:
        return
    spawn_ufo_ticks += 1    #道具生成时间索引增加
    screen_width = screen.get_width()   #更新屏幕宽度
    #判断是否到了生成道具的时候
    if not is_ActionTime(spawn_ufo_ticks,
                (settings.spawn_ufo_interval*4400//screen_width)):
        return
    #随机生成道具
    n = randint(1,2)
    if n == 1:
        new_ufo1=Ufo(settings, game_starts, screen, randint, 1)
        ufos.add(new_ufo1)  
    elif n == 2:
        new_ufo2=Ufo(settings, game_starts, screen, randint, 2)
        ufos.add(new_ufo2)
    spawn_ufo_ticks = 0 #重置道具生成时间索引
        
def check_collide(settings, game_starts, hero, enemies, down_enemies, 
                  bullets, ufos, active_ufos):
    """碰撞检测"""
    #检测敌机是否与子弹发生了碰撞
    bm_collisions = pygame.sprite.groupcollide(enemies, bullets, False, True)
    for enemy in bm_collisions:
        #若碰撞，敌机生命值减少
        enemy.life -= game_starts.bullet_damage
        if enemy.life <= 0:
            #若敌机生命值小于等于0，更新计分板，删除敌机， 播放敌机爆炸动画
            game_starts.scores += enemy.score
            enemy.kill()
            down_enemies.add(enemy)
        elif enemy.life > 0:
            #若敌机生命值大于0，播放敌机碰撞动画，并清零碰撞动画播放时间索引
            enemy.been_hit = True
            enemy.hit_ticks = 0
    #检测飞船是否与道敌机发生了碰撞
    hm_collisions = pygame.sprite.spritecollide(hero, enemies, True)
    for enemy in hm_collisions:
        #若碰撞，删除敌机，播放敌机爆炸动画，飞船生命值减1
        down_enemies.add(enemy)
        if not hero.Invincible:
            hero.Invincible = True
            game_starts.lifes -= 1
            if game_starts.lifes <= 0:
                game_starts.game_active = False
                game_starts.game_stop = True
                game_starts.game_over = True
                save(settings, game_starts)
    #检测飞船是否与道具发生了碰撞
    hu_collisions = pygame.sprite.spritecollide(hero, ufos, True)
    for ufo in hu_collisions:
        #若碰撞，检测是否有已激活的相同种道具
        same_ufos = [same_ufo for same_ufo in active_ufos 
                     if same_ufo.type == ufo.type]
        if same_ufos:
            #若有已激活的相同种道具,重置被效果更改后的设置,并删除相同的道具,启动与飞船碰撞的道具效果
            for same_ufo in same_ufos:
                same_ufo.reset(game_starts)
                same_ufo.kill()
                active_ufos.add(ufo)
        else:
            #若没有已激活的相同种道具,启动与飞船碰撞的道具效果
            active_ufos.add(ufo)
        
def surface(settings, game_starts, screen, bg, hero, bullets, enemies, 
            down_enemies, ufos, active_ufos, sd, buttons):
    """绘制各个Group中对象"""
    bg.draw()
    #判断游戏是否激活
    if game_starts.game_active:
        bullets.draw(screen)
        hero.draw()
        enemies.draw(screen)
        down_enemies.draw(screen)
        ufos.draw(screen)
        sd.draw()
    elif not game_starts.game_active:
        if game_starts.game_over:
            GameOver(settings, game_starts, screen, sd, hero)
        else:
            GameStart(settings, screen)
    #根据游戏状态绘制按钮
    for button in [Button for Button in buttons 
                   if Button.active_blit == game_starts.game_active 
                      and Button.stop_blit == game_starts.game_stop]:
        button.draw(sd.score_rect)
    #更新屏幕
    pygame.display.flip()    
    #限制游戏运行速率
    pygame.time.Clock().tick(game_starts.hightest_ticks 
                             * game_starts.rander_speed)
def update(game_starts, bg, hero, bullets, 
           enemies, down_enemies, ufos, active_ufos):
    """调用各个Sprite及Group的update方法"""
    #判断游戏是否激活，以及是否暂停
    if not game_starts.game_active or game_starts.game_stop:
        return 
    game_starts.hard_update()
    bg.update()
    hero.update()
    hero.Invincible_update()
    bullets.update()
    enemies.update()
    ufos.update()
    for ufo in active_ufos:
        ufo.active_effect(game_starts)
    for enemy in [enemy3 for enemy3 in enemies.sprites() if enemy3.type == 3]:
        enemy.enemy3_image_update()
    for enemy in down_enemies.sprites():
        enemy.bomb_update()
    
def set_PFS(settings, game_starts, screen, FPS):
    """调整游戏帧率"""
    #获取实时屏幕宽和高
    screen_width = screen.get_width()
    screen_height = screen.get_height()
    #根据屏幕宽和高调整帧数上限
    if FPS < settings.hightest_FPS * game_starts.rander_speed \
             + ((screen_width // screen_height)**2):
        game_starts.hightest_ticks += 5
    elif FPS > settings.hightest_FPS * game_starts.rander_speed \
               + ((screen_width // screen_height)**2):
        game_starts.hightest_ticks -= 5
        
def save(settings, game_starts):
    """存档"""
    filename = settings.hightest_score_filename
    try:
        with open(filename) as h_sco:
            hightest_score = h_sco.read()
            if int(game_starts.scores) > int(hightest_score):
                with open(filename,'w') as h_sco:
                    h_sco.write(str(int(game_starts.scores)))
                game_starts.hightest_score = int(game_starts.scores)
            else:
                game_starts.hightest_score = int(game_starts.scores)
    except FileNotFoundError:
        with open(filename,'w') as h_sco:
            h_sco.write(str(int(game_starts.scores)))
        game_starts.hightest_score = int(game_starts.scores)
        
def GameOver(settings, game_starts, screen, sd, ship):
    """游戏结束后的界面，存档，重置游戏"""
    if game_starts.lifes <= 0:
        save(settings, game_starts)
    #更新screen对象的rect属性
    screen_rect = screen.get_rect()
    #更新h_score_rect的rect属性，并将其放置于screen的左上角
    h_score_rect = settings.hightest_score_image.get_rect()
    h_score_rect.topleft = screen_rect.topleft
    #将hightest_score_image渲染在screen上
    screen.blit(settings.hightest_score_image, h_score_rect)
    #将最高分分数渲染在screen上
    sd.prep_hightest_score(h_score_rect)
    
    #更新h_score_rect的rect属性，并将其放置于screen的中部3/4高处
    score_rect = settings.score_image.get_rect()
    score_rect.centerx = screen_rect.centerx 
    score_rect.centery = screen_rect.centery* 3/4
    #将hightest_score_image渲染在screen上
    screen.blit(settings.score_image, score_rect)
    #将分数渲染在screen上
    sd.prep_score(score_image_rect=score_rect)

def GameStart(settings, screen):
    screen_rect = screen.get_rect()
    title_rect = settings.title_image.get_rect()
    title_rect.centerx = screen_rect.centerx
    title_rect.centery = screen_rect.centery * 2/3
    screen.blit(settings.title_image, title_rect)