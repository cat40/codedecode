import random
def cbase(x, base): #must have three digits
    pass
zeroes = 'X~CBV'.split('')
ones = 'c{`HW'.split('')
twos = 'F/PoZ'.split('')
threes = 'Q|xvy'.split('')
fours = '_rfuG'.split('')
fives = 'iJwtM'.split('')
sixes = '}bsLm'.split('')
numbers = {0:zeroes, 1:ones, 2:twos, 3:threes, 4:fours, 5:fives, 6:sixes}
lines = [line.rstrip('\n') for line in open('test.txt')]
message = ''


numberss={}
for num in zeros:
    numberss [num] = "0"
for num in ones:
    numberss [num] = "1"
for num in twos:
    numberss [num] = "2"
for num in threes:
    numberss [num] = "3"
for num in fours:
    numberss [num] = "4"
for num in fives:
    numberss [num] = "5"
for num in sixes:
    numberss [num] = "6"


#missing newline addition right now
for line in lines:
    string = ''
    for char in line:
        num = ord(char)
        digits = cbase(num, 7).split('') #change base, split into list of individual charecters
        for dgt in digits:
            dgt = int(dgt)
            string += numbers[digit][random.randint(0,4)]
    message += string
print message


decodeddd = ""


#decoding
for char in message:
    n = numberss [char]
    decodeddd += n
decodedList = [decodeddd[i:i+3] for i in range(0, len(line), 3)]


    
    #figure out which list it's in
    #transform to number
    #convert to base 10, use ord()
