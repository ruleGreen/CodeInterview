# Copyright: WANG Hongru
import sys
import pygame
from pygame.locals import QUIT
# pygame.Surface surface类型，代表一个矩形的影像
# pygame.Rect rect类型，用来定位矩形空间的位置和可以用来侦测物件是否是碰撞的
# pygame.event 事件
# pygame.font 文字
# pygame.draw 绘图
# pygame.image 图片
# pygame.time 时间


pygame.init() # 初始化游戏模块
window_surface = pygame.display.set_mode((800,600)) # 建立windows视窗画布，大小为800 * 600
pygame.display.set_caption("Hello world!") # 设置视窗标题是hello world!
window_surface.fill((230,255,255)) # 清除桌面并填满背景色

head_font = pygame.font.SysFont(None, 60) # 设置font
text_surface = head_font.render('Hello world!', True, (0,0,0)) # 渲染 回传surface物件
window_surface.blit(text_surface, (10,10)) # blit 用来把其他元素渲染到另外一个surface上，这里是window视窗

pygame.display.update() # 更新界面，等所有操作完成后一次性更新(如果没有更新，则元素不会出现)

"""
while True:
    # 迭代整个事件 如有符合事件则对应处理
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
"""