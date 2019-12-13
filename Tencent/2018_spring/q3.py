# Question3
import math
n, m = map(int, input().strip().split())

# method one: brute force
# n 50000 m 100000
"""
if n > m:
    print(0)
elif n == m:
    print(1)
else:
    upper = m - n
    start = 1
    res = [_ for _ in range(n)]
    while start <= upper:
        res[0] = start
        for j in range(1, n):
            if res[j-1] == 1:
                res[j:] = [1 for _ in range(j, n)]
                break
            else:
                res[j] = math.ceil(res[j - 1] / 2)
        if sum(res) <= m:
            start += 1
        else:
            break

    print(start - 1)
"""

# binary search
if n > m:
    print(0)
elif n == m:
    print(1)
elif n == 1:
    print(m)
else:
    upper = m - n
    start = 1
    res = [_ for _ in range(n)]
    while start <= upper:
        mid = start + (upper - start) // 2
        res[0] = mid
        for j in range(1, n):
            if res[j-1] == 1:
                res[j:] = [1 for _ in range(j, n)]
                break
            else:
                res[j] = math.ceil(res[j - 1] / 2)
        if sum(res) < m:
            start = mid + 1
        elif sum(res) == m:
            print(mid)
            break
        else:
            upper = mid - 1

    print(start - 1)