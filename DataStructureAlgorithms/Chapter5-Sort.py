# 28 November 2019
# author: Wang Hongru

# 复杂度对比 有序数 逆序数
"""
=================================================================
归并排序 快速排序              O(nlogn)             基于比较
冒泡排序 插入排序 选择排序      O(n^2)               基于比较
桶排序 基数排序 计数排序       O(n)                不基于比较
=================================================================

"""
# 是否是原地排序，稳定排序，不稳定排序
# 冒泡排序, 插入排序是原地排序，稳定排序
# 选择排序是原地排序，但是不稳定排序
# 归并排序是稳定排序，空间复杂度是O(N), 非原地排序

# 快速排序是不稳定排序，原地排序，空间复杂度为O(1), 只要在partition的时候不要使用额外的空间
# 比如 [6，8，7，6，3，5，9，4] 在经过第一次分区操作之后，两个 6 的相对先后顺序就会改变
# 快速排序在极端条件下时间复杂度退化成O(N^2), 比如说[1，3，5，6，8]  看pivot怎么选择，可以改成随机选取

# 归并排序的处理过程是由下到上的，先处理子问题，然后再合并。而快排正好相反，它的处理过程是由上到下的，先分区，然后再处理子问题

# 桶排序 年龄 高考分数
# 计数排序 有点类似于字符串匹配算法里面的next数组 详见下文
# 基数排序 手机号码排序，从低位到高位

"""
Q: 为什么有时候插入排序 比 冒泡排序更受欢迎？？？
A：冒泡排序的数据交换要比插入排序的数据移动要复杂，从常数时间复杂度分析
"""

"""
Q: O(n) 的时间找到数组内第k大的元素 或者第k小的元素
A: 使用快速排序的方法，详见下方函数
"""

"""
如果我们现在有 10 万条订单数据，我们希望按照金额从小到大对订单数据排序。对于金额相同的订单，我们希望按照下单时间从早到晚有序。
对于这样一个排序需求，我们怎么来做呢？最先想到的方法是：我们先按照金额对订单数据进行排序，然后，再遍历排序之后的订单数据，对于每个金额相同的小区间再按照下单时间排序。
这种排序思路理解起来不难，但是实现起来会很复杂。借助稳定排序算法，这个问题可以非常简洁地解决。
解决思路是这样的：我们先按照下单时间给订单排序，注意是按照下单时间，不是金额。排序完成之后，我们用稳定排序算法，按照订单金额重新排序。
"""
import math

class Solution(object):
    def __init__(self):
        self.methods = 5

    # 冒泡排序 Bubble Sort
    # 每次冒泡比较相邻两个位置的元素，使得每次冒泡结束的时候数组当中最大的元素在最右边
    # 最多执行 len(numbers) 次冒泡
    # 优化：
    # 当某次冒泡操作已经没有数据交换时，说明已经达到完全有序，不用再继续执行后续的冒泡操作
    def bubbleSort(self, numbers):
        if numbers is None or len(numbers) == 0:
            return numbers

        # 冒泡排序
        for i in range(0, len(numbers)):
            flag = 0
            for j in range(0, len(numbers) - i - 1):   # 注意！！！！！
                if numbers[j] > numbers[j + 1]:        # 注意！！！！！
                    flag = 1
                    numbers[j], numbers[j+1] = numbers[j+1], numbers[j]    # 注意！！！！！
            print("after {} th bubble: {}".format(i, numbers))
            if flag == 0:
                return numbers
        return numbers


    # 插入排序
    # 把数据看做 已排序区间 和 未排序区间
    def insertSort(self, numbers):
        if numbers is None or len(numbers) == 0:
            return numbers

        # 插入排序
        # 这样写思想是对的，但是复杂度过高，一般不对
        """
        for i in range(0, len(numbers)):
            for j in range(0, i):
                if numbers[j] > numbers[i]:
                    value = numbers.pop(i)
                    numbers.insert(j, value)    # 把未排序区间的第一个数插入到已排序区间
                    break
            print("after {} th insert: {}".format(i, numbers))
        """
        for i in range(1, len(numbers)):
            value = numbers[i]
            index = i - 1
            while index >= 0:
                if numbers[index] < value:       # 注意！！！！！这里是value，而不是numbers[i]
                    break
                numbers[index+1] = numbers[index]
                index -= 1
            numbers[index + 1] = value
            print("after {} th insert: {}".format(i, numbers))
        return numbers

    # 选择排序
    def chooseSort(self, numbers):
        for i in range(0, len(numbers)):
            flag = 0
            for j in range(i, len(numbers)):
                if numbers[i] > numbers[j]:
                    flag = 1          # 检测当前选择是否有数据交换操作
                    numbers[i], numbers[j] = numbers[j], numbers[i]
            print("after {} th choose: {}".format(i, numbers))
            if flag == 0:
                return numbers
        return numbers

    # 归并排序
    # 分治是一种解决问题的处理思想，递归是一种编程技巧
    # 递推公式：merge_sort(p…r) = merge(merge_sort(p…q), merge_sort(q+1…r))
    # 终止条件：p >= r 不用再继续分解
    # 复杂度分析: T(n) = 2*T(n/2) + n； n>1
    def recursionSortV1(self, numbers):
        if numbers is None or len(numbers) == 0:
            return numbers

        if len(numbers) == 1:
            return numbers

        def merge(left, right):            # 合并函数借助哨兵简化方法 传入的后两个数组各在尾部多放一个和原有最后值相同的值 或者 最大值
            all = []
            l = r = 0
            while l < len(left) and r < len(right):
                if left[l] < right[r]:
                    all.append(left[l])
                    l += 1
                else:
                    all.append(right[r])
                    r += 1

            if l < len(left):
                all.extend(left[l:])

            if r < len(right):
                all.extend(right[r:])

            return all

        middle = len(numbers) // 2
        left = self.recursionSortV1(numbers[:middle])
        right = self.recursionSortV1(numbers[middle:])

        res = merge(left, right)
        return res

    def recursionSortV2(self, numbers, start, end):

        def merge(arr, l, m, r):            # 合并函数借助哨兵简化方法 传入的后两个数组各在尾部多放一个和原有最后值相同的值 或者 最大值
            n1 = m - l
            n2 = r - m

            # 创建临时数组
            L = [0] * (n1)
            R = [0] * (n2)

            # 拷贝数据到临时数组 arrays L[] 和 R[]
            for i in range(0, n1):
                L[i] = arr[l + i]

            for j in range(0, n2):
                R[j] = arr[m + j]

                # 归并临时数组到 arr[l..r]
            i = 0  # 初始化第一个子数组的索引
            j = 0  # 初始化第二个子数组的索引
            k = l  # 初始归并子数组的索引

            while i < n1 and j < n2:
                if L[i] <= R[j]:
                    arr[k] = L[i]
                    i += 1
                else:
                    arr[k] = R[j]
                    j += 1
                k += 1

            # 拷贝 L[] 的保留元素
            while i < n1:
                arr[k] = L[i]
                i += 1
                k += 1

            # 拷贝 R[] 的保留元素
            while j < n2:
                arr[k] = R[j]
                j += 1
                k += 1

        if end - start > 1:
            middle = (start + end) // 2
            self.recursionSortV2(numbers, start, middle)
            self.recursionSortV2(numbers, middle, end)
            merge(numbers, start, middle, end)

    # 快速排序
    """
    如果要排序数组中下标从 p 到 r 之间的一组数据，我们选择 p 到 r 之间的任意一个数据作为 pivot（分区点）。
    我们遍历 p 到 r 之间的数据，将小于 pivot 的放到左边，将大于 pivot 的放到右边，将 pivot 放到中间
    """
    # 递推公式：quick_sort(p…r) = quick_sort(p…q-1) + quick_sort(q+1… r)
    # 终止条件：p >= r
    # 优化选取pivot的方法: 三数取中法  随机法
    def quickSort(self, numbers, start, end):
        if start >= end:
            return

        def partition(numbers, start, end):
            pivot = end - 1
            pointer = current = start          # pointer 可以指向小于pivot的最后一个元素 也可以指向大于pivot的第一个元素
            while current < end - 1:           # 这里是指向大于pivot的第一个元素，这两者区别在于一个是先交换，再+1；另一个是先+1，再交换
                if numbers[current] < numbers[pivot]:
                    numbers[current], numbers[pointer] = numbers[pointer], numbers[current]
                    pointer += 1
                current += 1
            numbers[pointer], numbers[pivot] = numbers[pivot], numbers[pointer]
            return pointer

        pivot = partition(numbers, start, end)
        self.quickSort(numbers, start, pivot)
        self.quickSort(numbers, pivot + 1, end)    # 注意！！！！！ pivot + 1， 因为pivot左右两边都是排好序的，所以不需要再对pivot进行操作

    # 利用快速排序找到数组中第k大的元素
    def findKthMax(self, numbers, k, start, end):

        def partition(numbers, start, end):
            pivot = end - 1
            pointer = current = start          # pointer 可以指向小于pivot的最后一个元素 也可以指向大于pivot的第一个元素
            while current < end - 1:           # 这里是指向大于pivot的第一个元素，这两者区别在于一个是先交换，再+1；另一个是先+1，再交换
                if numbers[current] < numbers[pivot]:
                    numbers[current], numbers[pointer] = numbers[pointer], numbers[current]
                    pointer += 1
                current += 1
            numbers[pointer], numbers[pivot] = numbers[pivot], numbers[pointer]
            return pointer

        pivot = partition(numbers, start, end)
        print("pivot, numbers", pivot, numbers, numbers[pivot])
        if pivot + 1 == k:
            return numbers[pivot]
        elif pivot + 1 < k:
            return self.findKthMax(numbers, k, pivot + 1, end)     # 如果不加return, 递归最终结果返回不了第一层，所以就是None
        else:
            return self.findKthMax(numbers, k, start, pivot)

    # 计数排序
    # 计数排序只能用在数据范围不大的场景中，如果数据范围k比要排序的数据n大很多，就不适合用计数排序了。而且，计数排序只能给非负整数排序，如果要排序的数据是其他类型的，要将其在不改变相对大小的情况下，转化为非负整数。
    def countSort(self, numbers):
        if numbers is None or len(numbers) == 0:
            return numbers

        maxVal = max(numbers)
        count = [0] * (maxVal + 1)

        # 计算numbers里面每个元素的个数放入count里面
        for i in range(len(numbers)):
            count[numbers[i]] += 1

        # 依次累加
        for i in range(1, len(count)):
            count[i] = count[i-1] + count[i]

        print("count", count)

        # 临时数组tmp，存储最后排序之后的结果
        tmp = [0] * len(numbers)
        # 计数排序的关键步骤
        for i in range(len(numbers) - 1, -1, -1):
            index = count[numbers[i]] - 1
            tmp[index] = numbers[i]
            count[numbers[i]] -= 1

        # 把tmp的结果拷贝回numbers
        for i in range(len(numbers)):
            numbers[i] = tmp[i]

        return numbers

if __name__ == "__main__":
    solution = Solution()
    print("================================================")
    # 冒泡排序
    numbers = [3, 5, 4, 3, 8, 7, 1, 2]
    print("Original numbers", numbers)
    number = solution.bubbleSort(numbers)
    print("1. After bubble sort: ", number)
    # 选择排序
    numbers = [3, 5, 4, 3, 8, 7, 1, 2]
    print("Original numbers", numbers)
    number = solution.chooseSort(numbers)
    print("2. After choose sort: ", number)
    # 插入排序
    numbers = [3, 5, 4, 3, 8, 7, 1, 2]
    print("Original numbers", numbers)
    number = solution.insertSort(numbers)
    print("3. After insert sort: ", number)
    # 递归排序 V1
    numbers = [3, 5, 4, 3, 8, 7, 1, 2]
    print("Original numbers", numbers)
    number = solution.recursionSortV1(numbers)
    print("4. After recursion sort V1: ", number)
    # 递归排序 V2
    numbers = [3, 5, 4, 3, 8, 7, 1, 2]
    print("Original numbers", numbers)
    solution.recursionSortV2(numbers, 0, len(numbers))
    print("4. After recursion sort V2: ", numbers)
    # 快速排序
    numbers = [3, 5, 4, 3, 8, 7, 1, 2]
    print("Original numbers", numbers)
    solution.quickSort(numbers, 0, len(numbers))
    print("5. After quick sort: ", numbers)
    # 计数排序
    numbers = [3, 5, 4, 3, 8, 7, 1, 2]
    print("Original numbers", numbers)
    number = solution.countSort(numbers)
    print("6. After count sort: ", number)

    # 利用快速排序找到数组中第k大的元素
    numbers = [3, 5, 4, 3, 8, 7, 1, 2]
    print("Original numbers", numbers)
    kthMax = solution.findKthMax(numbers, 4, 0, len(numbers))
    print("4 th max of {}: ".format(numbers), kthMax)

    print("================================================")