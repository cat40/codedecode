import random
def cbase(x): #must have three digits
    places = []
    n = 0
    while sum(places)*6 <= x:
        places.append(7**n)
        n += 1
    places = list(reversed(places))
    num = ''
    placeIndex = 0
   #print places
    while x > 0:
        #print x
        i=0
        place = places[placeIndex]
        while i < 7:
            #print x-place*i, i
            if x - place*i < place:
                num += str(i)
                x-=place*i
                placeIndex += 1
                break
            #x -= place*i
            i += 1
    num = '0'*(3-len(num)) + num
    return num
        
zeroes = list('X~CBV')
ones = list('c{`HW')
twos = list('F/PoZ')
threes = list('Q|xvy')
fours = list('_rfuG')
fives = list('iJwtM')
sixes = list('}bsLm')
numbers = {0:zeroes, 1:ones, 2:twos, 3:threes, 4:fours, 5:fives, 6:sixes}

numberss={}
for key, i in zip(numbers, (str(x) for x in range(0, 7))):
    for num in numbers[key]:
        numberss[num] = i
#print numberss
##        
##for num in zeros:
##    numberss [num] = "0"
##for num in ones:
##    numberss [num] = "1"
##for num in twos:
##    numberss [num] = "2"
##for num in threes:
##    numberss [num] = "3"
##for num in fours:
##    numberss [num] = "4"
##for num in fives:
##    numberss [num] = "5"
##for num in sixes:
##    numberss [num] = "6"


#missing newline addition right now
def encode(fname):
    message = ''
    #lines = [line.rstrip('\n') for line in open(fname)]
    lines = fname.split('\n')
    for line in lines:
        string = ''
        for char in line:
            num = ord(char)
            digits = list(cbase(num)) #change base, split into list of individual charecters
            for dgt in digits:
                dgt = int(dgt)
                string += numbers[dgt][random.randint(0,4)]
        message += string
    return message



#decoding
def decode(message):
    decodeddd = ''
    for char in message:
        n = numberss [char]
        decodeddd += n
    decodedList = [decodeddd[i:i+3] for i in range(0, len(decodeddd), 3)]
    decodeddd = ''
    for num in decodedList:
        decodeddd += chr(int(num, 7))
    return decodeddd
    
    #figure out which list it's in
    #transform to number
    #convert to base 10, use ord()
