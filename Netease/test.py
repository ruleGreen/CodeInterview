a = [1,2,3]
b = a
b[:] = [x+1 for x in a]
print(a, b)
b = [x-1 for x in a]
print(a, b)

print(2.2 // 2)


array = [414, 574, 100, 684, 296, 666, 384, 772, 246, 946, 608, 786, 660, 862, 228, 500, 660, 304, 284, 578, 890, 234, 72, 261, 769, 864, 770, 750, 553, 7, 875, 367, 183, 57]
length = len(array)
count_4 = 0
count_2 = 0

for i in range(0, length):

    if array[i] % 4 == 0:
        count_4 += 1
    if array[i] % 2 == 0:
        count_2 += 1

res = 'No'
if length & 1 == 0:
    if count_4 >= (length - 1) // 2 + 1:
        res = "Yes"
    if count_2 - count_4 >= length - (count_4 * 2):
        res = "Yes"
else:
    if count_4 >= (length - 1) // 2:
        res = "Yes"
    if count_2 - count_4 >= length - (count_4 * 2):
        res = "Yes"
print(length, count_4, count_2, res)