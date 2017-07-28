# -*- coding: utf-8 -*-
"""
Created on Thu Jul 20 09:54:29 2017

@author: lenovo
"""
import pygame
from setting import Setting
import game_functions as gf


def check_event():
    pygame.init()
    ai_setting = Setting()
    screen = pygame.display.set_mode(
            (ai_setting.screen_width,ai_setting.screen_height))
    pygame.display.set_caption("Check key input")
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                print(event.key)
            elif event.type == pygame.KEYUP:
                pygame.display.flip()
        gf.update_screen()
        
check_event()