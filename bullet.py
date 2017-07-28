# -*- coding: utf-8 -*-
"""
Created on Thu Jul 20 14:04:06 2017

@author: lenovo
"""

import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    #管理子弹类
    
    def __init__(self,ai_setting, screen, ship):
        #在飞船处创建一个子弹对象
        super().__init__()
        self.screen = screen
        
        #在0，0 处创建子弹，并移到正确的位置
        self.rect = pygame.Rect(0, 0, ai_setting.bullet_width,
                                 ai_setting.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        
        #小数点储存位置
        self.y = float(self.rect.y)
        
        self.color = ai_setting.bullet_color
        self.speed_factor = ai_setting.bullet_speed_factor
        
    def update(self):
        #向上移动子弹
        self.y -= self.speed_factor
        #更新子弹位置
        self.rect.y = self.y
        
    def draw_bullet(self):
        #绘制子弹
        pygame.draw.rect(self.screen, self.color, self.rect)