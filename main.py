#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 13:25:39 2024

@author: dawnzheng
"""

import pygame
from sys import exit

# initiate pygame 
pygame.init() 
clock = pygame.time.Clock()


# set screen 
screen = pygame.display.set_mode((800, 400))
bg = pygame.Surface((800, 400)).convert()
bg.fill('White')

# infinite loop
while True: 
    for event in pygame.event.get():
        
        # if x out of game window, stop running code 
        if event.type == pygame.QUIT: 
            pygame.quit() 
            exit() 
         
    # update surfaces 
    
    screen.blit(bg, (0,0))

    # display screen         
    pygame.display.update() 
    clock.tick(60) 
