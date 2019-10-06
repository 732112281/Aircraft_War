#coding:utf-8
class GameStarts():
    """跟踪游戏的统计信息"""
    def __init__(self,settings):
        """初始化统计信息"""
        self.reset_game(settings)
        #游戏刚启动时处于非活动状态
        self.game_active = False
        self.game_stop = False
    def reset_game(self, settings):
        """初始化在游戏运行期间可能变化的统计信息"""
        self.ship_lifes = settings.ship_lifes
        self.ship_scores = settings.ship_scores
        self.bullet_damage = settings.bullet_damage
        self.bullet_line = settings.bullet_line
        self.rander_speed = settings.rander_speed
        self.hightest_ticks = settings.hightest_ticks
        self.hightest_FPS = settings.hightest_FPS