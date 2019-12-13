# Question2
n = int(input())
nums = list(map(int, input().strip().split()))
nums = sorted(nums, reverse=True)
if len(nums) == 0:
    print(0)
niuniu, sheep = 0, 0
for i in range(len(nums)):
    if i & 1 == 0:
        niuniu += nums[i]
    else:
        sheep += nums[i]

print(niuniu - sheep)