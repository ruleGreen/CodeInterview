# 13 January 2020
# Copyright: WANG Hongru


# trick 1
G = [set() for i in range(4)]
connections = [[0,1],[0,2],[1,2]]
for i, j in connections:
    G[i].add(j)
    G[j].add(i)
print(G)

# trick 2
# it is important to transfer grpah to different data structure
directions = {
      1: [(0,-1),(0,1)],
      2: [(-1,0),(1,0)],
      3: [(0,-1),(1,0)],
      4: [(0,1), (1,0)],
      5: [(0,-1),(-1,0)],
      6: [(0,1), (-1,0)]
}