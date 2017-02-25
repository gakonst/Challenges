unshifted = str(input())
e = int(input())
alphabet = list(range(10))

def shiftStr(unshifted,e):
    shift = ""
    for digit in unshifted:
        shifted_digit = alphabet[alphabet.index((int(digit)+e)%len(alphabet))]
        shift+= str(shifted_digit)
    return shift


print (shiftStr(unshifted,e))





