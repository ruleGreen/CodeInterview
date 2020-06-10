import os
# basic of python

print(ord('a'))     # 字符的ascii码
print(chr(ord('j') + 11 - 10))
print(bin(10))      # 数字的二进制

# file and directory
base_dir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
print(base_dir)

# //  vs /
print(5 / 2)
print(5 // 2)
print(1 // 26)

#
print(10^9)  # 异或
print(10**9)

#
print(list(zip([1,2], [3,4], [5,6], [7,8])))
print([1,3] + [4,5])
a_list = [1,4]
a_list += [3]
print(a_list)

# init the list
stack = list()
stack_1 = [0] * 8
stack_2 = [0 * 8]
stack_3 = [[0] * 8]
print(stack_1, stack_2, stack_3)
stack_1[0] = 1
print(stack_1)
cands = [[]] * 3
print(cands)

# middle of list
print(6 // 2)
print(5 // 2)

# 求两者的并集
print({1, 4} | {1, 3})

# 基本数据结构
# tuple
tuple = ("apple", "banana", "cherry")
print(tuple[1])

# dict
import collections
dict = collections.Counter("abscdcfsd")

def isAnagram1(s, t):
    dict1, dict2 = {}, {}
    for item in s:
        dict1[item] = dict1.get(item, 0) + 1
    for item in t:
        dict2[item] = dict2.get(item, 0) + 1
    return dict1 == dict2

def isAnagram2(s, t):
    dict1, dict2 = [0]*26, [0]*26
    for item in s:
        dict1[ord(item) - ord('a')] += 1
    for item in t:
        dict2[ord(item) - ord('a')] += 1
    return dict1 == dict2

print(isAnagram1("cat", "tac"))

# 输入输出的格式处理
number = list(map(int, input("Please input numbers: ").strip().split()))
print("{} is {}".format(10, 9))

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


# python 判断变量是否是int 字符串 列表 元组 字典的办法
a = 1
b = [1,2,3,4]
c = (1,2,3,4)
d = {"A":1,"B":2,"C":3,"D":4}
e = "abc"

if isinstance(a, int):
    print("a's type is int")
else:
    print("a is not int")
if isinstance(b, list):
    print("b's type is list")
else:
    print("b is not list")
if isinstance(e, str):
    print("e's type is str")
else:
    print("e is not str")

print(sorted([1,3,2,4]))