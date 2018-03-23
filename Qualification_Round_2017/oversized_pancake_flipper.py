def solve(s, k):
    flip_counter = 0
    for i in range(len(s) - k + 1):
        if not s[i]:
            flip_counter += 1
            # flip the k next pancakes
            for j in range(i, (i+k)):
                s[j] = not s[j]

    # check if all elements are +
    if not all(s):
        flip_counter = -1

    return flip_counter

# read input from file
# print output in file
f_name = "A-large-practice"
f_in = open(f_name + ".in", "r")
f_out = open(f_name + ".out", "w")

# for each test case
for test in range(int(f_in.readline().strip())):
    # read inputs
    s, k = f_in.readline().strip().split()
    # solve
    r = solve([c == '+' for c in s], int(k))
    # print output
    if r >= 0:
        f_out.write("Case #{}: {}\n".format(test+1, r))
    else:
        f_out.write("Case #{}: IMPOSSIBLE\n".format(test+1))
