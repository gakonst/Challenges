from collections import Counter


#Fails the tests 12-13-14.
#Use Pypy2 for slightly faster performance
#Can also use next(sys.stdin) instead of raw_input() for minor improvement

def solve(n):
    # Repeat for each testcase
    for i in range(0, n):
        # D is number of words to be checked
        # S  is number of potential dictionary strings
        d, s = map(int, raw_input().split())
        # words = ['ant', 'top', 'open', 'apple', 'lean']
        # d_strings = ['anteplop', 'antelope', 'penleantopan']
        # d,s = 5,3
        chars = []
        words = []
        d_strings = []
        n_chars = []
        n_strings = []
        for i in range(0, d):
            word = raw_input().strip()
            words.append(word)
            chars.append([character for character in word])
            # [item for sublist in chars[i] for item in sublist]
           # chars.append([character for character in words[i]])
            # n_chars.append(0)
            n_chars.append(Counter(chars[i]))
        perfect = Counter()
        for p in n_chars:
            perfect |= p
            # print str(perfect) + " is the perfect dictionary. Searching if it exists"
            # if perfect in n_strings:
            #  print perfect
        for i in range(0, s):
            count = 0
            is_dict = True
            not_perf = False
            d_strings.append(raw_input().strip())
            n_strings.append(Counter(d_strings[i]))
            if n_strings[i] == perfect:
                print "Yes Yes"
                #  print d_strings[i]
            else:
                for letter in perfect:
                    diff = n_strings[i][letter] - perfect[letter]
                    if diff < 0:
                        count += abs(diff)
                        is_dict = False
                    else:
                        not_perf = True
            if not is_dict:
                print "No " + str(count)
            if not_perf and is_dict:
                print "Yes No"
                # Is Dictionary String?
                #
                # print n_strings
                # print n_chars
                # print d_strings
                # print chars
                # print Counter(list(perfect))


if __name__ == '__main__':
    T = int(raw_input().strip())
    solve(T)
