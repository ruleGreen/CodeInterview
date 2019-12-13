n = int(input())

# build corrdinate
corr_x, corr_y = [], []
for _ in range(n):
    x, y = map(int, input().strip().split())
    corr_x.append(x)
    corr_y.append(y)

flag = True
res = []
for i in range(len(corr_x)):
    for j in range(len(corr_x)):
        if corr_x[j] > corr_x[i] and corr_y[j] > corr_y[i]:
            flag = False
    if flag:
        res.append([corr_x[i], corr_y[i]])
    flag = True


res = sorted(res)
# print(res)

for i in range(len(res)):
    print(res[i][0], res[i][1])