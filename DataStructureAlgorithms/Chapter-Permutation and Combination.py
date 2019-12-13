# 8 December 2019
# Copyright WANG Hongru

# 排列和组合 都是从n个元素里面选取k个，只不过排列考虑顺序，组合不考虑顺序

# 组合参见 leetcode combination等一系列题目


class Solution:
    # 排列
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

    # subset [1,2,3] => [[],[1],[2],[3],[1,2],...]
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