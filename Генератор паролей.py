from random import *
digits= '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters =  'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
chars = ''
print('Укажите количество паролей для генерации')
while True:
    n=input()
    if str(n).isdigit()==True and int(n)>0:    
        n=int(n)
        break
    else:
        print('Введите целое число больше нуля')
        continue
print('Укажите длину паролей')
while True:
    le=input()
    if str(le).isdigit()==True and int(le)>0:
            le=int(le)
            break
    else:
        print('Укажите длину больше нуля')

print('Пароль должен содержать цифры?   Да\Нет')
if input().lower()=='да':
    chars += digits
print('Пароль должен содержать сторчные буквы?   Да\Нет')
if input().lower()=='да':
    chars += lowercase_letters
print('Пароль должен содержать прописные буквы?   Да\Нет')
if input().lower()=='да':
    chars += uppercase_letters
print('Пароль должен содержать спец символы?   Да\Нет')
if input().lower()=='да':
    chars += punctuation
def generate_password(le, chars):
    password = ''
    for i in range(int(le)):
        password += choice(chars) 

    print(password)
for u in range(n):
    generate_password(le, chars)
