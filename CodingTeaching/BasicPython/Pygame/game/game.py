# Copyright WANG Hongru
import sys
import pygame
from pygame.locals import QUIT

bg_jpg = "bg.jpg"
star_jpg = "stars.jpg"

pygame.init() # 初始化
screen = pygame.display.set_mode((800,600), 0, 32)
pygame.display.set_caption("Hello world!")

bg = pygame.image.load(bg_jpg).convert()
stars = pygame.image.load(star_jpg).convert_alpha()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()

    screen.blit(bg, (0,0))

    x,y = pygame.mouse.get_pos()   # 获得鼠标位置
    x -= stars.get_width() / 2
    y -= stars.get_height() / 2

    screen.blit(stars, (x,y))

    pygame.display.update()