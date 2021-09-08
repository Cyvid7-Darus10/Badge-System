from django.conf import settings

LETTERS = 'abcdefghijklmnopqrstuvwxyz@.abcdefghijklmnopqrstuvwxyz@.'
key = settings.ENCRYPT_KEY.split(',')

print(key)

def encrypt(message):
    encrypted = ''
    i = 0
    for chars in message:
        if chars in LETTERS:
            if i == len(key):
                i = 0
            num = LETTERS.find(chars)
            num += int(key[i])
            encrypted +=  LETTERS[num]
            print(key[i])
            i += 1

    return encrypted

def decrypt(message):
    encrypted = ''
    i = 0
    for chars in message:
        if chars in LETTERS:
            if i == len(key):
                i = 0
            num = LETTERS.find(chars)
            num -= int(key[i])
            encrypted +=  LETTERS[num]
            i += 1

    return encrypted