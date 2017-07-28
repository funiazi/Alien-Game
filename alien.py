# -*- coding: utf-8 -*-
"""
Created on Fri Jul 21 09:57:59 2017

@author: lenovo
"""

import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    #表示单个外星人的类
    
    def __init__(self, ai_setting, screen):
        #初始化外星人并放置到起始位置
        super().__init__()
        self.screen = screen
        self.ai_setting = ai_setting
        
        #加载外星人图像，设置rect属性
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()
        
        #每个外星人都到左上角
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        
        #储存外星人准确位置
        self.x = float(self.rect.x)
        
    def blitme(self):
        #在指定位置绘制外星人
        self.screen.blit(self.image, self.rect)
        
    def check_edges(self):
        #如果外星人位于边缘则返回 True
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    #向左或右移动外星人
    def update(self):
        self.x += (self.ai_setting.alien_speed_factor *
                   self.ai_setting.fleet_direction)
        self.rect.x = self.x
               
        
        
        