# 10 December 2019
# Copyright: Wang Hongru

"""
Q: 有一家公司要完成一个课题，该课题分为n个月完成。现在知道每个月至少需要多少人手才能完成这个阶段的任务。
假如说我们要聘请一个员工，那么我们就要有一定的花费（第二行的第一个数字）；
假如说我们解雇一个员工，那么我们也有一定的花费（第二行的第三个数字）。
当然员工也是要拿工资的，每个月拿一定量的工资（假如说某个员工不干活也是拿工资的，第二行第二个数字），
问你完成这个课题，最小需要花费多少钱？
Input:
3  //一个课题分三个月解决
4 5 6  //分别为聘请一个员工的花费、一个员工的工资、一个员工被解雇的花费
10 9 11 //第一个月至少需要10个人，第二个月至少需要9个人，第三个月至少需要11个人
"""

class Solution:
    def findMinCost(self, months, hire, salary, fired, needed):
        # 其实我们只需要记录最少的人数和最多的人数
        min_needed, max_needed = min(needed), max(needed)
        cost = [[-1 for _ in range(max_needed - min_needed + 1)] for _ in range(months)]

        for person in range(needed[0] - min_needed, max_needed - min_needed + 1):
            cost[0][person] = (person + min_needed) * (hire + salary)

        for month in range(1, len(cost)):
            # 第一种情况 当前所需要的人数少于上个月的
            if needed[month] < needed[month-1]:
                for person in range(needed[month] - min_needed, needed[month-1] - min_needed + 1):
                    decrease = needed[month-1] - (person + min_needed)
                    cost[month][person] = cost[month-1][needed[month-1] - min_needed] + decrease * fired + (needed[month-1] - decrease) * salary

            # 第二种情况 当前所需要的人数大于上个月的
            if needed[month] > needed[month-1]:
                for person in range(needed[month] - min_needed, max_needed - min_needed + 1):
                    # cost[month-1][person] +
                    cost[month][person] = min(cost[month][person], )

        return


if __name__ == "__main__":
    months = int(input("Please input the month: "))
    hire, salary, fired = map(int, input("Please input the cost, salary, fired cost of individual person: ").strip().split())
    needed = list(map(int, input("Please input the minimum person needed per month: ").strip().split()))
    sol = Solution()
    mincost = sol.findMinCost(months, hire, salary, fired, needed)
    print("The final minimum cost is:", mincost)
