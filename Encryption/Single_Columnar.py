def split_len(seq, length):
    return [seq[i:i + length] for i in range(0, len(seq), length)]


def encrypt():
    print("You are using Single Columnar Encryption")
    plaintext=input('Enter your Plain Text: ')
    key=input('Enter your Key: ')
    a=(split_len(plaintext, len(key)))
    
    order = {
      int(val): num for num, val in enumerate(key)
   }
    ciphertext = ''

    for index in sorted(order.keys()):
        for part in split_len(plaintext, len(key)):
            try:ciphertext += part[order[index]]
            except IndexError:
                continue
    print("Your Cipher text is: "+ciphertext)

def decrypt():
    print("You are using Single Columnar Decryption")
    import math
    cipher=input('Enter your Cipher Text: ')
    key=input('Enter your KeY: ')
    msg = ""
    k_indx = 0
    msg_indx = 0
    msg_len = float(len(cipher))
    msg_lst = list(cipher)
    col = len(key)
    row = int(math.ceil(msg_len / col))
    key_lst = sorted(list(key))
    dec_cipher = []
    for _ in range(row):
        dec_cipher += [[None] * col]

    for _ in range(col):
        curr_idx = key.index(key_lst[k_indx])
  
        for j in range(row):
            dec_cipher[j][curr_idx] = msg_lst[msg_indx]
            msg_indx += 1
        k_indx += 1
    try:
        msg = ''.join(sum(dec_cipher, []))
    except TypeError:
        raise TypeError("This program cannot",
                        "handle repeating words.")
  
    null_count = msg.count('_')
  
    if null_count > 0:
        return msg[: -null_count]
  
    print("Your Message is: "+msg)
