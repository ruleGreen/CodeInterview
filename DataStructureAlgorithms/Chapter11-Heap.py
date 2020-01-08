# -*- coding: utf-8 -*-
# 8 January 2020
# Copyright: WANG Hongru

# python 当中heapq的使用
import heapq as hq
import numpy as np

data = np.arange(10)
np.random.shuffle(data)  # shuffle the data
heap = []
for i in data:
    hq.heappush(heap, i)
print(heap, data)
print(hq.heappop(heap))  # pop the minimum value
print(hq.heapreplace(heap, 0.2))  # replace the minimum value
print("after pop and replace: ", heap)
print(hq.nlargest(3, heap))   # find the n largest value
print(hq.nsmallest(2, heap))  # find the n smallest value

data = [2, 3, 0, 1, 4, 5, 7, 9, 10, 8, 6]
hq.heapify(data)    # heapify the data
print(data)

"""
知识点：
1. 堆是一个完全二叉树；堆中每一个节点的值都必须大于等于（或小于等于）其子树中每个节点的值
2. 往堆中插入一个元素就需要进行堆化操作，堆化分为从上往下 和 从下往上 两种
一般来说往堆中插入一个元素使用 从下往上 的 堆化； 删除堆顶元素使用 从上往下 的堆化

建堆的实现思路有两种， 建堆的时间复杂度是O(n)
1. 类似于往堆中插入一个元素，从前往后处理一个数组，这时的堆化方式是从下往上
2. 从后往前处理数组（这时从第一个非叶子节点的元素开始处理），然后依次从上往下堆化

tips: 堆排序不是稳定的排序算法，因为在排序的过程，存在将堆的最后一个节点跟堆顶节点互换的操作，所以就有可能改变值相同数据的原始相对顺序。

知识拓展:
Q: 为什么快速排序没有堆排序性能好？
A: 1. 第一点，堆排序数据访问的方式没有快速排序友好。因为不是顺序遍历 2. 第二点，对于同样的数据，在排序过程中，堆排序算法的数据交换次数要多于快速排序。本来有序的数据建堆之后可能无序了
"""

"""
Code: Java version

public class Heap {
    private int[] a; // 数组，从下标1开始存储数据, 这样数组中下标为 i 的节点的左子节点，就是下标为 i∗2 的节点，右子节点就是下标为 i∗2+1 的节点，父节点就是下标为 2i​ 的节点
    private int n;  // 堆可以存储的最大数据个数
    private int count; // 堆中已经存储的数据个数
    
    public Heap(int capacity) {
    a = new int[capacity + 1];
    n = capacity;
    count = 0;
    }

    public void insert(int data) {
    if (count >= n) return; // 堆满了
    ++count;
    a[count] = data;
    int i = count;
    while (i/2 > 0 && a[i] > a[i/2]) { // 自下往上堆化
      swap(a, i, i/2); // swap()函数作用：交换下标为i和i/2的两个元素
      i = i/2;
    }
    }
  
  
    public void removeMax() {
      if (count == 0) return -1; // 堆中没有数据
      a[1] = a[count];
      --count;
      heapify(a, count, 1);
    }
    
    private void heapify(int[] a, int n, int i) { // 自上往下堆化
      while (true) {
        int maxPos = i;
        if (i*2 <= n && a[i] < a[i*2]) maxPos = i*2;
        if (i*2+1 <= n && a[maxPos] < a[i*2+1]) maxPos = i*2+1;
        if (maxPos == i) break;
        swap(a, i, maxPos);
        i = maxPos;
      }
    }
    
    private static void buildHeap(int[] a, int n) {
      for (int i = n/2; i >= 1; --i) {
        heapify(a, n, i);
      }
    }
    
    private static void heapify(int[] a, int n, int i) {
      while (true) {
        int maxPos = i;
        if (i*2 <= n && a[i] < a[i*2]) maxPos = i*2;
        if (i*2+1 <= n && a[maxPos] < a[i*2+1]) maxPos = i*2+1;
        if (maxPos == i) break;
        swap(a, i, maxPos);
        i = maxPos;
      }
    }
    
    // n表示数据的个数，数组a中的数据从下标1到n的位置。
    public static void sort(int[] a, int n) {
      buildHeap(a, n);
      int k = n;
      while (k > 1) {
        swap(a, 1, k);
        --k;
        heapify(a, k, 1);
      }
    }

 }
"""

