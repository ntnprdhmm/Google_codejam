f_name = "A-large-practice"
f_in = open(f_name + ".in", "r")
f_out = open(f_name + ".out", "w")
# for each test case
for test_case in range(int(f_in.readline().strip())):
    c = int(f_in.readline().strip())
    nb_items = int(f_in.readline().strip())
    items = list(map(int, f_in.readline().strip().split()))
    d = {}
    for i in range(nb_items):
        # calculate the complement, and search it in the dict
        comp = c - items[i]
        if comp in d:
            f_out.write("Case #{}: {} {}\n".format(test_case+1, d[comp]+1, i+1))
            break
        # add the price of this item in the dict
        d[items[i]] = i