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
        
        #飞船速度设置
        self.ship_speed_factor = 1.5
        
        #子弹设置
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3