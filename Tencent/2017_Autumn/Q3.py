"""
给定一个正整数，编写程序计算有多少对质数的和等于输入的这个正整数，并输出结果。输入值小于1000。
如，输入为10, 程序应该输出结果为2。（共有两对质数的和为10,分别为(5,5),(3,7)）
"""


def isPrimeNumber(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def getPrimeNumber(n):
    res = []
    for i in range(2, n):
        if isPrimeNumber(i):
            res.append(i)
    return res


n = int(input())
res = getPrimeNumber(n)
count = 0
for i in range(len(res)):
    if n - res[i] in res and n - res[i] <= n // 2:
        count += 1
print(count)