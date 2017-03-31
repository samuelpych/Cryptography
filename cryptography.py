"""
cryptography.py
Author: Sam
Credit: none yet

Assignment:

Write and submit a program that encrypts and decrypts user data.

See the detailed requirements at https://github.com/HHS-IntroProgramming/Cryptography/blob/master/README.md
To get a character's numeric representation, find the index of that character in the string 
(use the code associations.find(char) to get the index of char's first occurrence in associations)
To get a character back from this numeric representation, get the character at that number's index 
in the string (using associations[index]).
MUST ENCRYPT AND DECRYPT 
"""
associations = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 .,:;'\"/\\<>(){}[]-=_+?!"
key=input("Key: ")
letter=input("Enter e to encrypt, d to decrypt, or q to quit: ")
instruction=input("Message: ")
def encrypt(message, key, process):
     messnum = [associations.find(x) for x in message]
     keynum = [associations.find(x) for x in key]
     keynum = keynum*(len(messnum)//len(keynum))+keynum[:len(messnum)%len(keynum)]
     keynum = [process*x for x in keynum]
     emess = [sum(x) for x in zip(messnum, keynum)]
     emess = ''.join([associations[x%len(associations)] for x in emess])
     print(emess)
      
process = "a"
process = input("Enter e to encrypt, d to decrypt, or q to quit: ")
        print("Goodbye!")
while process != "q":
    if process == "e":
        message = input("Message: ")
        key = input("Key: ")
        encrypt(message, key, 1)
    elif process == "d":
        message = input("Message: ")
        key = input("Key: ")
        encrypt(message, key, -1)
    else:
        print("Did not understand command, try again.")
if process == "q":
        print("Goodbye!")
associations[index]
"""
must convert characters to numbers and back before actual math
"""