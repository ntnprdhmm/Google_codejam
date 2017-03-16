f_name = "B-large-practice"
f_in = open(f_name + ".in", "r")
f_out = open(f_name + ".out", "w")

""" Return the index of the last hyphen in the stack
    Or None if no hyphen found
"""
def find_last_hyphen(s):
    last = None
    for i in range(len(s)):
        if s[i] == "-":
            last = i
    return last

""" flip the top of the stack
"""
def flip_stack_top(s, idx):
    # get the top of the stack
    top = s[:idx+1]
    # special case : the top start with "+"
    if top[0] is "+":
        # flip the "+" at the beginnning
        i = 0
        while top[i] is "+":
            top[i] = "-"
            i += 1 
    else:
        # flip the top
        temp = []
        for i in range(idx, -1, -1):
            temp.append("+" if s[i] == "-" else "-")
        top = temp
    return top + s[idx+1:]

# for each test case
for test_case in range(int(f_in.readline().strip())):
    stack = list(f_in.readline().strip())
    counter = 0
    # while there are "-", get the last "-" index and flip the top
    last_hyphen = find_last_hyphen(stack)
    m = 0
    while last_hyphen is not None:
        stack = flip_stack_top(stack, last_hyphen)
        counter += 1
        last_hyphen = find_last_hyphen(stack)
    # print the answer for this test Case
    f_out.write("Case #{}: {}\n".format(test_case+1, counter))