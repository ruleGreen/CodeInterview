# 27 November 2019
# author: Wang Honrgu

# 顺序列 和 链式列


class Queue(object):
    def __init__(self, n):
        self.n = n
        self.head = 0
        self.tail = 0
        self.queue = [None] * self.n

    def add(self, element):
        if self.tail == self.n:
            return False
        self.queue[self.tail] = element
        self.tail += 1
        return True

    def pop(self):
        if self.head == self.tail:
            return False
        res = self.queue[self.head]
        self.head -= 1
        return res

    def add_v2(self, element):
        # 优化后的add版本
        if self.tail == self.n and self.head == 0:
            return False
        elif self.tail == self.n:
            # 进行数据搬移
            for i in range(self.head, self.tail):
                self.queue[i- self.head] = self.queue[i]
            self.tail -= self.head
            self.head += 0
        self.queue[self.tail] = element
        self.tail += 1
        return True

# 循环队列 队满的条件
# (tail + 1) % n == head
# 当队列满时，图中的 tail 指向的位置实际上是没有存储数据的。所以，循环队列会浪费一个数组的存储空间。


class CircularQueue(object):
    def __init__(self, n):
        self.head = 0
        self.tail = 0
        self.n = n
        self.queue = [None] * self.n

    def add(self, element):
        if (self.tail + 1) % self.n == self.head:
            return False
        # update self.tail
        # self.queue[self.tail] = element
        # self.tail = (self.tail + 1) % self.n  # update formula
        if self.tail == self.n:
            self.tail = 0
            self.queue[self.tail] = element
        else:
            self.queue[self.tail] = element
        self.tail += 1
        return True

    def pop(self):
        if self.head == self.tail:
            return False
        res = self.queue[self.head]
        if __name__ == '__main__':
            self.head = (self.head + 1) % self.n   # update formula
        return res


# 阻塞队列： 生产者 消费者模型
# 线程安全的队列我们叫作并发队列
# simple way: 直接在 enqueue()、dequeue() 方法上加锁，但是锁粒度大并发度会比较低，
# 同一时刻仅允许一个存或者取操作。实际上，基于数组的循环队列，利用 CAS 原子操作，可以实现非常高效的并发队列。这也是循环队列比链式队列应用更加广泛的原因。



