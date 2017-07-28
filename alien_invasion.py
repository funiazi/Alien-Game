# -*- coding: utf-8 -*-
"""
Created on Wed Jul 19 11:22:53 2017

@author: lenovo
"""

import pygame
from setting import Setting
from ship import Ship
from pygame.sprite import Group
import game_functions as gf
from game_states import Game_States
from button import Button
from scorebord import Scorebord


def run_game():
    #初始化一个屏幕对象
    pygame.init()
    ai_setting = Setting()
    screen = pygame.display.set_mode(
            (ai_setting.screen_width,ai_setting.screen_height))
    pygame.display.set_caption("Alien Invasion")
    
    
    #创建统计信息实例
    states = Game_States(ai_setting)
    sb = Scorebord(ai_setting, screen, states)
    
    #创建一艘飞船，一个外星人组类，一个子弹组类
    ship = Ship(ai_setting, screen)
    aliens = Group()
    bullets = Group()
    
    
    #创建外星人群
    gf.create_fleet(ai_setting, screen, aliens, ship)
    
    #创建开始按钮
    play_button = Button(ai_setting, screen, "Play")
    
    #游戏主循环
    while True:
        #监听鼠标和键盘
        gf.check_events(ai_setting, screen, sb, ship, aliens, bullets, states,
                        play_button)
        if states.game_active:
            ship.update()
            gf.update_bullet(ai_setting, screen, states, sb, ship,
                                  aliens, bullets)
            gf.update_aliens(ai_setting, states, screen, sb, ship, 
                             aliens, bullets)   
        gf.update_screen(ai_setting,screen,states, sb, ship, aliens, bullets,
                         play_button)
        

run_game()