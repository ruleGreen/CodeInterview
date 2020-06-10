# 2020 1 April
# Copyright: WANG Hongru

# defination of the Graph
"""
邻接矩阵
[
0, 1, 0, 1, 0
1, 0, 0, 0, 1
0, 0, 0, 0, 0
1, 0, 0, 0, 1
0, 1, 0, 1, 0
]

邻接表
1: [2,3,4]
2: [4,5]
3: [1]
4: [1,2]
5: [2]
"""
V = [1,2,3,4,5]
E = [[2,3,4], [4,5], [1], [1,2], [2]]
grpah = {}
for i in range(len(V)):
    grpah[V[i]] = set()
    for j in range(len(E[i])):
        grpah[V[i]].add(E[i][j])
print(grpah)

# bfs vs dfs  queue vs stack
"""
bfs: time complexity O(V+E)  space complexity O(V)
终止顶点 t 离起始顶点 s 很远，需要遍历完整个图才能找到。
这个时候，每个顶点都要进出一遍队列，每个边也都会被访问一次，
所以，广度优先搜索的时间复杂度是 O(V+E)，
其中，V 表示顶点的个数，E 表示边的个数。
当然，对于一个连通图来说，
也就是说一个图中的所有顶点都是连通的，E 肯定要大于等于 V-1，所以，广度优先搜索的时间复杂度也可以简写为 O(E)。

dfs: time complexity O(E) space complexity O(V)

"""
class Solution:
    def __init__(self, grpah):
        self.grpah = grpah

    def bfs(self, s, t):
        return

    def dfs(self, s, t):
        return

sol = Solution(grpah)
sol.dfs(1, 3)
sol.bfs(1, 3)
