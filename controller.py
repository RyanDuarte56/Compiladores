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
def isEqualSign(char):
  if char == '=':
    return True
  return False

# checar se o caractere é sinal de maior
def isGreaterSign(char):
  if char == '>':
    return True
  return False

# checar se o caractere é sinal de menor
def isLessSign(char):
  if char == '<':
    return True
  return False

# checar se o caractere é sinal de exclamação
def isExclamationSign(char):
  if char == '!':
    return True
  return False

# checar se o caractere é operador matemático
def isMath(char):
  if char in ['+', '-', '*', '/']:
    return True
  return False

# checar se o caractere é ponto
def isDot(char):
  if char == '.':
    return True
  return False

# checar se o caractere é hashtag
def isHash(char):
  if char == '#':
    return True
  return False

# checar se o caractere é espaço ou quebra de linha
def isSpace(char):
  if char == ' ' or char == '\n':
    return True
  return False