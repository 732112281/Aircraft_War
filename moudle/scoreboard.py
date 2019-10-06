#coding:utf-8
import pygame.font
class Scoreboard():
    """显示得分信息的类"""
    
    def __init__(self, settings, screen, game_starts, bg_color=None):
        """初始化显示得分涉及的属性"""
        self.settings = settings
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.starts = game_starts
        self.bg_color = bg_color
        
        #显示得分信息时使用的字体设置
        self.text_color = settings.scoreboard_text_color
        font_kind = settings.button_font_kind
        font_size = settings.scoreboard_font_size
        self.font = pygame.font.SysFont(font_kind, font_size)
        
        #准备初始得分图像
        self.prep_score()
        self.score_rect = self.score_image.get_rect()
    def prep_score(self):
        """将得分转换为一幅渲染的图像"""
        score_str = str(self.starts.scores)
        self.score_image = self.font.render('SCORE:' + score_str, True, 
                                            self.text_color, self.bg_color)
    def draw(self):
        """在屏幕上显示得分"""
        #将得分放在屏幕右上角
        self.score_rect = self.score_image.get_rect()
        self.screen_rect = self.screen.get_rect()
        self.score_rect.topright = self.screen_rect.topright
        self.screen.blit(self.score_image, self.score_rect)
        
        