# some special cases


# leetcode 54. Spiral Matrix
"""
public class Solution {
    public List<Integer> spiralOrder(int[][] matrix) {

        List<Integer> res = new ArrayList<Integer>();

        if (matrix.length == 0) {
            return res;
        }

        int rowBegin = 0;
        int rowEnd = matrix.length-1;
        int colBegin = 0;
        int colEnd = matrix[0].length - 1;

        while (rowBegin <= rowEnd && colBegin <= colEnd) {
            // Traverse Right
            for (int j = colBegin; j <= colEnd; j ++) {
                res.add(matrix[rowBegin][j]);
            }
            rowBegin++;

            // Traverse Down
            for (int j = rowBegin; j <= rowEnd; j ++) {
                res.add(matrix[j][colEnd]);
            }
            colEnd--;

            if (rowBegin <= rowEnd) {
                // Traverse Left
                for (int j = colEnd; j >= colBegin; j --) {
                    res.add(matrix[rowEnd][j]);
                }
            }
            rowEnd--;

            if (colBegin <= colEnd) {
                // Traver Up
                for (int j = rowEnd; j >= rowBegin; j --) {
                    res.add(matrix[j][colBegin]);
                }
            }
            colBegin ++;
        }

        return res;
    }
}
"""

class Solution:
    def spiralOrder(self, matrix):
        if not matrix: return []
        R, C = len(matrix), len(matrix[0])
        seen = [[False] * C for _ in matrix]
        ans = []
        dr = [0, 1, 0, -1]       # 技巧一, 这个技巧也可以用在八皇后问题上，或者一切与矩阵相关的
        dc = [1, 0, -1, 0]
        r = c = di = 0
        for _ in range(R * C):
            ans.append(matrix[r][c])
            seen[r][c] = True
            cr, cc = r + dr[di], c + dc[di]
            if 0 <= cr < R and 0 <= cc < C and not seen[cr][cc]:
                r, c = cr, cc
            else:
                di = (di + 1) % 4
                r, c = r + dr[di], c + dc[di]
        return ans


    def generateMatrix(self, n):
        result = [[0 for i in range(n)] for j in range(n)]
        coord = [[(i, j) for j in range(n)] for i in range(n)]

        count = 1

        while coord:
            print(coord)
            for x, y in coord.pop(0):
                result[x][y] = count
                count += 1
            coord = list(zip(*coord))[::-1]     # 技巧二, zip, any, all等函数

        return result


# 所有查找和为target的题型 都可以考虑成 0-1 背包的变形
"""
Q: Leetcode 377. Combination Sum IV
Follow-up: What if negative numbers are allowed in the given array?
"""
def combinationSum4(nums, target: int) -> int:
    # dp
    nums.sort()
    result = [1] + [0] * target

    for i in range(len(result)):
        for num in nums:
            if num == i:
                result[i] += 1
            elif num < i:
                result[i] += result[i - num]
            elif num > i:
                break

    return result[target]

# important !!!!!
import collections
def combinationSum4WithLength(self, nums, target, length, memo=collections.defaultdict(int)):
    if length <= 0: return 0
    if length == 1: return 1 * (target in nums)
    if (target, length) not in memo:
        for num in nums:
            memo[target, length] += self.combinationSum4(nums, target - num, length - 1)
    return memo[target, length]

