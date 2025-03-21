texto=input("El texto que desee añadir para impresión: ")
if texto== texto.upper():
    abc="ABCDEFGHIJKLMNOPQRSTVXYZ"
else:
    abc="abcdefghijklmnopqrstuvwxyz"
k=int(input("Valor de desplazamiento "))
cifrad=""
for c in texto:
    if c in abc:
        cifrad+= abc[(abc.index(c)+k)%(len(abc))]
    else:
        cifrad+=c
print("Texto cifrado: ", cifrad)
                    
