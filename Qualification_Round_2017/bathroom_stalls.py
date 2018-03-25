from heapq import heappush, heappop

f_name = "C-small-practice-2"
f_in = open(f_name + ".in", "r")
f_out = open(f_name + ".out", "w")

class Range(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __lt__(self, o):
        return (self.y - self.x) > (o.y - o.x)

def solve(n, k):
    if n == k: return (0, 0)

    q = []
    heappush(q, Range(0, n-1))
    for _ in range(k-1):
        b = heappop(q) # pop the biggest range of free stalls
        #print(b)
        m = (b.x + b.y) // 2 # find the "left middle"
        #print(m)
        left = Range(b.x, m-1)
        right = Range(m+1, b.y)
        if right.y >= right.x:
            heappush(q, right)
        if left.y >= left.x:
            heappush(q, left)

    b = heappop(q)
    #print(b)
    m = (b.y + b.x) // 2
    #print(m)
    left = b.y - m
    right = m - b.x
    return (max(left, right), min(left, right))

for test in range(int(f_in.readline().strip())):
    n, k = map(int, f_in.readline().split())
    print("%d %d" % (n, k))
    max_stalls, min_stalls = solve(n, k)
    f_out.write("Case #{}: {} {}\n".format(test+1, max_stalls, min_stalls))
