from scanner import Scanner

# ler arquivo; string Ãºnica com todos os caracteres
input = ''.join(open('code.txt', 'r').readlines())
Scanner(input)