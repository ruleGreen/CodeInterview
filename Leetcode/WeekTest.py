class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        total_pos = a + b + c
        self.cands = list()

        # dfs tle
        # dfs + cut
        def dfs(curr, a, b, c, total):
            if len(curr) == total:
                self.cands.append(curr)
            elif len(curr) < total:
                self.cands.append(curr)

            if len(curr) >= 2:
                if (curr[-1] != 'a' or curr[-2] != 'a') and a > 0:
                    dfs(curr + 'a', a - 1, b, c, total)

                if (curr[-1] != 'b' or curr[-2] != 'b') and b > 0:
                    dfs(curr + 'b', a, b - 1, c, total)

                if (curr[-1] != 'c' or curr[-2] != 'c') and c > 0:
                    dfs(curr + 'c', a, b, c - 1, total)

            else:
                if a > 0:
                    dfs(curr + 'a', a - 1, b, c, total)
                if b > 0:
                    dfs(curr + 'b', a, b - 1, c, total)
                if c > 0:
                    dfs(curr + 'c', a, b, c - 1, total)

        dfs('', a, b, c, total_pos)

        max_len = max(len(self.cands[i]) for i in range(len(self.cands)))
        print(self.cands)

        for i in range(len(self.cands)):
            if len(self.cands[i]) == max_len:
                return self.cands[i]


sol = Solution()
res = sol.longestDiverseString(4, 42, 7)
print(res)