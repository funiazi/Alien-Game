# -*- coding: utf-8 -*-
"""
Created on Fri Jul 28 10:34:07 2017

@author: lenovo
"""

import pygame.font
from pygame.sprite import Group
from ship import Ship

class Scorebord():
    #显示得分类信息
    def __init__(self, ai_setting, screen, states):
        #初始化属性
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_setting = ai_setting
        self.states = states
        
        #显示得分时的字体
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)
        
        #准备得分图像
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()
        
    def prep_score(self):
        #将得分渲染为一幅图像
        round_score = round(self.states.score, -1)
        score_str = "{:,}".format(round_score)
        self.score_image = self.font.render(score_str, True, self.text_color,
                                            self.ai_setting.bg_color)
        
        #将得分放在右上角
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20
        
    def prep_high_score(self):
        #将最高得分渲染为图像
        high_score = round(self.states.high_score, -1)
        high_score_str = "{:,}".format(high_score)
        self.high_score_image = self.font.render(high_score_str, True, 
                                self.text_color, self.ai_setting.bg_color)
        
        #将最高分放在屏幕中央
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.screen_rect.top
        
    def prep_level(self):
        #将等级渲染为图像
        self.level_image = self.font.render(str(self.states.level), True,
                                self.text_color, self.ai_setting.bg_color)
        
        #将等级放在得分下方
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10
        
    def prep_ships(self):
        #显示剩余多少飞船
        self.ships = Group()
        for ship_number in range(self.states.ships_left):
            ship = Ship(self.ai_setting, self.screen)
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)            
        
    def show_score(self):
        #在屏幕上显示得分
        self.screen.blit(self.score_image,self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        #绘制飞船
        self.ships.draw(self.screen)