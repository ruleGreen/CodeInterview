# Copyright: WANG Hongru
import turtle as t

t.pu() # 抬笔
t.goto(-300,300)
t.write("Ready Go?", font=80)

t.goto(0,0)

t.dot(10) # 绘制点
t.dot(20, "black") # 绘制黑色的点
t.seth(60) # 设置画笔的角度
t.forward(100)

t.pd() # 落笔
t.colormode(255) # 颜色模式
t.pensize(3) # 笔画大小
t.fillcolor(3,4,5)
t.begin_fill()
t.circle(30, steps=3)
t.end_fill()

t.forward(100) # fd()
t.backward(100) # back() bk()
t.right(90) # angle 90
t.forward(60)
t.left(90) # angle 90
t.forward(80)

t.done() # done and save