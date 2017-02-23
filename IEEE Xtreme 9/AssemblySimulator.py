import os


# Handle operations
def alu(src, dest, command):
    ##Print 00,0F -> Prints from 00 to 0F
    static = False
    dest = int(dest, 16)
    # Static value or from memory (previous value from memory matrix)?
    if "#" in src:
        static = True
        arg = src.strip("#")
        arg = int(arg, 16)
    else:
        src = int(src,16)
        arg = int(memArray[src-1],16)
    #
    dest = int(memArray[dest - 1], 16)

    if command == 'ADD':
        dest += arg
    elif command == 'SUB':
        dest -= arg
        if dest < 0:
            dest = -dest
    elif command == 'AND':
        dest = dest & arg
    elif command == 'XOR':
        dest = dest ^ arg
    elif command == 'OR':
        dest = dest | arg
    dest = hex(dest)
    fmt = '{:08x}'
    dest = fmt.format(int(dest, 16))
    dest = dest[len(dest) - 2:]
    print dest
    return dest

# Handle branches based on command and comparison result
def branches(src, comp):
    result = False
    if command == 'BEQ' and comp == 0:
        result = True
    elif command == 'BNE' and comp != 0:
        result = True
    elif command == 'BGT' and comp > 0:
        result = True
    elif command == 'BLT' and comp < 0:
        result = True
    elif command == 'BGE' and comp >= 0:
        result = True
    elif command == 'BLE' and comp <= 0:
        result = True
    return result

def move(src,dest):
	static = dereferenced_src = dereferenced_dest = False
	if "#" in src:
		static = True
        arg = src.strip("#")
        arg = int(arg, 16)
    else:    	src = int(src,16)
        arg = int(memArray[src-1],16)
    #if "(" in src:
    #	dereferenced_src = True
    #	src = src.strip("(").strip(")")
    #else:

	#    f "(" in dest:
    #	dereferenced_dest= True
    #	dest = dest.strip("(").strip(")")
    #else:	
    dest = arg


# Print single byte
def singleprint(index):
    print memArray[index - 1]


# Print range of bytes
def multiprint(start, end):
    print memArray[start:end]


comp = 0
input = open("AssemblySimulator.txt", 'r')
memory = input.readline().strip()
# Consider memory -> string length
stringlength = int(memory, 16)
commands = input.readlines()
input.close()
memArray = []
# Initialize memory
for i in range(0, stringlength):
    memArray.append("00")
# print memArray
operators = ['ADD', 'SUB', 'AND', 'OR', 'XOR']
branchlist = ['BEQ', 'BNE', 'BLE', 'BLT']
other = ['COMP', 'PRINT', 'MOVE']
no_label = operators + other
i = 0
label = "w/e"
while i in range(0, len(commands)):
    print "i = " + str(i)
    line = commands[i].replace(",", " ").split(" ")

    if line[0] in no_label:
        if len(line) == 2:
            command = 'PRINT1'
            dest = line[1]
            dest = dest.rstrip()
            print "Command Issued: " + command, dest
        elif len(line) == 3:
            command = line[0]
            src = line[1]
            dest = line[2]
            dest = dest.rstrip()
            print "Command Issued: " + command, src, dest
    else:
        label = line[0]
        command = line[1].rstrip()
        print "Command Issued: " + label, command

    if command == 'PRINT1':
        index = int(dest, 16)
        singleprint(index)
    elif command == 'PRINT':
        start = int(src, 16)
        end = int(dest, 16)
        multiprint(start, end)
    elif command in operators:
        x = alu(src, dest, command)
        memArray[int(dest, 16) - 1] = x
    elif command == 'COMP':
        comp = int(src, 16) - int(dest, 16)
    elif command in branchlist:
        x = branches(src, comp)
        if x:
            i = int(label) - 1
            print "Branch taken"
        else:
            print "Branch not taken"
     elif command == 'MOVE':
     	move(src,dest)
    i += 1
# print output
