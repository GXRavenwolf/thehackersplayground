#DECRYPTER PROGRAM

outerwheel="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
innerwheel="abcdefghijklmnopqrstuvwxyz"
size=len(outerwheel)
ciphertext = ""
plaintext = ""
encrypting=True
keyword=input("Enter the keyword that was used: ")
lenkey=len(keyword)
ciphertext=input("Enter ciphered code: ")
length = len(ciphertext)
indx = input("Enter the letter index that was used: ")

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
    if ciphertext[i].islower():
        for lower in range(size):
            if ciphertext[i]==innerwheel[lower]:
                plaintext+=outerwheel[lower]
    if ciphertext[i].isupper():
        for upper in range(size):
            if ciphertext[i]==outerwheel[upper]:
                plaintext+=innerwheel[upper]

print("Your plaintext is {}".format(plaintext))
