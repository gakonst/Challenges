

alphabet = 'abcdefghijklmnopqrstuvwxyz'

heights = list(map(int,input().split()))
word = input()

# maxHeight found by finding the letter with the biggest height in the word given
maxHeight = 0
for letter in word:
    if heights[alphabet.index(letter)] > maxHeight:
            maxHeight = heights[alphabet.index(letter)]


area = len(string) * maxHeight
print (word)

''' Better Way:

    heights = list(map(int,input().split()))
    word = [heights[ord(c)-ord('a')] for c in input()]
    print (max(word)*len(word))
'''


