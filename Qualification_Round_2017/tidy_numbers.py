def find_previous_tidy(n):
    s = str(n)
    previous = "0"
    previous_index = 0
    for i, digit in enumerate(s):
        if previous > digit:
            return int(s[:previous_index+1]) * 10**(len(s) - previous_index - 1) - 1
        if previous != digit:
            previous_index = i
        previous = digit
    return n

# read input from file
# print output in file
f_name = "B-small-practice"
f_in = open(f_name + ".in", "r")
f_out = open(f_name + ".out", "w")

for test in range(int(f_in.readline())):
    n = int(f_in.readline())
    n = find_previous_tidy(n)

    f_out.write("Case #{}: {}\n".format(test+1, n))
