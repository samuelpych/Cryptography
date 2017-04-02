"""
cryptography.py
Author: Sam
Credit: Dave Wilson, Earl

Assignment:

Write and submit a program that encrypts and decrypts user data.

See the detailed requirements at https://github.com/HHS-IntroProgramming/Cryptography/blob/master/README.md
To get a character's numeric representation, find the index of that character in the string 
(use the code associations.find(char) to get the index of char's first occurrence in associations)
To get a character back from this numeric representation, get the character at that number's index 
in the string (using associations[index]).
MUST ENCRYPT AND DECRYPT 
"""
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
repeatasoc="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 .,:;'\"/\\<>(){}[]-=_+?!abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 .,:;'\"/\\<>(){}[]-=_+?!"
order=str(input("Enter e to encrypt, d to decrypt, or q to quit: "))
while order  not in ["q"]:
    if order =="e":
        one=input("Message: ")
        message=list(one)
        decode=input("Key: ")
        key= list(decode)
        for a in range(0, len(message)):
            message[a]=associations.find(message[a])
        for a in range(0, len(key)):
            key[a]=associations.find(key[a])
        while len(key)<len(message):
            key.extend(key)
        ab=[a+b for a,b in zip(message, key)]
        for a in range(0, len(message)):
            thingy=repeatasoc[ab[a]]
            print(thingy,end="")
        print( )
    if order=="d":
        listmsg=input("Message: ")
        message=list(listmsg)
        key1=input("Key: ")
        key= list(key1)
        for a in range(0, len(message)):
            message[a]=associations.find(message[a])
        for a in range(0, len(key)):
            key[a]=associations.find(key[a])
        while len(key)<len(message):
            key.extend(key)
        ab=[a-b for a,b in zip(message, key)]
        for a in range(0, len(message)):
            thingy=repeatasoc[ab[a]]
            print(thingy,end="")
        print( )
    else:
        print("Did not understand command, try again.")
    order=input("Enter e to encrypt, d to decrypt, or q to quit: ")
if order=="q":
        print("Goodbye!")
        
        

"""
must convert characters to numbers and back before actual math
"""
