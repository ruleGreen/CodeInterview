# 26 November 2019
# author: Wang Hongru

# stack
# 1. 递归
# 2. 深度优先搜索
# 3. 模拟函数调用
# 4. 栈在表达式求值的应用 34+15*9-6 (一个数据栈，一个操作符栈) 浏览器的前进后退问题也可以使用两个栈的实现，还可以用两个栈模拟优先队列的实现方式

# 内存中的堆栈和数据结构堆栈不是一个概念，可以说内存中的堆栈是真实存在的物理区，数据结构中的堆栈是抽象的数据存储结构。
# 内存空间在逻辑上分为三部分：代码区、静态数据区和动态数据区，动态数据区又分为栈区和堆区。
# 代码区：存储方法体的二进制代码。高级调度（作业调度）、中级调度（内存调度）、低级调度（进程调度）控制代码区执行代码的切换。
# 静态数据区：存储全局变量、静态变量、常量，常量包括final修饰的常量和String常量。系统自动分配和回收。
# 栈区：存储运行方法的形参、局部变量、返回值。由系统自动分配和回收。
# 堆区：new一个对象的引用或地址存储在栈区，指向该对象存储在堆区中的真实数据

# References
#

class ArrayStack(object):
    def __init__(self, n):
        self.n = n
        self.count = 0
        self.stack = [None] * n

    def push(self, element):
        if self.count == self.n:
            return False
        else:
            self.stack[self.count] = element
            self.count += 1
        return True

    def pop(self):
        if self.count == 0:
            return False
        else:
            res = self.stack[self.count]
            self.count -= 1
        return res


