# 22 November 2019
# author: Wang Hongru

"""
数组是适合查找操作，但是查找的时间复杂度并不为 O(1)。
即便是排好序的数组，你用二分查找，时间复杂度也是 O(logn)。
所以，正确的表述应该是，数组支持随机访问，根据下标随机访问的时间复杂度为 O(1)
"""
# basic operations of array
array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
print(array.index(4))  # index(element) get the index of element
print(array.pop(1))    # pop(index) delete the element at the position of index
print("Before delete the element", array)
del array[0]           # delete the element according to index
print("After delete the element", array)


# 下面这两种方法都没有改变array的内存位置，在使用递归代码去做 res.append(array)的时候要注意，就会报错
array = array.sort()
array.sort()
# 下面这个可以
array = sorted(array)

maxV = max(array)
minV = min(array)

# 每次使用递归的时候要注意append 和 pop
nums = 2
array.append(nums)
# TO DO some recursion function
array.pop(-1)


"""
如果数组中的数据是有序的，我们在某个位置插入一个新的元素时，就必须按照刚才的方法搬移 k 之后的数据。
但是，如果数组中存储的数据并没有任何规律，数组只是被当作一个存储数据的集合。在这种情况下，如果要将某个数组插入到第 k 个位置，为了避免大规模的数据搬移，
我们还有一个简单的办法就是，直接将第 k 位的数据搬移到数组元素的最后，把新的元素直接放入第 k 个位置
"""

# Leetcode 40
"""
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        self.res = []
        
        candidates = [candidates[i] for i in range(len(candidates)) if candidates[i] <= target ]
        self.dfs(candidates, target, [])
        
        return self.res
    
    def dfs(self, cands, target, memo):
        # print(memo, target)
        if target == 0:
            memo = sorted(memo)
            # print(self.res,"before res")
            if memo not in self.res:
                self.res.append(memo)
            # print(self.res, "after res")
            return 
        
        if target < 0:
            return
        
        for i in range(0, len(cands)):
            value = cands.pop(i)
            memo.append(value)
            if target - value >= 0:        # 减少搜索空间
                self.dfs(cands, target - value, memo)
            memo.pop(-1)
            cands.insert(i, value)
            
"""