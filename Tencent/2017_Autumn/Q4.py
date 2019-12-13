def binarySearch(down, up, n, res):
    while down <= up:
        mid = ((up - down) >> 1) + down
        print((down, mid), (mid, up))
        if mid < n:
            res += '1'
            down = mid + 1
        elif mid > n:
            res += '0'
            up = mid - 1
        elif mid == n:
            res += '1'
            return res

        if len(res) == 6:
            return res


n = int(input())
down, up, res = -90, 90, ''
res = binarySearch(down, up, n, res)
if len(res) == 6:
    print(res)
else:
    res += '0' * (6 - len(res))
    print(res)
