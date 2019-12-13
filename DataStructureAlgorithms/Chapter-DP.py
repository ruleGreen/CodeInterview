# 0-1 背包问题
"""
weight:物品重量，n:物品个数，w:背包可承载重量
public int knapsack(int[] weight, int n, int w) {
  boolean[][] states = new boolean[n][w+1]; // 默认值false
  states[0][0] = true;  // 第一行的数据要特殊处理，可以利用哨兵优化
  if (weight[0] <= w) {
    states[0][weight[0]] = true;
  }
  for (int i = 1; i < n; ++i) { // 动态规划状态转移
    for (int j = 0; j <= w; ++j) {// 不把第i个物品放入背包
      if (states[i-1][j] == true) states[i][j] = states[i-1][j];
    }
    for (int j = 0; j <= w-weight[i]; ++j) {//把第i个物品放入背包
      if (states[i-1][j]==true) states[i][j+weight[i]] = true;
    }
  }
  for (int i = w; i >= 0; --i) { // 输出结果
    if (states[n-1][i] == true) return i;
  }
  return 0;
}
"""

"""
// 没有记录选择
public int maxW = Integer.MIN_VALUE; //存储背包中物品总重量的最大值
// cw表示当前已经装进去的物品的重量和；i表示考察到哪个物品了；
// w背包重量；items表示每个物品的重量；n表示物品个数
// 假设背包可承受重量100，物品个数10，物品重量存储在数组a中，那可以这样调用函数：
// f(0, 0, a, 10, 100)
public void f(int i, int cw, int[] items, int n, int w) {
  if (cw == w || i == n) { // cw==w表示装满了;i==n表示已经考察完所有的物品
    if (cw > maxW) maxW = cw;
    return;
  }
  f(i+1, cw, items, n, w);
  if (cw + items[i] <= w) {// 已经超过可以背包承受的重量的时候，就不要再装了
    f(i+1,cw + items[i], items, n, w);
  }
}
"""

# 正则表达式问题

"""
public class Pattern {
  private boolean matched = false;
  private char[] pattern; // 正则表达式
  private int plen; // 正则表达式长度

  public Pattern(char[] pattern, int plen) {
    this.pattern = pattern;
    this.plen = plen;
  }

  public boolean match(char[] text, int tlen) { // 文本串及长度
    matched = false;
    rmatch(0, 0, text, tlen);
    return matched;
  }

  private void rmatch(int ti, int pj, char[] text, int tlen) {
    if (matched) return; // 如果已经匹配了，就不要继续递归了
    if (pj == plen) { // 正则表达式到结尾了
      if (ti == tlen) matched = true; // 文本串也到结尾了
      return;
    }
    if (pattern[pj] == '*') { // *匹配任意个字符
      for (int k = 0; k <= tlen-ti; ++k) {
        rmatch(ti+k, pj+1, text, tlen);
      }
    } else if (pattern[pj] == '?') { // ?匹配0个或者1个字符
      rmatch(ti, pj+1, text, tlen);
      rmatch(ti+1, pj+1, text, tlen);
    } else if (ti < tlen && pattern[pj] == text[ti]) { // 纯字符匹配才行
      rmatch(ti+1, pj+1, text, tlen);
    }
  }
}
"""

class Solution:
    def __init__(self, numbers):
        self.numbers = numbers

    # A = [1, 2, 4, 1, 7, 8, 3]  这里认为A[0]与A[n-1]不相邻
    # DP公式 f(i) = max(f(i-2) + numbers[i], f(i-1))
    # 这个解决不了部分case [-4,-2,-4,-1,-7,-8,-3]
    def non_rec_f(self):
        opt = [0] * len(self.numbers)
        opt[0] = self.numbers[0]
        opt[1] = max(self.numbers[0], self.numbers[1])
        for i in range(2, len(self.numbers)):
            opt[i] = max(opt[i - 2] + self.numbers[i], opt[i - 1])
        return opt[len(self.numbers) - 1]

    # A = [-4,-2,-4,-1,-7,-8,-3] 解决数组中含有负数的形式 这里认为A[0] 与 A[n-1] 不相邻
    # DP公式 f(i) = max(numbers[i], max(f(i-2) + numbers[i], f(i-1))
    def chooseMaxV2(self):
        opt = [0] * len(self.numbers)  # 如果要求使用O(1)的空间复杂度就需要用三个变量来保存最终的结果以及 opt[i-1], opt[i-2]
        opt[0] = self.numbers[0]
        opt[1] = max(self.numbers[0], self.numbers[1])
        for i in range(2, len(self.numbers)):
            opt[i] = max(self.numbers[i], max(opt[i - 2] + self.numbers[i], opt[i - 1]))
        return opt[len(self.numbers) - 1]