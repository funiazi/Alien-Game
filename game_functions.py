# -*- coding: utf-8 -*-
"""
Created on Wed Jul 19 13:45:48 2017

@author: lenovo
"""

import sys
import pygame
from time import sleep
from bullet import Bullet
from alien import Alien


#响应键按下事件
def check_down_event(event, ai_setting, screen, sb, ship, bullets, states, aliens):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left =True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_setting, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()
    elif event.key == pygame.K_p:
        start_game(ai_setting, states, screen, sb, ship, bullets, aliens)
        
            
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


def check_events(ai_setting, screen, sb, ship, aliens, bullets, states ,play_button):
    #响应事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            #根据按键设置移动标志
            check_down_event(event, ai_setting, screen, sb, ship, bullets, 
                             states, aliens)
        elif event.type == pygame.KEYUP:
            check_up_event(ship,event) 
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_setting, states, screen, sb, ship, bullets, 
                              aliens, play_button, mouse_x, mouse_y)
            
def check_play_button(ai_setting, states, screen, sb, ship, bullets, aliens, 
                      play_button, mouse_x, mouse_y):
    #玩家点击按钮时开始游戏
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not states.game_active:
        ai_setting.initialize_dynamic_setting()
        start_game(ai_setting, states, screen, sb, ship, bullets, aliens)
        
        
def start_game(ai_setting, states, screen, sb, ship, bullets, aliens):
    #按下按钮重置统计信息
    states.reset_states()
    states.game_active = True
    
    #重置记分牌
    sb.prep_score()
    sb.prep_high_score()
    sb.prep_level()
    sb.prep_ships()
    
    #隐藏光标
    pygame.mouse.set_visible(False)
       
    #清空子弹和外星人
    aliens.empty()
    bullets.empty()
        
    #创建新的外星人，并让飞船居中
    create_fleet(ai_setting, screen, aliens, ship)
    ship.center_ship()
        
            
def update_screen(ai_setting,screen,states, sb, ship, aliens, bullets,
                         play_button):
    #循环时重绘屏幕
    screen.fill(ai_setting.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)
    
    #显示得分
    sb.show_score()
    
    #如果处于非活跃时，绘制开始按钮
    if not states.game_active:
        play_button.draw_button()
    
    pygame.display.flip()
    
def update_bullet(ai_setting, screen, states, sb, ship,
                                  aliens, bullets):
    #更新子弹位置
    bullets.update()
        
    #删除消失的子弹
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
            
    check_bullet_alien_collisions(ai_setting, screen, states, sb, ship,
                                  aliens, bullets)
    
    
def check_bullet_alien_collisions(ai_setting, screen, states, sb, ship,
                                  aliens, bullets):
    #检查是否有子弹击中外星人，有就两个都删除
    collisions = pygame.sprite.groupcollide(bullets,aliens,True,True)
    
    if collisions:
        for aliens in collisions.values():
            states.score += ai_setting.alien_point * len(aliens)
            sb.prep_score()
        check_high_score(states, sb)
        
    #检查外星人是否为零，加快游戏节奏，重新生成外星人
    if len(aliens) == 0:
        bullets.empty()
        ai_setting.increase_speed()
        
        #消灭一群外星人后等级提升
        states.level += 1
        sb.prep_level()
        
        create_fleet(ai_setting, screen, aliens, ship)
            
def check_high_score(states,sb):
    #检查是否出现最高分
    if states.score > states.high_score:
        states.high_score = states.score
        sb.prep_high_score()
        

def get_number_aliens_x(ai_setting,alien_width):
    #计算能容纳多少外星人
    available_space_x = ai_setting.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x
        
def get_number_aliens_row(ai_setting,ship_height,alien_height):
    #计算能容纳多少行外星人
    available_space_y = (ai_setting.screen_height -
                           (3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows

def create_alien(ai_setting,screen,aliens, alien_number, row_number):
    #创建一个外星人并设间距为外星人宽度
    #放置在当前行
    alien = Alien(ai_setting, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + alien_width * 2 * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)

def create_fleet(ai_setting, screen, aliens,ship):
    '''创建外星人'''
    #创建第一行外星人
    alien = Alien(ai_setting, screen)
    number_aliens_x = get_number_aliens_x(ai_setting,alien.rect.width)
    number_rows = get_number_aliens_row(ai_setting,ship.rect.height,
                                        alien.rect.height)
    
    #创建外星人群
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(ai_setting, screen, aliens, alien_number,
                         row_number)
     
def check_fleet_edges(ai_setting,aliens):
    #检测外星人是否到达边界，并动作
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_setting,aliens)
            break
        
def change_fleet_direction(ai_setting, aliens):
    #将外星人整个向下移动，并改变运动方向
    for alien in aliens.sprites():
        alien.rect.y += ai_setting.fleet_drop_speed
    ai_setting.fleet_direction *= -1
    
    
#飞船到达屏幕底部
def check_alien_bottom(ai_setting, states, screen, sb, ship, aliens, bullets):
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            #做出如同碰撞的动作
            ship_hit(ai_setting, states, screen, sb, ship, aliens, bullets)
            break
            

def ship_hit(ai_setting, states, screen, sb, ship, aliens, bullets):
    '''响应被外星人撞到飞船'''
    #将飞船数量减一
    if states.ships_left > 0 :
        states.ships_left -= 1
        
        #更新剩余飞船数
        sb.prep_ships()

        #清空外星人和子弹列表
        aliens.empty()
        bullets.empty()
    
        #创建新的外星人并放到屏幕底
        create_fleet(ai_setting,screen,aliens,ship)
        ship.center_ship()
    
        #暂停
        sleep(0.5)
    
    else:
        pygame.mouse.set_visible(True)
        states.game_active = False
    
    
def update_aliens(ai_setting, states, screen, sb, ship, 
                             aliens, bullets):
    #更新外星人群的位置
    check_fleet_edges(ai_setting, aliens)
    aliens.update()        
    
    #检测飞船与外星人的碰撞
    if pygame.sprite.spritecollideany(ship,aliens):
        ship_hit(ai_setting, states, screen, sb, ship, aliens, bullets)
    
    check_alien_bottom(ai_setting, states, screen, sb, ship, aliens, bullets)
    