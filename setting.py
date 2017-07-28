# -*- coding: utf-8 -*-
"""
Created on Wed Jul 19 12:02:20 2017

@author: lenovo
"""

class Setting():
    #储存游戏的设置信息
    
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230,230,230)
        
        #飞船静态设置
        self.ship_limit = 3
        
        #子弹静态设置      
        self.bullet_width = 300
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3
        
        #外星人静态设置
        self.fleet_drop_speed = 10
        
        #游戏节奏
        self.speedup_scale = 1.1
        self.score_scale = 1.5
        self.initialize_dynamic_setting()
        
    def initialize_dynamic_setting(self):
        #初始化随时间变化的设置
        self.ship_speed_factor = 1.5
        self.alien_speed_factor = 1
        self.bullet_speed_factor = 1
        self.alien_point = 50
        #fleet_direction为1表示右移，-1表示左移
        self.fleet_direction = 1
        
    def increase_speed(self):
        #提高速度设置
        self.ship_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_point = int(self.alien_point * self.score_scale)
        