#coding:utf-8
import pygame.font
class Button(object):
    def __init__(self, settings, screen, location, rect_part=None):
        self.screen = screen
        self.settings = settings
        self.location = location
        self.rect_part = rect_part
        self.screen_rect = self.screen.get_rect()
    def draw_button(self):
        """绘制按钮"""
        self.screen.blit(self.image, self.rect)
class messageButton(Button):
    def __init__(self, settings, screen, location, msg, rect_part=None):
        """初始化按钮的属性"""
        super(messageButton, self).__init__(self, settings, screen, location, rect_part = None)
        self.prep(msg,  location, rect_part)
    def prep(self, msg, location, rect_part):
        """设置按钮的默认属性,并渲染按钮的图像"""
        #创建按钮图像(按钮的标签只需创建一次),并获取其rect属性
        self.button_color = self.settings.button_up_color
        self.text_color = self.settings.button_text_color
        self.font = pygame.font.SysFont(None, self.settings.button_font_size)
        self.image = self.font.render(msg, True, self.text_color)
        self.rect = self.image.get_rect()
        self.location = (self.screen_rect.centerx, self.screen_rect.centery * 5 / 4)
        #设置rect属性的默认部分
        if not rect_part:
            self.rect_part = self.rect.center
        self.rect_part = self.location
        self.width, self.height = self.rect.width, self.rect.height
        
    def draw_button(self):
        """绘制文本"""
        self.screen.blit(self.msg_image, self.msg_image_rect)
class imageBotton(Button):
    def __init__(self, settings, screen, location, image, rect_part=None):
        super().__init__()
        self.prep(image, location, rect_part)
    def prep(self, msg, image,location, rect_part):
        """设置按钮的默认属性,并渲染按钮的图像"""
        #创建按钮图像(按钮的标签只需创建一次),并获取其rect属性
        if msg:
            self.button_color = self.settings.button_up_color
            self.text_color = self.settings.button_text_color
            self.font = pygame.font.SysFont(None, self.settings.button_font_size)
            self.image = self.font.render(msg, True, self.text_color)
        elif image:
            self.image = image
        self.rect = self.image.get_rect()
        #设置默认位置
        if not location:
            self.location = (self.screen_rect.centerx, self.screen_rect.centery * 5 / 4)
        #设置rect属性的默认部分
        if not rect_part:
            self.rect_part = self.rect.center
        self.rect_part = self.location
        self.width, self.height = self.rect.width, self.rect.height