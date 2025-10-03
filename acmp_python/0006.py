def getLetterInt(letter):
    if letter == 'A':
        return 1 
    if letter == 'B':
        return 2 
    if letter == 'C':
        return 3 
    if letter == 'D':
        return 4 
    if letter == 'E':
        return 5 
    if letter == 'F':
        return 6 
    if letter == 'G':
        return 7 
    if letter == 'H':
        return 8
    return 0


def decode(move): 
    if len(move) != 5:
        return 'ERROR'

    fromX = move[0]
    fromY = move[1]
    sep = move[2]
    toX = move[3]
    toY = move[4]

    if sep != '-':
        return 'ERROR'

    fromXint = getLetterInt(fromX)
    if not (fromXint in range(1,9)):
        return 'ERROR'

    fromYint = int(fromY)
    if not (fromYint in range(1,9)):
        return 'ERROR'

    toXint = getLetterInt(toX)
    if not (toXint in range(1,9)):
        return 'ERROR'

    toYint = int(toY)
    if not (toYint in range(1,9)):
        return 'ERROR'
    
    if (abs(fromXint-toXint) == 1 and abs(fromYint-toYint) == 2) or ((abs(fromXint-toXint) == 2 and abs(fromYint-toYint) == 1)):
        return 'YES'
    else:
        return 'NO'


move = input()
print(decode(move))
