# -*- coding: utf-8 -*-
"""
Created on Wed Jul 19 13:45:48 2017

@author: lenovo
"""

import sys
import pygame
from bullet_ex import Bullet

#响应键按下事件
def check_down_event(event, ai_setting, screen, ship, bullets):
    '''if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left =True '''
    if event.key == pygame.K_UP:
        ship.moving_up = True
    elif event.key == pygame.K_DOWN:
        ship.moving_down = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_setting, screen, ship, bullets)
        
            
def fire_bullet(ai_setting, screen, ship, bullets):
    #创建一颗子弹并加入到bullets组中
    #检查是否达到弹药限制数
    if len(bullets) < ai_setting.bullets_allowed:
        new_bullet = Bullet(ai_setting, screen, ship)
        bullets.add(new_bullet)
        
#响应键升起事件
def check_up_event(ship,event):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False
    elif event.key == pygame.K_UP:
        ship.moving_up = False
    elif event.key == pygame.K_DOWN:
        ship.moving_down = False

def check_events(ai_setting, screen, ship, bullets):
    #响应事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            #根据按键设置移动标志
            check_down_event(event, ai_setting, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_up_event(ship,event) 
                
        
            
def update_screen(ai_setting,screen,ship, bullets):
    #循环时重绘屏幕
    screen.fill(ai_setting.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    pygame.display.flip()
    
def update_bullet(bullets):
    #更新子弹位置
    bullets.update()
        
    #删除消失的子弹
    for bullet in bullets.copy():
        if bullet.rect.left > 1200:
            bullets.remove(bullet)
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    