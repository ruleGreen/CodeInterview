# 12 December 2019
# Copyright: Wang Hongru
import collections

class Solution:
    # Leetcode 49. Group Anagrams
    """
    Input: ["eat", "tea", "tan", "ate", "nat", "bat"]
    Output:
    [
      ["ate","eat","tea"],
      ["nat","tan"],
      ["bat"]
    ]
    """
    def groupAnagrams(self, strs):
        if len(strs) == 0 or strs is None:
            return [[]]

        ans = collections.defaultdict(list)
        print("ans is:", ans)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            print("tuple of count is: ", tuple(count))
            ans[tuple(count)].append(s)
        return ans.values()

if __name__ == "__main__":
    sol = Solution()
    print("===============================================================")
    sol.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])