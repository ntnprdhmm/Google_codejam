f_name = "A-large-practice"
f_in = open(f_name + ".in", "r")
f_out = open(f_name + ".out", "w")

# for each test case
for test_case in range(int(f_in.readline().strip())):
    n = int(f_in.readline().strip())
    # read the links, save them
    links = []
    for _ in range(n):
        a, b = list(map(int, f_in.readline().strip().split()))
        links.append((a, b))
    # for each links, count how many links it cut
    counter = 0
    for i in range(n):
        for j in range(i+1, n):
            if not ((links[j][0] > links[i][0] and links[j][1] > links[i][1]) or (links[j][0] < links[i][0] and links[j][1] < links[i][1])):
                counter += 1
    f_out.write("Case #{}: {}\n".format(test_case+1, counter))