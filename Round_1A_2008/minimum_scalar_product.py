f_name = "A-large-practice"
f_in = open(f_name + ".in", "r")
f_out = open(f_name + ".out", "w")
# for each test case
for test_case in range(int(f_in.readline().strip())):
    # read the number of dimensions of the vectors
    n = int(f_in.readline().strip())
    # read the 2 vectors
    a = list(map(int, f_in.readline().strip().split()))
    b = list(map(int, f_in.readline().strip().split()))
    # sort the vectors (a in asc and b in desc)
    a.sort()
    b.sort(reverse=True)
    # do the scalar product
    s_p = sum([ai*bi for (ai, bi) in zip(a, b)])
    f_out.write("Case #{}: {}\n".format(test_case+1, s_p))