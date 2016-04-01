import random
CIPHER = {}
LETTERS = "qwertyuiopasdfghjklzxcvbnm 1234567890"
MSG = "this is an encryption message"
def init():
    global CIPHER
    letter_list = list(LETTERS)
    random.shuffle(letter_list)
    for letter in LETTERS:
        CIPHER[letter] =letter_list.pop()


def encode():
    enc =""
    for ch in MSG:
        enc += CIPHER[ch]
    return enc
def decode(message):
    result =""
    for ch in message:
        for key,value in CIPHER.items():
            if ch == value:
                result += key
    return result

init()
print MSG
print encode()
print decode(encode())
#print CIPHER
