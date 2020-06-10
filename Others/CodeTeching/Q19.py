# Carrey Wong
# 2020 05 27

import random
import matplotlib.pyplot as plt

# minimum 3 maximum 18 max 3*18 = 54 min 3*3=9
res = {}

def roll_dice():
    dice_num = random.randint(3, 18)
    return dice_num

total = 1000
roll = []
for i in range(total):
    one = roll_dice()
    two = roll_dice()
    three = roll_dice()
    result = one + two + three
    roll.append(result)
    if result in res:
        res[result] += 1
    else:
        res[result] = 1

x = list(res.keys())
y = list(res.values())
plt.xlabel("点数")
plt.ylabel("次数")
plt.hist(roll, bins=range(9, 54))
plt.show()
