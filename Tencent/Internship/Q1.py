# DP 集锦

"""
给定一个整数数组[a1,a2,.....aN] ，N个数,  现在从里面选择若干数使得他们的和最大，同时满足相邻两数不能同时被选， a1和aN首尾两个也认为是相邻的。
"""
"""
leetcode 扎气球问题
"""
class Solution:
    def __init__(self, numbers):
        self.numbers = numbers

    def chooseMax(self):
        self.res = []
        self.dfs([], self.numbers)
        return self.res

    def dfs(self, memo, numbers):
        if sum(memo) > sum(self.res):
            self.res = sorted(memo)

        if len(numbers) == 0:
            return

        if len(numbers) == 1:
            memo.append(numbers[0])
            if sum(memo) > sum(self.res):
                self.res = sorted(memo)
            memo.pop()
            return

        if len(numbers) == 2:
            memo.append(numbers[0])
            if sum(memo) > sum(self.res):
                self.res = sorted(memo)
            memo.pop()
            memo.append(numbers[1])
            if sum(memo) > sum(self.res):
                self.res = sorted(memo)
            memo.pop()
            return

        # print("memo", memo)
        # print("numbers", numbers)
        # print("res", self.res)

        # 这里写错了
        for i in range(len(self.numbers)):
            memo.append(self.numbers[i])
            if i == 0:
                self.dfs(memo, numbers[2:-2])
            elif i == len(numbers) - 1:
                self.dfs(memo, numbers[1:-3])     # -3 决定了递归条件有三个 错误
            else:
                self.dfs(memo, numbers[:i-1] + numbers[i+2:])
            memo.pop()



    # A = [1, 2, 4, 1, 7, 8, 3]  这里认为A[0]与A[n-1]不相邻
    # DP公式 f(i) = max(f(i-2) + numbers[i], f(i-1))
    # 这个解决不了部分case [-4,-2,-4,-1,-7,-8,-3]
    def non_rec_f(self):
        opt = [0] * len(self.numbers)
        opt[0] = self.numbers[0]
        opt[1] = max(self.numbers[0], self.numbers[1])
        for i in range(2, len(self.numbers)):
            opt[i] = max(opt[i - 2] + self.numbers[i], opt[i - 1])
        return opt[len(self.numbers) - 1]

    # A = [-4,-2,-4,-1,-7,-8,-3] 解决数组中含有负数的形式 这里认为A[0] 与 A[n-1] 不相邻
    # DP公式 f(i) = max(numbers[i], max(f(i-2) + numbers[i], f(i-1))
    def chooseMaxV2(self):
        opt = [0] * len(self.numbers)     # 如果要求使用O(1)的空间复杂度就需要用三个变量来保存最终的结果以及 opt[i-1], opt[i-2]
        opt[0] = self.numbers[0]
        opt[1] = max(self.numbers[0], self.numbers[1])
        for i in range(2, len(self.numbers)):
            opt[i] = max(self.numbers[i], max(opt[i-2] + self.numbers[i], opt[i-1]))
        return opt[len(self.numbers) - 1]


# 目前存在递归过深的问题
# 1. 手动模拟递归调用
# 2. 我似乎在leetcode上看到类似的，好像是使用反推法做的
if __name__ == "__main__":
    numbers = [-4,-2,-4,-1,-7,-8,-3]
    sol = Solution(numbers)
    res = sol.chooseMaxV2()
    print("The final result is: ", res)