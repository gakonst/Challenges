import six
from collections import OrderedDict
# Break list in n equal chunks. If noneven, is ok
def chunks(l,n):
    for i in range(0,len(l),n):
        yield l[i:i+n]

# https://www.hackerrank.com/challenges/keyword-transposition-cipher algorithm
def substitutedAlphabet(key, alphabet):
    final = ""
    block = []
    filtered = alphabet
    for letter in key:
        filtered = filtered.replace(letter,"")
    cipherbet = key +filtered
    blocks = list(chunks(cipherbet,len(key)))

    zipped = list(map(list, six.moves.zip_longest(*blocks, fillvalue='-')))
    alphabets = [''.join(y) for y in zipped]
    alphabets = [ab.replace("-","") for ab in alphabets]

    #SECRT -> CERST
    key = sorted(key)
    for letter in key:
        for alph in alphabets:
            if alph.startswith(letter):
                final+=alph
                break
    return final

def indexInSub(letter,substituted):
    i = 0
    if letter is " ":
        return None
    for l in substituted:
        if letter == l: # found
            return i
        else:
            i+=1 # continue looking
    return None

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
n = int(input())
for _ in range(n):
    decoded = ""
    key = str(input())
    key = "".join(OrderedDict.fromkeys(key))
    secret = str(input())
    substituted = substitutedAlphabet(key,alphabet)
    for letter in secret:
        # find index in sub alphabet
        index = indexInSub(letter, substituted)
        if index is not None:
            decoded+=alphabet[index]
        else:
            decoded+=" "
    print (decoded)


