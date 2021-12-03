def encrypt():
    print("You are using Rail Fence Encryption")
    s=input("Enter Your Text: ")
    k=int(input("Enter your key: "))
    enc=[[" " for i in range(len(s))] for j in range(k)]
    flag=0
    row=0
    for i in range(len(s)):
        enc[row][i]=s[i]
        if row==0:
            flag=0
        elif row==k-1:
            flag=1
        if flag==0:
            row+=1
        else:
            row-=1
    for i in range(k):
        print("".join(enc[i]))
    
    ct=[]
    for i in range(k):
        for j in range(len(s)):
            if enc[i][j]!=' ':
                ct.append(enc[i][j])    
        cipher="".join(ct)
    print("Cipher Text: ",cipher)        


def decrypt():
    print("You are using Rail Fence Decryption")
    cipher=input('Enter your Cipher Text: ')
    key=int(input('Enter Your Key: '))
    rail = [['\n' for i in range(len(cipher))] 
                  for j in range(key)]
    dir_down = None
    row, col = 0, 0
        
    for i in range(len(cipher)):
        if row == 0:
            dir_down = True
        if row == key - 1:
            dir_down = False
        rail[row][col] = '*'
        col += 1    
        if dir_down:
            row += 1
        else:
            row -= 1 
    index = 0
    for i in range(key):
        for j in range(len(cipher)):
            if ((rail[i][j] == '*') and
                (index < len(cipher))):
                rail[i][j] = cipher[index]
                index += 1


    result = []
    row, col = 0, 0
    for i in range(len(cipher)):
        if row == 0:
            dir_down = True
        if row == key-1:
            dir_down = False
        if (rail[row][col] != '*'):
            result.append(rail[row][col])
            col += 1
        if dir_down:
            row += 1
        else:
            row -= 1 

    print("".join(result))
