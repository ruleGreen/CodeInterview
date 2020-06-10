# 20 February 2020
# Copyright WANG Hongru
# Leetcode 做题思路

"""
Ref: https://zhuanlan.zhihu.com/p/104983442?utm_source=ZHShareTargetIDMore&utm_medium=social&utm_oi=770934326882734080
"""

# 思路一  Pattern: Sliding window

"""
Maximum Sum Subarray of Size K (easy)  not find

Smallest Subarray with a given sum (easy)

Longest Substring with K Distinct Characters (medium)

Fruits into Baskets (medium)

No-repeat Substring (hard)

Longest Substring with Same Letters after Replacement (hard)

Longest Subarray with Ones after Replacement (hard)
"""

# 思路二 PatternL: two points

# Case 1: sort and find
"""
Pair with Target Sum (easy)

Remove Duplicates (easy)

Squaring a Sorted Array (easy)

Triplet Sum to Zero (medium)

Triplet Sum Close to Target (medium)

Triplets with Smaller Sum (medium)

Subarrays with Product Less than a Target (medium)

Dutch National Flag Problem (medium)
"""

# 思路三 Fast & Slow pointers

"""
LinkedList Cycle (easy)

Start of LinkedList Cycle (medium)

Happy Number (medium)

Middle of the LinkedList (easy)
"""

# 思路四 Pattern: Merge Intervals，区间合并类型

"""
Merge Intervals (medium)

Insert Interval (medium)

Intervals Intersection (medium)

Conflicting Appointments (medium)
"""

# 思路五 Pattern: Cyclic Sort，循环排序

# 这些问题一般设计到排序好的数组，而且数值一般满足于一定的区间
# 如果问题让你需要在排好序/翻转过的数组中，寻找丢失的/重复的/最小的元素

"""
Cyclic Sort (easy)

Find the Missing Number (easy)

Find all Missing Numbers (easy)

Find the Duplicate Number (easy)

Find all Duplicate Numbers (easy)
"""

# 思路六 Pattern: In-place Reversal of a LinkedList，链表翻转

"""
Reverse a LinkedList (easy)
"""
class Solution:
    def reverseList(self, head):
        # cur,prev = head,None
        # while cur:
        #    cur.next,prev,cur = prev,cur,cur.next
        # return prev

        cur, prev = head, None
        while cur:
            # cur,cur.next,prev = cur.next,prev,cur
            cur.next, prev, cur = prev, cur, cur.next
        return prev

"""
Reverse a Sub-list (medium)

Reverse every K-element Sub-list (medium)
"""

# 思路七 Pattern: Tree Breadth First Search，树上的BFS

"""
Binary Tree Level Order Traversal (easy)

Reverse Level Order Traversal (easy)

Zigzag Traversal (medium)

Level Averages in a Binary Tree (easy)

Minimum Depth of a Binary Tree (easy)

Level Order Successor (easy)

Connect Level Order Siblings (medium)
"""

# 8. Pattern: Tree Depth First Search，树上的DFS

"""
Binary Tree Path Sum (easy)

All Paths for a Sum (medium)

Sum of Path Numbers (medium)

Path With Given Sequence (medium)

Count Paths for a Sum (medium)
"""

# 9. Pattern: Two Heaps，双堆类型

"""
Find the Median of a Number Stream (medium)

Sliding Window Median (hard)

Maximize Capital (hard)
"""

# 10. Pattern: Subsets，子集类型，一般都是使用多重DFS

"""
Subsets (easy)

Subsets With Duplicates (easy)

Permutations (medium)

String Permutations by changing case (medium)

Balanced Parentheses (hard)

Unique Generalized Abbreviations (hard)
"""

# 11. Pattern: Modified Binary Search，改造过的二分

"""
Order-agnostic Binary Search (easy)

Ceiling of a Number (medium)

Next Letter (medium)

Number Range (medium)

Search in a Sorted Infinite Array (medium)

Minimum Difference Element (medium)

Bitonic Array Maximum (easy)
"""

# 12. Pattern: Top ‘K’ Elements，前K个系列

"""
Top ‘K’ Numbers (easy)

Kth Smallest Number (easy)

‘K’ Closest Points to the Origin (easy)

Connect Ropes (easy)

Top ‘K’ Frequent Numbers (medium)

Frequency Sort (medium)

Kth Largest Number in a Stream (medium)

‘K’ Closest Numbers (medium)

Maximum Distinct Elements (medium)

Sum of Elements (medium)

Rearrange String (hard)
"""

# 13. Pattern: K-way merge，多路归并

"""
Merge K Sorted Lists (medium)

Kth Smallest Number in M Sorted Lists (Medium)

Kth Smallest Number in a Sorted Matrix (Hard)

Smallest Number Range (Hard)
"""

# 14. Pattern: 0/1 Knapsack (Dynamic Programming)，0/1背包类型

"""
0/1 Knapsack (medium)

Equal Subset Sum Partition (medium)

Subset Sum (medium)

Minimum Subset Sum Difference (hard)
"""

# ** 15. Pattern: Topological Sort (Graph)，拓扑排序类型

"""
Topological Sort (medium)

Tasks Scheduling (medium)

Tasks Scheduling Order (medium)

All Tasks Scheduling Orders (hard)

Alien Dictionary (hard)
"""


# DP Problems

"""
1. 0/1 Knapsack, 0/1背包，6个题
0/1 Knapsack，0/1背包问题

Equal Subset Sum Partition，相等子集划分问题

Subset Sum，子集和问题

Minimum Subset Sum Difference，子集和的最小差问题

Count of Subset Sum，相等子集和的个数问题

Target Sum，寻找目标和的问题
"""

"""
2. Unbounded Knapsack，无限背包，5个题
Unbounded Knapsack，无限背包

Rod Cutting，切钢条问题

Coin Change，换硬币问题

Minimum Coin Change，凑齐每个数需要的最少硬币问题

Maximum Ribbon Cut，丝带的最大值切法
"""

"""
3. Fibonacci Numbers，斐波那契数列，6个题
Fibonacci numbers，斐波那契数列问题

Staircase，爬楼梯问题

Number factors，分解因子问题

Minimum jumps to reach the end，蛙跳最小步数问题

Minimum jumps with fee，蛙跳带有代价的问题

House thief，偷房子问题
"""

"""
4. Palindromic Subsequence，回文子系列，5个题
Longest Palindromic Subsequence，最长回文子序列

Longest Palindromic Substring，最长回文子字符串

Count of Palindromic Substrings，最长子字符串的个数问题

Minimum Deletions in a String to make it a Palindrome，怎么删掉最少字符构成回文

Palindromic Partitioning，怎么分配字符，形成回文
"""

"""
5. Longest Common Substring，最长子字符串系列，13个题
Longest Common Substring，最长相同子串

Longest Common Subsequence，最长相同子序列

Minimum Deletions & Insertions to Transform a String into another，字符串变换

Longest Increasing Subsequence，最长上升子序列

Maximum Sum Increasing Subsequence，最长上升子序列和

Shortest Common Super-sequence，最短超级子序列

Minimum Deletions to Make a Sequence Sorted，最少删除变换出子序列

Longest Repeating Subsequence，最长重复子序列

Subsequence Pattern Matching，子序列匹配

Longest Bitonic Subsequence，最长字节子序列

Longest Alternating Subsequence，最长交差变换子序列

Edit Distance，编辑距离

Strings Interleaving，交织字符串
"""

