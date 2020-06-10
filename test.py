class Solution:
    def minTaps(self, n: int, ranges) -> int:

        cands = []
        for i in range(len(ranges)):
            cands.append([i - ranges[i], i + ranges[i]])
        cands = sorted(cands, key=lambda x: (x[0], x[1]))

        print(cands)
        start = 0
        res = 0

        if cands[0][0] > 0 or cands[-1][1] < n:
            return -1
        while start < len(cands) - 1:
            print(start)
            if cands[start][1] < cands[start + 1][0]:
                return -1
            elif cands[start + 1][0] == cands[start][0]:
                start += 1
            elif cands[start + 1][0] > cands[start][1]:
                res += 1
                start += 1
        return res

if __name__ == "__main__":
    n = 5
    ranges = [3,4,1,1,0,0]
    sol = Solution()
    sol.minTaps(n, ranges)