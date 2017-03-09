import re

# convert the pattern to a regex
def pattern_to_regex(pattern):
    pattern = pattern.replace("(", "[")
    pattern = pattern.replace(")", "]")
    return re.compile("^" + pattern + "$")

f_name = "A-large-practice"
f_in = open(f_name + ".in", "r")
f_out = open(f_name + ".out", "w")

l, d, n = list(map(int, f_in.readline().strip().split()))
# save the alien words
words = []
for i in range(d):
    words.append(f_in.readline().strip())
# test cases
for test_case in range(n):
    # read the pattern and convert it to regex
    pattern = pattern_to_regex(f_in.readline().strip())
    # count how many generated words are in the alien dict
    count = 0
    for word in words:
        if re.match(pattern, word):
            count += 1
    f_out.write("Case #{}: {}\n".format(test_case+1, count))