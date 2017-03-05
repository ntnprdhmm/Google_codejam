f_name = "B-large-practice"
f_in = open(f_name + ".in", "r")
f_out = open(f_name + ".out", "w")
# for each test case
for i in range(int(f_in.readline().strip())):
    words = f_in.readline().strip().split()
    f_out.write("Case #{}: {}\n".format(i+1, " ".join(words[::-1])))