# basic of python

print(ord('a'))     # 字符的ascii码
print(chr(ord('j') + 11 - 10))
print(bin(10))      # 数字的二进制

print({1, 4} | {1, 3})

number = list(map(int, input("Please input numbers: ").strip().split()))
print("{} is {}".format(10, 9))

# 基本数据结构
tu = tuple()

# 保留两位小数
print('%.2f' % 0.11223)



# lambda function
x = lambda x: x + 1
print(x(5))

x = [[1,2], [3,4], [5,6]]
x = sorted(x, key=lambda x: x[1])
print(x)

diction = {"A":1, "B":1, "C":2}
diction = sorted(diction.items(), key=lambda item: (item[1],item[0]))

print("diction", diction)

# random number
import random
num = random.randint(0,10)
print("num  is", num)

# 异或交换两个数
def switch(a, b):
    a = a ^ b
    b = a ^ b
    a = a ^ b
    return a, b

# Q1: 异或找出只出现一次的数字: 相同的数字异或为0，0与任何一个数异或还是这个数本身

# Q2: 找出重复数: 给定一个包含 n + 1 个整数的数组 nums，其数字都在 1 到 n 之间（包括 1 和 n），可知至少存在一个重复的整数。假设只有一个重复的整数，找出这个重复的数。
# 假设i是重复的那个数，则可以通过两次异或得到: 异或整个数组 异或1到n ->  (1^2^..^i^i^..^n)    ^  (1^2^3...^n) = i


