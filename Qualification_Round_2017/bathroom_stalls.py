from heapq import heappush, heappop

f_name = "C-large-practice"
f_in = open(f_name + ".in", "r")
f_out = open(f_name + ".out", "w")

def solve(n, k):
    if n == k: return (0, 0)

    q = []
    heappush(q, -n)
    for _ in range(k-1):
        b = -heappop(q) # pop the biggest range of free stalls
        left = (b-1) // 2
        right = b // 2
        #print("%d %d" % (left, right))
        heappush(q, -right)
        heappush(q, -left)

    b = -heappop(q)
    left = b // 2
    right = (b-1) // 2
    #print("%d %d" % (left, right))
    return left, right

for test in range(int(f_in.readline().strip())):
    n, k = map(int, f_in.readline().split())
    #print("-------------")
    print("%d %d" % (n, k))
    max_stalls, min_stalls = solve(n, k)
    f_out.write("Case #{}: {} {}\n".format(test+1, max_stalls, min_stalls))
