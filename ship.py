# -*- coding: utf-8 -*-
"""
Created on Wed Jul 19 12:13:20 2017

@author: lenovo
"""
import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    
    def __init__(self,ai_setting, screen):
        #初始化飞船并设置在初始位置
        super().__init__()
        self.screen = screen
        self.ai_setting = ai_setting
        
        
        #将飞船放在底部
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        
        #在center中储存小数值
        self.center = float(self.rect.centerx)
        self.row = float(self.rect.centery)
        
        #移动标志
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
        
    def update(self):
        #根据标志飞到相应位置
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_setting.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_setting.ship_speed_factor
        if self.moving_up and self.rect.top > 0:
            self.row -= self.ai_setting.ship_speed_factor
        if self.moving_down and (self.rect.top + 
                self.rect.height) < self.screen_rect.height:
            self.row += self.ai_setting.ship_speed_factor
            
        #更新位置
        self.rect.centerx = self.center
        self.rect.centery = self.row
    
    def center_ship(self):
        #让飞船在屏幕居中
        self.center = self.screen_rect.centerx
    
    def blitme(self):
        #在指定位置设置飞船
        self.screen.blit(self.image,self.rect)