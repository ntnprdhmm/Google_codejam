def generated_from_pattern(pattern):
    return find_words(pattern, 0, [])

def find_words(pattern, i, words):
    # if we are at the end of the pattern, stop
    if len(pattern) <= i+1:
        return pattern
    else:
        # if the next char is an oppening bracket recursive call on all the possibilities
        if pattern[i] == '(':
            letters = []
            j = i + 1
            while pattern[j] != ')':
                letters.append(pattern[j])
                j += 1
            # recursive call for each letter, without the brackets block
            first_part = pattern[:i]
            second_part = pattern[j+1:]
            for letter in letters:
                word = find_words(first_part + letter + second_part, i + 1, words)
                if word:
                    words.append(word)
            return words
        # just go to the next pattern char
        else:
            return words.append(find_words(pattern, i+1, words))

f_name = "test"
f_in = open(f_name + ".in", "r")
f_out = open(f_name + ".out", "w")

l, d, n = list(map(int, f_in.readline().strip().split()))
# save the alien words
words = []
for i in range(d):
    words.append(f_in.readline().strip())
# test cases
for test_case in range(n):
    # read the pattern
    pattern = f_in.readline().strip()
    # generate words from the pattern and loop through them
    print(generated_from_pattern(pattern))