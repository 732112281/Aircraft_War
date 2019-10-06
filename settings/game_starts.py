#coding:utf-8
class GameStarts():
    """跟踪游戏的统计信息"""
    
    def __init__(self,settings, bullets, enemies, 
                        down_enemies, ufos, active_ufos):
        """初始化统计信息"""
        self.reset_game(settings, bullets, enemies, 
                        down_enemies, ufos, active_ufos)
        #游戏刚启动时处于非活动状态
        self.game_active = False
        self.game_stop = True
    def reset_game(self, settings, bullets, enemies, 
                         down_enemies, ufos, active_ufos):
        """初始化在游戏运行期间可能变化的统计信息"""
        self.lifes = settings.lifes
        self.scores = settings.scores
        self.bullet_damage = settings.bullet_damage
        self.bullet_line = settings.bullet_line
        self.rander_speed = settings.rander_speed
        self.hightest_ticks = settings.hightest_ticks
        self.hightest_FPS = settings.hightest_FPS
        bullets.empty()
        enemies.empty()
        down_enemies.empty()
        ufos.empty()
        active_ufos.empty()