# -*- coding: utf-8 -*-
"""
Created on Tue Jul 25 12:15:44 2017

@author: lenovo
"""

import pygame
from pygame.sprite import Sprite

class Rain(Sprite):
    #表示雨滴的类
    
    def __init__(self, ai_setting, screen):
        super().__init__()
        self.screen = screen
        self.ai_setting = ai_setting
        
        #加载雨滴图像
        self.image = pygame.image.load('images/rain.bmp')
        self.rect = self.image.get_rect()
        
        #每个雨滴都到左上角
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        
        #储存雨滴准确位置
        self.y = float(self.rect.y)
        
    def update(self):
        self.y += self.ai_setting.alien_speed_factor
        self.rect.y = self.y