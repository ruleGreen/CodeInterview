"""
定义LCS(S,T)为字符串S和字符串T最长公共子序列的长度,即一个最长的序列W既是S的子序列也是T的子序列的长度。
小易给出一个合法的括号匹配序列s,小易希望你能找出具有以下特征的括号序列t:
1、t跟s不同,但是长度相同
2、t也是一个合法的括号匹配序列
3、LCS(s, t)是满足上述两个条件的t中最大的
因为这样的t可能存在多个,小易需要你计算出满足条件的t有多少个。
"""

s = input().strip()


class Solution:
    def __init__(self):
        self.res = []

    def reset(self):
        self.res = []

    def generate(self, n, t, left, right):
        # 产生所有与s相同长度的合法的括号序列，并且与s不相同 -> t
        if len(t) == n:
            if left == right and s != t:
                self.res.append(t)
            return
        if left > right:
            self.generate(n, t + "(", left + 1, right)
            self.generate(n, t + ")", left, right + 1)
        else:
            self.generate(n, t + "(", left + 1, right)

    def lcs(self, i, j, s, t, v):
        print(i, j, s, t, v)
        if i == len(s) or j == len(t):
            print("+++++++++weird++++++++++")
            if j < len(t):
                v += len(t) - j
            if i < len(s):
                v += len(s) - i
            if v < self.v:
                print("------res--------:", v)
                self.v = v
            # max()
            return
        if s[i] == t[j]:
            self.lcs(i+1, j+1, s, t, v+1)
        else:
            self.lcs(i, j+1, s, t, v)
            self.lcs(i+1, j, s, t, v)

    def lcs_geek(self, s, n, t, m):
        maxlcs = [[0 for _ in range(m)] for _ in range(n)]
        for j in range(0, m):
            if s[0] == t[j]:
                maxlcs[0][j] = 1
            elif j != 0:
                maxlcs[0][j] = maxlcs[0][j-1]
            else:
                maxlcs[0][j] = 0

        for i in range(0, n):
            if s[i] == t[0]:
                maxlcs[i][0] = 1
            elif i != 0:
                maxlcs[i][0] = maxlcs[i-1][0]
            else:
                maxlcs[i][0] = 0

        for i in range(1, n):
            for j in range(1, m):
                if s[i] == t[j]:
                    maxlcs[i][j] = max(maxlcs[i-1][j], maxlcs[i][j-1], maxlcs[i-1][j-1]+1)
                else:
                    maxlcs[i][j] = max(maxlcs[i-1][j], maxlcs[i][j-1], maxlcs[i-1][j-1])

        return maxlcs[n-1][m-1]

solution = Solution()
solution.generate(len(s), "", 0, 0)
cans = solution.res
length = []
for i in range(len(cans)):
    solution.v = float('inf')
    solution.lcs(0, 0, s, cans[i], 0)
    print(solution.v)
    print("==========end===========")
    value = solution.v
    length.append(value)

print(length)
print(length.count(max(length)))