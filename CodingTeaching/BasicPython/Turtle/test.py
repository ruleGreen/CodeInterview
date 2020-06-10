import turtle as t

"""
t.pu() # 抬笔
t.pd() # 落笔
t.forward(100) # 前进
t.right(90) # 右转90
t.forward(100)
t.left(90)
t.dot(10, 'red') # 点

t.pu()
t.goto(-100,100) # 去到(-100,100)
t.pd()
t.write("Ready Go") # 写
t.done() # done and save
"""

"""
t.pensize(3) # 改变笔画的大小
t.pencolor('orange') # 改变笔画的颜色
t.fillcolor('orange') # 选择填充的颜色
t.begin_fill() # 开始着色
t.circle(100) # 画一个圆
t.end_fill() # 结束着色
t.goto(-100,100)
t.circle(10, steps=5)
t.done()
"""
x = 8
y = 10
z = 12
t.speed(-1)
for i in range(5):
    for j in range(4):
        t.forward(x)
        x += 2
        t.right(90)
        t.forward(y)
        y += 2
        t.right(90)
        t.forward(z)
        z += 2
        t.right(90)

t.done()
