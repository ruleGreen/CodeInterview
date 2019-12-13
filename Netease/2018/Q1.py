n = int(input())
# machine1: 2 * n + 1
# machine2: 2 * n + 2

if n == 1:
    print('1')
elif n == 2:
    print('2')

res = ""

while n > 0:
    if n & 1 == 0:
        # num is even
        n = (n - 2) // 2
        res = "2" + res
    else:
        n = (n - 1) // 2
        res = "1" + res
print(res)
