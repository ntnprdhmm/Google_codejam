from heapq import heappush, heappop

f_name = "C-large-practice"
f_in = open(f_name + ".in", "r")
f_out = open(f_name + ".out", "w")

def solve(n, k):
    if n == k: return (0, 0)

    p_queue = [-n] # priority queue => biggest stalls ranges first
    gaps_sizes = {n: 1} # remember the number of gaps of the same size

    while True:
        biggest = -heappop(p_queue) # pop the biggest range of free stalls
        nb_gaps = gaps_sizes[biggest] # number of gaps with the same size
        del gaps_sizes[biggest] # remove this entry from dict (useless to keep it)
        if k <= nb_gaps:
            # the last person will take one of this gap
            return biggest // 2, (biggest-1) // 2
        else:
            k -= nb_gaps
            left, right = (biggest-1) // 2, biggest // 2
            for gap in [left, right]:
                # if this gap doesn't exists => create it
                if not gap in gaps_sizes:
                    gaps_sizes[gap] = 0
                    heappush(p_queue, -gap)
                gaps_sizes[gap] += nb_gaps

for test in range(int(f_in.readline().strip())):
    n, k = map(int, f_in.readline().split())
    #print("-------------")
    print("%d %d" % (n, k))
    max_stalls, min_stalls = solve(n, k)
    f_out.write("Case #{}: {} {}\n".format(test+1, max_stalls, min_stalls))
