#coding:utf-8
import pygame.font
class Button(object):
    """有关按钮的类"""
    
    def __init__(self, settings, screen, ID, active_blit=False, stop_blit=True, \
                 msg=None, up_bg_color=None, down_bg_color=None, bg_size=None,
                 up_image=None, down_image=None, ):
        """初始化与按钮有关的属性"""
        self.screen = screen
        self.settings = settings
        self.screen_rect = self.screen.get_rect()
        self.active_blit = active_blit
        self.stop_blit = stop_blit
        self.msg = msg
        self.up_bg_color = up_bg_color
        self.down_bg_color = down_bg_color
        self.bg_size = bg_size
        self.up_image = up_image
        self.down_image = down_image
        self.ID = ID
        #初始化各项属性
        self.init()
    def init(self):
        """初始化各项属性"""
        if self.up_image or self.down_image:
            if not self.up_image and self.down_image:
                self.image = self.down_image
            else:
                self.image = self.up_image
            self.image_rect = self.image.get_rect()
        else:
            self.image = None
        if self.msg:
            text_color = self.settings.button_text_color
            text_kind = self.settings.button_font_kind
            text_size = self.settings.button_font_size
            font = pygame.font.SysFont(text_kind, text_size)
            self.up_msg_image = font.render(self.msg, True, 
                                         text_color, self.up_bg_color)
            if self.down_bg_color:
                self.down_msg_image = font.render(self.msg, True, 
                                         text_color, self.down_bg_color)
            else:
                self.down_msg_image = None
            if self.down_msg_image and not self.up_msg_image:
                self.msg_image = self.down_msg_image
            else:
                self.msg_image = self.up_msg_image
            self.msg_rect = self.up_msg_image.get_rect()
            try:
                if (self.up_bg_color or self.down_bg_color) and len(self.bg_size) == 2:
                    self.bg_rect = pygame.Rect(0, 0, self.bg_size[0], 
                                               self.bg_size[1])
                else:
                    self.bg_rect = self.msg_rect
            except TypeError:
                self.bg_rect = self.msg_rect
            
            try:
                if self.bg_color and len(self.bg_size) == 2:
                    if self.msg_rect.height < self.bg_rect.height and \
                        self.msg_rect.width < self.bg_rect.width:
                        self.msg_rect = self.bg_rect
            except AttributeError:
                pass
        try:
            if self.down_msg_image == None:
                pass
        except AttributeError:
            self.down_msg_image = None
        self.set_rect()
        
    def set_rect(self):
        """设置button对象的rect属性"""
        if self.msg and self.image:
            if self.msg_rect.height > self.image_rect.height and \
                self.msg_rect.width > self.image_rect.width:
                self.rect = self.msg_rect
            else:
                self.rect = self.image_rect
            self.image_rect.center = self.msg_rect.center
        elif self.msg and not self.image:
            self.rect = self.msg_rect
        elif self.image and not self.msg:
            self.rect = self.image_rect 
            
    def change_image(self, button_down):
        """button对象被按下时切换图片"""
        if button_down:
            if not (self.up_bg_color or self.down_bg_color):
                self.image = self.down_image
            elif self.down_bg_color:
                self.msg_image = self.down_msg_image
        else:
            if not (self.up_bg_color or self.down_bg_color):
                self.image = self.up_image
            elif self.down_bg_color:
                self.msg_image = self.up_msg_image
                
    def update(self, score_rect):
        """设置button对象的位置"""
        self.screen_rect = self.screen.get_rect()
        if self.ID == 0:
            self.rect.centerx = self.screen_rect.centerx
            self.rect.centery = self.screen_rect.centery * 5/4
        elif self.ID == 1:
            self.rect.topright = score_rect.bottomright
        elif self.ID == 2:
            self.rect.topright = score_rect.bottomright
        
    def draw(self, score_rect):
        """绘制按钮"""
        self.update(score_rect)
        if self.image and not self.msg:
            self.screen.blit(self.image, self.image_rect)
        elif self.msg and not self.image:
            self.screen.blit(self.msg_image, self.msg_rect)
        elif self.msg and self.image:
            if not (self.up_bg_color or self.down_bg_color):
                self.screen.blit(self.image, self.image_rect)
                self.screen.blit(self.msg_image, self.msg_rect)
            else:
                self.screen.blit(self.msg_image, self.msg_rect)