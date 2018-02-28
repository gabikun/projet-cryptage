f=open('messageacry-affine.txt','r')
msg=f.read()
f.close

cle1=int(input("choisissez votre clé a"))
cle2=int(input("choisissez votre clé b"))
if cle1%2==0 or cle1==13 or cle2>=26:
    print ("Le cryptage est impossible, veuillez changer de clé 1")
else:
    print (msg)
    print (cle1)
    print (cle2)
    msgcrypte=""
    for i in range (len(msg)):
        print (ord(msg[i]))
        a=ord(msg[i])
        if a==32 or a==10:
            msgcrypte=msgcrypte
        else:
            a=a-97
            a=a*cle1
            a=a+cle2
            b=a%26
            print (chr(b+97))
            msgcrypte=msgcrypte+(chr(b+97))
    print(msgcrypte)

    fcrypte=open('message-crypté-affine.txt','w')
    fcrypte.write(msgcrypte)
    fcrypte.close()
