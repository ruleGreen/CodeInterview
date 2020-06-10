# 剑指offer 第43题:

# Q: 给定 n 求出 从 1 到 n 中所有数字包含 1 的个数


# Ref: https://blog.csdn.net/Koala_Tree/article/details/79524603

class Solution:
    def numberOfx(self, n, x):   # -> x: 1- 9
        res = 0
        n_list = list(str(n).strip())

        start = 0

        for i in range(len(n_list) - 1, -1, -1):
            basic = "".join(n_list[j] for j in range(i))
            if basic != "":
                basic = int(basic)
                basic = basic * (10 ** start)
            else:
                basic = 0

            # print(n_list[i], x, basic)
            if int(n_list[i]) > x:
                res += basic + (10 * start)
            elif int(n_list[i]) == x:
                rest = "".join(n_list[j] for j in range(i + 1, len(n_list)))
                res += basic + int(rest) + 1
            else:
                res += basic
            # print("res", res)
            start += 1
        return res

    # this is for number 0
    def numberOf0(self, n):
        res = 0
        n_list = list(str(n).strip())

        start = 0

        for i in range(len(n_list) - 1, 0, -1):
            basic = "".join(n_list[j] for j in range(i))
            if basic != "":
                basic = int(basic)
                basic = basic * (10 ** start) - 1
            else:
                basic = 0

            # print(n_list[i], x, basic)
            if int(n_list[i]) > 0:
                res += basic + (10 * start)
            elif int(n_list[i]) == 0:
                rest = "".join(n_list[j] for j in range(i + 1, len(n_list)))
                if rest != "":
                    res += basic + int(rest) + 1
            else:
                res += basic
            # print("res", res)
            start += 1
        return res


if __name__ == "__main__":
    sol = Solution()
    res = sol.numberOfx(2593, 5)
    res_0 = sol.numberOf0(100)
    print("res", res)
    print("res of 0", res_0)