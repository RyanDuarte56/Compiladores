from controller import isLetter, isDigit, isReserved, isDelimiter, isParenthesis, isAssign, isMath
from scanner import Scanner

# ler arquivo; string única com todos os caracteres
input = ''.join(open('code.txt', 'r').readlines())
Scanner(input)
