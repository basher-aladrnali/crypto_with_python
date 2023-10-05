"""
CAESER CIPHER ENCRYPTION/DECRYPTION
AUTHER: MO BASHER

"""
letters = "abcdefghijklmnopqrstuvwxyz"

#encryption

def encrypt(plaintext, key):
#check
    assert key > 0
    
    plaintext = plaintext.lower()
    
    ciphertext= ''

#process    
    for letter in plaintext:
#skip
        if letter not in letters:
            ciphertext += letter
        else:
            ciphertext += letters[(letters.index(letter) + key)%26]
#output

    return ciphertext

#input
print()
print("Do ypu want to Encrypt ? ")
user_input=input("Y/N:  ").upper()
if user_input == "Y":
    print()
    key = int(input("Enter the key: "))
    plaintext = input("Enter the text to Encrypt: ")
    print(encrypt(plaintext, key))
else:
    print("OK BRO")
