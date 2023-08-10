from controller import isLetter, isDigit, isReserved, isDelimiter, isParenthesis, isAssign, isMath


def Scanner(input):
    state = 0
    pos = 0
    content = ''
    
    while pos < len(input):
        char = input[pos]
        match state:
            case 0:
                if isLetter(char):
                    content += char
                    state = 1
                elif isDigit(char):
                    content += char
                    state = 2
                elif isDelimiter(char):
                    print('; -> DELIMITER')
                elif isParenthesis(char):
                    print('%c -> PARENTHESIS'%(char))
                elif isAssign(char):
                    print('= -> ASSIGN')
                elif isMath(char):
                    print('%c -> MATH_OP'%(char))
            case 1:
                if isLetter(char) or isDigit(char):
                    content += char
                elif isReserved(content):
                    print("%s -> RESERVED"%(content))
                    state = 0
                    content = ''
                    pos -= 1
                else:
                    print("%s -> IDENTIFIER"%(content))
                    state = 0
                    content = ''
                    pos -= 1
            case 2:
                if isDigit(char):
                    content += char
                else:
                    print("%s -> NUMBER  "%(content))
                    state = 0
                    content = ''
                    pos -= 1
        pos += 1