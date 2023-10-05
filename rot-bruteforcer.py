'''
Caesar/ROT Cipher Brute-Forcer
Author: mo basher
'''


alphabet = 'abcdefghijklmnopqrstuvwxyz'

#---- INPUT ----#
ciphertext = input("enter your ciphertext: ")
key = int(input("enter your key: "))


#---- PROCESS ----#
def caesar_decrypt(ciphertext, key): # input
    # check key is an integer and is > 0
    # assert --> make sure
    assert key > 0

    ciphertext = ciphertext.lower()
    plaintext = ''

    for state in ciphertext:
        # skip special characters
        if state not in alphabet:
            plaintext += state
        else:
            plaintext += alphabet[ (alphabet.index(state) - key)%25 ] # use mod to keep the alphabet field of 24

    return plaintext

def bruteforce(ciphertext):
    for i in range(1, 25):
        print(i,":", caesar_decrypt(ciphertext, i))

#---- OUTPUT ----#
bruteforce(ciphertext)
