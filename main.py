#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
main: 
1. read data from MSP430 using serial 
2. calculate array of vectors 
3. update animation 
"""
# import statements 
import pygame
from sys import exit
import serial 
import numpy as np 

# read port (information coming from MSP430)
# port = '/dev/tty.usbmodem11203'
x0 = np.array([])
y = 300 #cm 

# initiate pygame 
pygame.init() 
clock = pygame.time.Clock()

# set screen 
screen = pygame.display.set_mode((800, 400))
bg = pygame.Surface((800, 400)).convert()
bg.fill('White')
# eyeball = pygame.draw.circle(bg, 'azure2', (400, 200), 50)

# eye = pygame.image.load('/Users/dawnzheng/Desktop/39.png').convert_alpha()
# iris = pygame.image.load('/Users/dawnzheng/Desktop/iris3.png').convert_alpha()
# iris_rect = iris.get_rect(center = (400, 200))
# ey_rect = eye.get_rect(center = (400, 200)) 

# with serial.Serial(port,9600,timeout = 0.050) as ser:
#     print(ser.name)
    
# infinite loop
# unindent when activating the port reading 
while True: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            pygame.quit() 
            exit() 
    
    # get data from MSP430 
    # data = ser.read(1) 
    # if len(data) > 0: 
    #     distance = ord(data) 
    #     print(distance)
    #     theta = ((distance - x0) // y)
    
    # update surfaces 
    screen.blit(bg, (0,0))
    
    pygame.draw.circle(bg, 'azure2', (100, 100), 20)
    pygame.draw.circle(bg, 'azure2', (100, 200), 20)
    pygame.draw.circle(bg, 'azure2', (100, 300), 20)

    pygame.draw.circle(bg, 'azure2', (200, 100), 20)
    pygame.draw.circle(bg, 'azure2', (200, 200), 20)
    pygame.draw.circle(bg, 'azure2', (200, 300), 20)

    pygame.draw.circle(bg, 'azure2', (300, 100), 20)
    pygame.draw.circle(bg, 'azure2', (300, 200), 20)
    pygame.draw.circle(bg, 'azure2', (300, 300), 20)

    pygame.draw.circle(bg, 'azure2', (400, 100), 20)
    pygame.draw.circle(bg, 'azure2', (400, 200), 20)
    pygame.draw.circle(bg, 'azure2', (400, 300), 20)

    pygame.draw.circle(bg, 'azure2', (500, 100), 20)
    pygame.draw.circle(bg, 'azure2', (500, 200), 20)
    pygame.draw.circle(bg, 'azure2', (500, 300), 20)

    pygame.draw.circle(bg, 'azure2', (600, 100), 20)
    pygame.draw.circle(bg, 'azure2', (600, 200), 20)
    pygame.draw.circle(bg, 'azure2', (600, 300), 20)

    pygame.draw.circle(bg, 'azure2', (700, 100), 20)
    pygame.draw.circle(bg, 'azure2', (700, 200), 20)
    pygame.draw.circle(bg, 'azure2', (700, 300), 20)
    
    x = np.arctan((pygame.mouse.get_pos()[1] - 100) / 100)
    print(x)

    # pygame.draw.circle(bg, 'black', pygame.mouse.get_pos(), 5)
    # screen.blit(eye, ey_rect)
    # screen.blit(iris, iris_rect)

    # display screen         
    pygame.display.update() 
    clock.tick(60) 
