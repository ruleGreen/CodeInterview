# 8 December 2019
# Copyright WANG Hongru

# 排列和组合 都是从n个元素里面选取k个，只不过排列考虑顺序，组合不考虑顺序

# 组合参见 leetcode combination等一系列题目


class Solution:
    # 排列
    """
    假设数组中存储的是1，2， 3...n。
    f(1, 2, ...n) = {最后一位是1, f(n - 1)} + {最后一位是2, f(n - 1)} + ... + {最后一位是n, f(n - 1)}。
    """
    # f(n) = n(n-1)(n-2).....1    O(n!)
    def permute(self, nums):
        res = []
        self.dfs(nums, [], res)
        return res

    def dfs(self, nums, path, res):
        if not nums:
            res.append(path)
            # return # backtracking
        for i in range(len(nums)):
            self.dfs(nums[:i] + nums[i + 1:], path + [nums[i]], res)

    """
    // 调用方式：
    // int[]a = a={1, 2, 3, 4}; printPermutations(a, 4, 4);
    // k表示要处理的子数组的数据个数
    public void printPermutations(int[] data, int n, int k) {
      if (k == 1) {
        for (int i = 0; i < n; ++i) {
          System.out.print(data[i] + " ");
        }
        System.out.println();
      }
    
      for (int i = 0; i < k; ++i) {
        int tmp = data[i];
        data[i] = data[k-1];
        data[k-1] = tmp;
    
        printPermutations(data, n, k - 1);
    
        tmp = data[i];
        data[i] = data[k-1];
        data[k-1] = tmp;
      }
    }
    """

    # subset [1,2,3] => [[],[1],[2],[3],[1,2],...]
    # important !!
    def subsets(self, nums):
        nums.sort()
        result = [[]]
        for num in nums:
            result += [i + [num] for i in result]
        return result

    # subset II [1,2,2] => [[],[1],[2],[1,2],..]
    def subsetWtihDup(self, nums):
        res, tmp = [[]], []
        import copy

        for i in range(len(nums)):
            tmp = copy.deepcopy(res)        # 深拷贝
            for j in range(len(res)):
                res[j].append(nums[i])
            res.extend(tmp)

        results = []
        for j in range(len(res)):
            res[j] = sorted(res[j])
            if res[j] not in results:
                results.append(res[j])
        return results


if __name__ == "__main__":
    sol = Solution()
    numbers = [1,2,3]
    print("==========================================================================================================")
    print("The permutations of numbers: ", sol.permute(numbers))
    print("The subsets of numbers: ", sol.subsets(numbers))
    print("The subsets of [1,2,2]: ", sol.subsetWtihDup([1,2,2]))