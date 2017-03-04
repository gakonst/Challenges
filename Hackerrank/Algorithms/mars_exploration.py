msg = input()

string = 'SOS'
chunk = 3
# Useful for splitting a string into chunks of chunk length
splitMsg = [ msg[i:i+chunk] for i in range(0,len(msg),chunk)]
count = 0

for msg in splitMsg:
    # Find how many characters differ in a string
    u = zip(msg, string)
    for i,j in u:
        if i != j:
            count+=1


print(count)


