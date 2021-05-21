# -*- coding: utf-8 -*-
"""
Created on Fri May 21 11:04:52 2021

@author: Shourabh Verma
"""

# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pygame, sys

pygame.init()
clock=pygame.time.Clock()

screen = pygame.display.set_mode((400,600))

#creating objects of game
player=pygame.Rect(200,500,30,30)
playerspeed=-4
enemy=pygame.Rect(70,50,40,40)
enemyspeed= -2;

while True:    
    screen.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
         
    enemy.x= enemy.x + enemyspeed
    
    
    if enemy.x == 0:
        enemyspeed=enemyspeed * -1
        enemy.y= enemy.y + 20
    
    if enemy.x == 380:
        enemyspeed=enemyspeed * -1
        enemy.y= enemy.y + 20
    
    player.y=player.y+playerspeed
           
    pygame.draw.rect(screen,(123,200,100),enemy)
    pygame.draw.rect(screen,(23,100,100),player)
    
    
    pygame.display.update()
    clock.tick(30)



 
    
   