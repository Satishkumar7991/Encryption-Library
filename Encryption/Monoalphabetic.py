def KEY():
    Key=""
    check=True
    while(check):
        check = False
        print("Enter Your Key: ")
        while(len(Key)!=26):
            Key +=input()
            if(len(Key)>26):
                print("Invalid Key: Only 26 Characters are allowed")
                Key=""
            elif(len(Key)<26):
                print("Invalid Key: Key must have 26 Characters")
                Key=""

        for i in range(len(Key)):
            for j in range(i+1,len(Key)):
                if(Key[i]==Key[j]):
                    print("Invalid Key: No duplicate Characters are allowed")
                    Key=""
                    check = True
    return Key
def dictionary():
    dict={'a':'b'}
    Key=KEY()
    dict.update({chr(ord('a')+1):'a'})
    for i in range(len(Key)):
        dict.update({chr(ord('a')+i):Key[i]})
    return dict
def encrypt():

    print("You are using Monoalphabetic Encryption")
    plain_text=input("Enter  your Text: ")
    dict=dictionary()
    
            
    encrypted=''
    for j in plain_text:
        for i in dict.keys():
            if(i==j):
                encrypted +=dict[i]
    print("Encrypted Text is: "+encrypted)

def decrypt():
    print("You are using Monoalphaetic Decryption")
    dict=dictionary()
    cipher_text=input("Enter  your Ciphered Text: ")
    text=""
    for i in cipher_text:
        for key,value in dict.items():
            if(i==value):
                text +=key
    print('Your Plain text is: '+text)