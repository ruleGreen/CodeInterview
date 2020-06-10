import turtle as t

"""
t.pu() # 抬笔
t.goto(-300, 300) # 把笔移动到某个位置
t.pd() # 落笔
t.write("Ready!!!")
t.pu()
t.goto(0,0)
t.pd()
t.pensize(3) # 改变笔画的大小
t.pencolor('orange') # 改变笔画的颜色
t.forward(100) # 前进100
t.right(90) # 右转90
t.forward(80)
t.left(90) # 左转90
t.forward(100)
t.done() # done and save
"""
"""
t.pensize(3)
t.pencolor('red')
t.dot(10, 'blue') # 画一个点
t.forward(100)
t.fillcolor('green') # 填充的颜色
t.begin_fill() # 开始着色
t.circle(80)
t.end_fill() # 结束着色
t.right(90)
t.forward(50)
t.circle(80, steps=3)
t.forward(30)
t.circle(80, steps=5)
t.done()
"""

# for i in range(10)
# while True
x = 8
y = 10
z = 12
t.speed(-1)
for i in range(5):
    for j in range(4):
        t.forward(x)
        x = x + 2
        t.right(90)
        t.forward(y)
        y += 2
        t.right(90)
        t.forward(z)
        z += 2
        t.right(90)
t.done()