#ENCRYPTER PROGRAM

outerwheel="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
innerwheel="abcdefghijklmnopqrstuvwxyz"
size=len(outerwheel)
ciphertext = ""
plaintext = ""
encrypting=True
keyword=input("Enter the keyword you would like to use: ")
lenkey=len(keyword)
plaintext=input("Enter the code you would like to encrypt: ")
length = len(plaintext)
indx = input("Enter the letter index you would like to use: ")

def setinner(capital, index, outerwheel, innerwheel):
    idxpos=0
    for idx in range(len(innerwheel)):
	    if index == innerwheel[idx]:
		    idxpos = idx
    Lfirst = innerwheel[0:idxpos]
    Lsecond = innerwheel[idxpos:]
    innerwheel= Lsecond + Lfirst
    newpos=0
    for cap in range(len(outerwheel)):
	    if capital == outerwheel[cap]:
		    newpos = cap
    back = size - newpos
    Rfirst = innerwheel[0:back]
    Rsecond = innerwheel[back:]
    innerwheel= Rsecond + Rfirst
    return(innerwheel)

for i in range(length):
    keydex=keyword[i%lenkey]
    innerwheel=setinner(keydex,indx,outerwheel,innerwheel)
    if plaintext[i].isupper():
        for capital in range(size):
            if plaintext[i]==outerwheel[capital]:
                ciphertext+=innerwheel[capital]
    elif plaintext[i].islower():
        for capital in range(size):
            if plaintext[i]==innerwheel[capital]:
                ciphertext+=outerwheel[capital]

print("Your ciphertext is {}".format(ciphertext))
