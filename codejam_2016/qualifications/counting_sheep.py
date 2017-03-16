f_name = "A-large-practice"
f_in = open(f_name + ".in", "r")
f_out = open(f_name + ".out", "w")

# for each test case
for test_case in range(int(f_in.readline().strip())):
    print("\n=====================")
    n = int(f_in.readline().strip())
    print("N : %d" % n)
    print("=======")
    answer = "INSOMNIA"
    # save all the digits she has seen
    d = {}
    for i in range(1, 200):
        print(n*i)
        for digit in str(n * i):
            if digit in d:
                d[digit] += 1
            else:
                d[digit] = 1
        # check if she has seen all the digits between 1 and 9
        if len(d.keys()) == 10:
            answer = n * i
            break
    f_out.write("Case #{}: {}\n".format(test_case+1, answer))