x = [0, 1, 2, 3, 4, 5, 6]

res_h1, res_h2, res_h3 = [], [], []
for i in range(0, len(x)):
    h1 = 2 * x[i] + 1 % 11
    h2 = 3 * x[i] + 2 % 10
    h3 = 5 * x[i] + 2 % 6
    res_h1.append(h1)
    res_h2.append(h2)
    res_h3.append(h3)

print(res_h1, res_h2, res_h3)


res_h1 = [res_h1[i] % 7 for i in range(len(res_h1))]
res_h2 = [res_h2[i] % 7 for i in range(len(res_h2))]
res_h3 = [res_h3[i] % 7 for i in range(len(res_h3))]

print("AFTER MOD N:")
print(res_h1, res_h2, res_h3)