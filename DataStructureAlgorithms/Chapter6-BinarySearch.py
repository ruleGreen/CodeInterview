# Two Sum
# Three Sum
# Four Sum

# Q: 排序的数组进行旋转之后再进行查找
# A: [2,5,6,0,0,1,2]

# Q: 二分查找的变形如下几种形式，参见下方代码
# A:

class Solution:

    # 二分查找 数组必须有序，才能进行二分查找 原因在于：二分查找算法需要按照下标随机访问元素 二分查找只能用在插入、删除操作不频繁，一次排序多次查找的场景中
    # 广泛应用在各种查找比如说fourSum, 求根号等
    def binarySearch(self, nums, value):
        if nums is None or value is None:
            return False
        l, r = 0, len(nums) - 1
        while l <= r:   # 循环退出条件
            mid = (r - l) // 2 + l   # 还可以优化成位运算, 注意位运算的优先级 不能写成 l + (r - l) >> 1
            if nums[mid] == value:
                return True
            elif nums[mid] < value:
                l = mid + 1          # l r的更新
            elif nums[mid] > value:
                r = mid - 1
        return False

    # 在rotate numbers [2, 5, 6, 1, 2, 2, 2] target: 5进行二分查找
    def search(self, nums, target: int) -> bool:
        if nums is None or target is None:
            return False

        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (r - l) // 2 + l
            while l < mid and nums[l] == nums[mid]:  # tricky part
                l += 1
            # remember the value of start and end
            if nums[mid] == target:
                return True
            elif nums[mid] >= nums[l]:
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            elif nums[mid] <= nums[r]:
                if nums[mid] <= target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        return False

    # 查找第一个值等于给定元素的值
    def findFirst(self, nums, target):
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] == target and nums[mid-1] != target:    # 这里需要注意mid为0的情况，虽然index为负值刚好规避了异常
                return mid
            elif nums[mid] >= target:
                r = mid - 1
            else:
                l = mid + 1
        return False

    # 查找最后一个值等于给定值的元素
    def findLast(self, nums, target):
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] == target and nums[mid + 1] != target:
                return mid
            elif nums[mid] <= target:
                l = mid + 1
            else:
                r = mid - 1
        return False

    # 查找第一个大于等于给定值的元素
    def findFirstGreatorEqual(self, nums, target):
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] >= target and nums[mid-1] < target:
                return mid
            elif nums[mid] >= target:
                r = mid - 1
            else:
                l = mid + 1
        return False

    # 查找最后一个小于等于给定值的元素
    def findLastGreatorEqual(self, nums, target):
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] <= target and nums[mid+1] > target:
                return mid
            elif nums[mid] <= target:
                l = mid + 1
            else:
                r = mid - 1
        return False

    # 求一个数的平方根， 非精确值
    def sqrt(self, number):
        l, r = 0, number
        while l <= r:
            mid = l + (r - l) / 2        # 求平方根这里就不能是整除
            if abs(mid * mid - number) < 10**(-6):
                return mid
            elif mid * mid < number:
                l = mid
            else:
                r = mid              # #

    # 在一个数组找四数之和
    def fourSum(self, nums, target: int):
        # method one
        res = []
        for i in range(len(nums)):
            value = nums.pop(i)
            tmp = self.threeSum(nums, target - value)
            for i in range(len(tmp)):
                tmp[i].append(value)
                tmp[i].sort()
                if tmp[i] not in res:
                    res.append(tmp[i])
            nums.insert(i, value)

        return res

    # 在一个数组找三数之和
    def threeSum(self, nums, target):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        nums.sort()
        # print(nums)
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:  # 过滤重复的
                continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                # print(i,l,r)
                s = nums[i] + nums[l] + nums[r]
                if s < target:
                    l += 1
                elif s > target:
                    r -= 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1
                    l += 1; r -= 1
        return res

if __name__ == "__main__":
    numbers = [3, 5, 4, 3, 8, 7, 1, 2]
    sol = Solution()
    print("============================================================")
    print("the result of binary search:", sol.binarySearch(numbers, 3))
    numbers = [3, 4, 5, 1, 2, 2, 2]
    print("the search result of rotate numbers:", sol.search(numbers, 3))
    numbers = [1, 1, 2, 2, 3, 4, 5, 6, 7, 7, 8, 9, 9, 10, 12]
    print("find fist 1: ", sol.findFirst(numbers, 1))
    print("find last 7: ", sol.findLast(numbers, 7))
    print("find first great or equal 9: ", sol.findFirstGreatorEqual(numbers, 9))
    print("find last great or equal 9: ", sol.findLastGreatorEqual(numbers, 9))
