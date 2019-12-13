string = input()
number = int(input())

# print(string, number)
# print(ord('a')) 97
string = list(string)
length = 0
for i in range(len(string)):
    num = 0
    for j in range(i, len(string)):
        num += ord(string[j]) - ord('a') + 1
        # print(j, i, string, num)
        if num == number:
            length = max(length, j - i + 1)

print(length)