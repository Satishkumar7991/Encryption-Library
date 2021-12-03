def encrypt():
    print("You are using Ceaser Cipher Encryption")
    text=input("Enter Your Message: ")
    shift=int(input("Enter Your Key: "))
    encrypt =''
    for i in range(len(text)):
        char = text[i]
        if(char.isupper()):
            encrypt +=chr((ord(char)+ shift-65)%26+ 65)
        else:
            encrypt +=chr((ord(char)+ shift-97)%26+ 97)
    print("Encrypted Message is: "+encrypt)

def decrypt():

    print("You are using Ceaser Cipher Decryption")
    text=input("Enter Your Ciphered Message: ")
    shift=int(input("Enter Your Key: "))
    plane_text=''
    for i in range(len(text)):
        char = text[i]
        if(char.isupper()):
            plane_text +=chr((ord(char)- shift-65)%26+ 65)
        else:
            plane_text +=chr((ord(char)- shift-97)%26+ 97)
    print("Your Message is: "+plane_text ) 