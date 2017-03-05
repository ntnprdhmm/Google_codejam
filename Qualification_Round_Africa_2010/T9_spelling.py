""" join the list, with pauses when necessary
"""
def to_string(l):
    len_l = len(l)
    # empty list => return empty string
    if len_l == 0:
        return ""
    # one item => return it
    if len_l == 1:
        return l[0]
    # many items => join them
    s = l[0]
    for i in range(1, len_l):
        if l[i-1][0] == l[i][0]:
            s += " "
        s += l[i]
    return s

""" letter to digits
"""
def get_code(letter):
    if letter == " ":
        return '0'
    keypad = ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
    # search the key index
    for i in range(len(keypad)):
        if letter in keypad[i]:
            # add 2 because "abc" is on keypad number 2
            return str(i + 2) * (keypad[i].index(letter) + 1)
    return None

f_name = "C-large-practice"
f_in = open(f_name + ".in", "r")
f_out = open(f_name + ".out", "w")
# for each test case
for test_case in range(int(f_in.readline().strip())):
    t9 = []
    sss = f_in.readline()[:-1] # last char is \n
    print(sss)
    for c in sss:
        t9.append(get_code(c))
    f_out.write("Case #{}: {}\n".format(test_case+1, to_string(t9)))