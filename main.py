# ler arquivo; string única com todos os caracteres
input = ''.join(open('code.txt', 'r').readlines())

# checar se o caractere é letra ou underline
def isLetter(char):
  if 'a' <= char <= 'z' or 'A' <= char <= 'Z' or char == '_':
    return True
  return False

# checar se o caractere é dígito
def isDigit(char):
  if '0' <= char <= '9':
    return True
  return False

# checar se o conteúdo é palavra reservada
def isReserved(content):
  if content in ['int', 'float', 'print', 'if', 'else']:
    return True
  return False

# checar se o caractere é ponto-e-vírgula
def isDelimiter(char):
  if char == ';':
    return True
  return False

# checar se o caractere é parênteses
def isParenthesis(char):
  if char in ['(', ')']:
    return True
  return False

# checar se o caractere é sinal de igual
def isAssign(char):
  if char == '=':
    return True
  return False

# checar se o caractere é operador matemático
def isMath(char):
  if char in ['+', '-', '*', '/']:
    return True
  return False

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