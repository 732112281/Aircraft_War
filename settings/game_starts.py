#coding:utf-8
class GameStarts():
    """跟踪游戏的统计信息"""
    
    def __init__(self,settings, bullets, enemies, 
                        down_enemies, ufos, active_ufos):
        """初始化统计信息"""
        self.settings = settings
        self.bullets = bullets
        self.enemies = enemies
        self.down_enemies = down_enemies
        self.ufos = ufos
        self.active_ufos = active_ufos
        self.reset_game()
        self.hightest_score = None
        #游戏刚启动时处于非活动状态
        self.game_active = False
        self.game_stop = True
        self.game_over = False
        self.rander_ticks = 0
        self.increase_hard_time = 0
        
    def hard_update(self):
        self.rander_ticks += 1
        """随分数增加游戏难度"""
        if self.rander_ticks > self.settings.increase_hard_interval and \
        self.scores > self.increase_hard_time * \
        self.settings.increase_hard_interval:
            self.increase_hard_time += 1
            self.ship_speed_factor += 0.1
            self.ship_Invincible_time += 1
            self.ufo1_keeptime += 1
            self.ufo2_keeptime += 1
            self.enemy1_life += 0.2
            self.enemy2_life += 0.2
            self.enemy3_life += 0.2
            self.enemy1_score += 0.5
            self.enemy2_score += 0.5
            self.enemy3_score += 0.5
            self.enemy_speed_factor1 += 0.05
            self.enemy_speed_factor2 += 0.05
            self.randerticks = 0
        
    def reset_game(self):
        """重置在游戏运行期间可能变化的统计信息"""
        #重置游戏初始进行速率
        self.rander_speed = self.settings.rander_speed
        #重置游戏初始最高帧数
        self.hightest_ticks = self.settings.hightest_ticks
        #重置飞船初始移动速度
        self.ship_speed_factor = self.settings.ship_speed_factor
        #重置飞船被击中时的无敌时间
        self.ship_Invincible_time = self.settings.ship_Invincible_time
        #重置飞船初始生命值
        self.lifes = self.settings.lifes
        #重置初始分数
        self.scores = self.settings.scores 
        #重置子弹移动速度
        self.bullet_speed_factor = self.settings.bullet_speed_factor
        #重置子弹伤害初始值
        self.bullet_damage = self.settings.bullet_damage
        #重置子弹行数初始值
        self.bullet_line = self.settings.bullet_line
        #重置道具1移动速度
        self.ufo1_speed_factor = self.settings.ufo1_speed_factor
        #重置道具2移动速度
        self.ufo2_speed_factor = self.settings.ufo2_speed_factor
        #重置道具1持续时间
        self.ufo1_keeptime = self.settings.ufo1_keeptime
        #重置道具2持续时间
        self.ufo2_keeptime = self.settings.ufo2_keeptime
        #重置敌飞船生命值
        self.enemy1_life = self.settings.enemy1_life
        self.enemy2_life = self.settings.enemy2_life
        self.enemy3_life = self.settings.enemy3_life
        #重置敌飞船分数
        self.enemy1_score = self.settings.enemy1_score
        self.enemy2_score = self.settings.enemy2_score
        self.enemy3_score = self.settings.enemy3_score
        #重置敌飞船移动速度
        self.enemy_speed_factor1 = self.settings.enemy_speed_factor1
        self.enemy_speed_factor2 = self.settings.enemy_speed_factor2
        #清空子弹编组
        self.bullets.empty()
        #清空敌飞机编组
        self.enemies.empty()
        #清空被击毁的敌飞机编组
        self.down_enemies.empty()
        #清空道具编组
        self.ufos.empty()
        #清空激活的道具编组
        self.active_ufos.empty()