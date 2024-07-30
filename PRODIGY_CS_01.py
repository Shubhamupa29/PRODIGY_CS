def encrypt(Original_text, key):
    alphabets = 'abcdefghijklmnopqrstuvwxyz'
    encrypted_text=''
    for l in Original_text:
        l=l.lower()
        if l != ' ':
            index=alphabets.find(l)
            if index==-1:
                encrypted_text+=l
            else:
                new_index=index+key
                if new_index>=26:
                    new_index-=26
                encrypted_text+=alphabets[new_index]
    return encrypted_text

def decrypt(Original_text, key):
    alphabets = 'abcdefghijklmnopqrstuvwxyz'
    Original_text=Original_text.lower()
    decrypted_text=''
    for l in Original_text:
        l = l.lower()
        if l != ' ':
            index = alphabets.find(l)
            if index == -1:
                decrypted_text += l
            else:
                new_index = index - key
                if new_index <0:
                    new_index += 26
                decrypted_text += alphabets[new_index]
    return decrypted_text

Original_text=input("Enter original text::")
choice= input("Enter the choice to D:Decrypt or E:Encrypt ::")
if choice=='D':
    print("--Decryption Operation Selected--")
    print()
    key=int(input("Enter the key::"))
    print("Original Text::",Original_text)
    print("Decrypted text::",decrypt(Original_text,key))
elif choice=='E':
    print("--Encryption Operation Selected--")
    print()
    key = int(input("Enter the key::"))
    print("Original Text::", Original_text)
    print("Encrypted text::", encrypt(Original_text, key))
else:
    print('Invalid Choice')
