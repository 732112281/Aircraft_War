#coding:utf-8
import pygame.font
class Scoreboard():
    """显示得分信息的类"""
    
    def __init__(self, settings, screen, game_starts, bg_color=None):
        """初始化显示得分涉及的属性"""
        self.settings = settings
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.game_starts = game_starts
        self.bg_color = bg_color
        
        #显示得分信息时使用的字体设置
        self.text_color = settings.scoreboard_text_color
        font_kind = settings.button_font_kind
        font_size = settings.scoreboard_font_size
        self.font = pygame.font.SysFont(font_kind, font_size)
        
        #准备初始得分图像
        self.prep_score()
        
        #准备将生命值转换为图像
        self.ship_image = settings.ship_image
        self.ship_image_rect = self.ship_image.get_rect()
        self.prep_life()
        
    def prep_score(self, score_image_rect = None):
        """将得分转换为一幅渲染的图像"""
        #将得分圆整
        rounded_score = int(round(self.game_starts.scores, 0))
        score_str = "{:,}".format(rounded_score)
        #设置分数前文字
        if self.game_starts.game_active:
            title = 'SCORE:'
        else:
            title = ''
        #生成渲染图像
        score_image = self.font.render(title + score_str, True, 
                                            self.text_color, self.bg_color)
        #获取渲染图像的rect属性
        self.score_rect = score_image.get_rect()
        #根据游戏是否激活调整图像位置
        if not self.game_starts.game_active and score_image_rect:
            self.score_rect.midtop = score_image_rect.midbottom
        else:
            self.score_rect.topright = self.screen_rect.topright
        #将得分渲染在screen上
        self.screen.blit(score_image, self.score_rect)
        
    def prep_life(self):
        """将飞船生命值转换为可渲染的图像"""
        self.life_images = []
        for image_number in range(self.game_starts.lifes):
            self.life_images.append(self.ship_image_rect.width * image_number)
    
    def prep_hightest_score(self, hightest_score_image_rect):
        """将最高分转换为可渲染的图像"""
        #更新最高分，并将最高分放在screen左上角
        hightest_score = str(self.game_starts.hightest_score)
        hightest_score_image = self.font.render(hightest_score, 
                                    True, self.text_color, self.bg_color)
        hightest_score_rect = hightest_score_image.get_rect()
        hightest_score_rect.topleft = hightest_score_image_rect.topright
        self.screen.blit(hightest_score_image, hightest_score_rect)
        
            
    def draw(self):
        """在屏幕上显示得分"""
        #更新screen的rect属性
        self.screen_rect = self.screen.get_rect()
        #更新得分，并将得分放在screen右上角
        self.prep_score()
        #更新飞船生命值
        self.prep_life()
        #将飞船生命值放在screen左上角，并将飞船生命值渲染在screen上
        for life_image_x in self.life_images:
            self.screen.blit(self.ship_image, (life_image_x, 0))
        
        
        