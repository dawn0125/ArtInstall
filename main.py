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

# def getPosition():
#     # get data from MSP430 
#     data = ser.read(1) 
#     if len(data) > 0: 
#         distance = ord(data) 
#         print(distance)
#         theta = ((distance - x0) // y)
        
#     return theta 

# read port (information coming from MSP430)
# port = '/dev/tty.usbmodem11203'
x0 = np.array([])
xpos = np.arange(100, 800, 100)
ypos = np.arange(100, 400, 100)

# initiate pygame 
pygame.init() 
clock = pygame.time.Clock()

# set screen 
screen = pygame.display.set_mode((800, 400))
bg = pygame.Surface((800, 400)).convert()
bg.fill('White')

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
    
    # pos = getPosition()
    # an array of angles as seen by each eye (assuming that the mouse is 200 px outside the screen)
    iris_angle = np.arctan((pygame.mouse.get_pos()[0] - xpos) / 200)
    
    # update surfaces 
    screen.blit(bg, (0,0))

    i = 0
    for x in xpos:
        for y in ypos:
            pygame.draw.circle(bg, "azure2", (x, y), 20)
            pygame.draw.circle(bg, "black", (iris_angle[i] * x * 2 / np.pi, y),5)
        i += 1

    # pygame.draw.circle(bg, 'black', pygame.mouse.get_pos(), 5)
    # screen.blit(eye, ey_rect)
    # screen.blit(iris, iris_rect)

    # display screen         
    pygame.display.update() 
    clock.tick(60) 
