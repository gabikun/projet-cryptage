f=open('messageacry-césar.txt','r')
msg=f.read()
f.close

cle=int(input("choisissez votre clé"))
print (msg)
print (cle)
msgcrypte=""
for i in range (len(msg)):
    print (ord(msg[i]))
    a=ord(msg[i])
    if a==32 or a==10:
        msgcrypte=msgcrypte
    else:
        a=a-97
        a=a+cle
        b=a%26
        print (chr(b+97))
        msgcrypte=msgcrypte+(chr(b+97))
print(msgcrypte)

fcrypte=open('message-crypté-césar.txt','w')
fcrypte.write(msgcrypte)
fcrypte.close()
