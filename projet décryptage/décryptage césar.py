fcrypte=open('message-crypté-césar.txt','r')
msg=fcrypte.read()
fcrypte.close

cle=int(input("choisissez votre clé"))
print (msg)
print (cle)
msgdecrypte=""
for i in range (len(msg)):
    print (ord(msg[i]))
    a=ord(msg[i])
    a=a-97
    b=a-cle
    if b<0:
        b=b+26
        print (chr(b+97))
    msgdecrypte=msgdecrypte+(chr(b+97))
print(msgdecrypte)

fdecrypte=open('message-décrypté-césar.txt','w')
fdecrypte.write(msgdecrypte)
fdecrypte.close()
