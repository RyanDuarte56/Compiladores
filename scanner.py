from controller import isLetter, isDigit, isReserved, isDelimiter, isParenthesis, isEqualSign, isGreaterSign, isLessSign, isExclamationSign, isMath, isDot, isHash, isSpace

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
                elif isDigit(char) or isDot(char):
                    content += char
                    state = 2
                elif isEqualSign(char):
                    content += char
                    state = 3
                elif isExclamationSign(char):
                    content += char
                    state = 4
                elif isGreaterSign(char) or isLessSign(char):
                    content += char
                    state = 5
                elif isHash(char):
                    state = 6
                elif isDelimiter(char):
                    print('; -> DELIMITER')
                elif isParenthesis(char):
                    print('%c -> PARENTHESIS'%(char))
                elif isMath(char):
                    print('%c -> MATH_OP'%(char))
                elif isSpace(char):
                    pos += 1
                    pass
            case 1:
                if isLetter(char) or isDigit(char):
                    content += char
                elif isReserved(content):
                    print('%s -> RESERVED'%(content))
                    state = 0
                    content = ''
                    pos -= 1
                else:
                    print('%s -> IDENTIFIER'%(content))
                    state = 0
                    content = ''
                    pos -= 1
            case 2:
                if isDigit(char) or isDot(char):
                    content += char
                else:
                    print('%s -> NUMBER'%(content))
                    state = 0
                    content = ''
                    pos -= 1
            case 3:
                if isEqualSign(char):
                    content += char
                    print('%s -> REL_OP'%(content))
                    state = 0
                    content = ''
                else:
                    print('%s -> ASSIGN'%(content))
                    state = 0
                    content = ''
                    pos -= 1
            case 4:
                if isEqualSign(char):
                    content += char
                    print('%s -> REL_OP'%(content))
                    state = 0
                    content = ''
            case 5:
                if isEqualSign(char):
                    content += char
                    print('%s -> REL_OP'%(content))
                    state = 0
                    content = ''
                else:
                    print('%s -> REL_OP'%(content))
                    state = 0
                    content = ''
                    pos -= 1
            case 6:
                if char == '\n':
                    state = 0
        pos += 1
