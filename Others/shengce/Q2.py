n, k = map(int, input().strip().split())
nums = list(map(int, input().strip().split()))

# print(n, k, numbers)
res = []
"""
def dfs(memo, target, numbers):
    if len(memo) == 3 and sum(memo) == target:
        memo = sorted(memo)
        if memo not in res:
            res.append(memo)
        return
    elif len(memo) > 3:
        return

    for i in range(len(numbers)):
        memo.append(numbers[i])
        dfs(memo, target, numbers[:i]+numbers[i+1:])
        memo.pop()

dfs([], k, numbers)
"""

for i in range(len(nums) - 2):
    if i > 0 and nums[i] == nums[i - 1]:  # 过滤重复的
        continue
    l, r = i + 1, len(nums) - 1
    while l < r:
        # print(i,l,r)
        s = nums[i] + nums[l] + nums[r]
        if s < k:
            l += 1
        elif s > k:
            r -= 1
        else:
            res.append([nums[i], nums[l], nums[r]])
            while l < r and nums[l] == nums[l + 1]:
                l += 1
            while l < r and nums[r] == nums[r - 1]:
                r -= 1
            l += 1; r -= 1

if len(res) == 0:
    print("-1 -1 -1")
else:
    for i in range(len(res)):
        print(res[i][0], res[i][1], res[i][2])