# -*- coding: utf-8 -*-
"""
Created on Tue Jul 25 11:59:21 2017

@author: lenovo
"""

import pygame
from setting import Setting
from pygame.sprite import Group
import game_functions as gf

def run():
    pygame.init()
    ai_setting = Setting()
    screen = pygame.display.set_mode((
            ai_setting.screen_width, ai_setting.screen_height))
    pygame.display.set_caption("Rain Drop")
    
    rains = Group()
    
    gf.create_rain_fleet(ai_setting, screen, rains)
    
    while True:
        #监听鼠标和键盘
        gf.update_rains(ai_setting, rains)
        gf.update_rain_screen(ai_setting,screen,rains)
        

run()
    
    