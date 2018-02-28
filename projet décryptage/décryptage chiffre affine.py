
fcrypte=open('message-crypté-affine.txt','r')
msg=fcrypte.read()
fcrypte.close

cle1=int(input("choisissez votre clé a"))
cle2=int(input("choisissez votre clé b"))
if cle1%2==0 or cle1==13 or 0>=cle2>=26 or 0>=cle1>=26:
    print ("Le cryptage est impossible, veuillez changer de clé 1")
else:
    print (msg)
    print (cle1)
    print (cle2)
    msgdecrypte=""
    for i in range (len(msg)):
        print (ord(msg[i]))
        a=ord(msg[i])
        a=a-97
        a=a-cle2
        if cle1==1:
            aprime=1
        elif cle1==3:
            aprime=9
        elif cle1==5:
            aprime=21
        elif cle1==7:
            aprime=15
        elif cle1==9:
            aprime=3
        elif cle1==11:
            aprime=19
        elif cle1==15:
            aprime=7
        elif cle1==17:
            aprime=23
        elif cle1==19:
            aprime=11
        elif cle1==21:
            aprime=5
        elif cle1==23:
            aprime=17
        elif cle1==25:
            aprime=25
        else:
            print ("problème de clé a")
        c=a*aprime
        b=c%26
        print (chr(b+97))
        msgdecrypte=msgdecrypte+(chr(b+97))
    print(msgdecrypte)

    fdecrypte=open('message-décrypté-affine.txt','w')
    fdecrypte.write(msgdecrypte)
    fdecrypte.close()
