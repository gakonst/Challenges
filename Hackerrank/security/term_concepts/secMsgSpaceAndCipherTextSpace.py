unshifted = str(input())
shift = ""
alphabet = list(range(10))

for digit in unshifted:
    shifted_digit = alphabet[alphabet.index((int(digit)+1)%len(alphabet))]
    shift+= str(shifted_digit)

print (shift)



