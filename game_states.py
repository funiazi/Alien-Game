# -*- coding: utf-8 -*-
"""
Created on Wed Jul 26 11:46:30 2017

@author: lenovo
"""

class Game_States():
    '''跟踪游戏统计信息'''
    
    def __init__(self, ai_setting):
        #初始化统计信息
        self.ai_setting = ai_setting
        self.reset_states()
        
        #让游戏一开始处于非活跃状态
        self.game_active = False
        
        #不重置最高得分
        self.high_score = 0
        
    def reset_states(self):
        self.ships_left = self.ai_setting.ship_limit
        self.score = 0
        self.level = 1