# Question 4
K = int(input())
A, numA, B, numB = map(int, input().strip().split())

import math

def combine(num, n):
    if n == 0 or n == num:
        return 1
    up = 1
    for i in range(num, num - n, -1):
        up = up * i
    return up // math.factorial(n)

print(K)
print(A, numA, B, numB)

res = 0
for x in range(0, (K // A) + 1):
    y = (K - x * A) // B
    if K == x*A + y*B:
        res += combine(numA, x) * combine(numB, y)

print(res % 1)