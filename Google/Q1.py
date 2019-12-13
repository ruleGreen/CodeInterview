T = int(input())

for case in range(T):
    N, M, Q = map(int, input().strip().split())
    P = list(map(int, input().strip().split()))
    R = list(map(int, input().strip().split()))

    # print(N, M, Q)
    # print(P, R)

    pages = [i for i in range(1, N+1)]
    res = []
    for i in range(len(R)):
        j = 1
        page = []
        while R[i] * j <= N:
            if R[i] * j not in P:
                page.append(R[i] * j)
            j += 1
        res.append(len(page))

    print("Case #" + str(case + 1) + ": " + str(sum(res)))


