start = list(map(int, input().strip().split(":")))
through = list(map(int, input().strip().split(":")))

res = [0] * 3
# print(res)

if start[2] + through[2] <= 59:
    res[2] = start[2] + through[2]
else:
    res[2] = (start[2] + through[2]) % 60
    res[1] += (start[2] + through[2]) // 60

# print("1", res)

if start[1] + through[1] + res[1] <= 59:
    res[1] += start[1] + through[1]
else:
    res[1] = (start[1] + through[1] + res[1]) % 60
    res[0] += (start[1] + through[1] + res[1]) // 60

if start[0] + through[0] + res[0] <= 23:
    res[0] += start[0] + through[0]
else:
    res[0] = 0

# print(res)
if res[0] == 0:
    res[0] = '24'

print(":".join(str(res[i]) for i in range(len(res))))