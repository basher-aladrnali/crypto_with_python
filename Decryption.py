"""
CAESER CIPHER ENCRYPTION/DECRYPTION
AUTHER: MO BASHER

"""
letters = "abcdefghijklmnopqrstuvwxyz"

#dncryption

def decrypt(ciphertext, key):
#check
    assert key > 0
    
    ciphertext = ciphertext.lower()
    
    plaintext= ''

#process    
    for letter in ciphertext:
#skip
        if letter not in letters:
            plaintext += letter
        else:
            plaintext += letters[(letters.index(letter) + key)%26]
#output

    return plaintext

#input
print()
print("Do ypu want to Dncrypt ? ")
user_input=input("Y/N:  ").upper()
if user_input == "Y":
    print()
    key = int(input("Enter the key: "))
    ciphertext = input("Enter the text to Encrypt: ")
    print(decrypt(ciphertext, key))
else:
    print("OK BRO")
