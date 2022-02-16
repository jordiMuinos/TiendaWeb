palabras=[]
palabra="";

while palabra!="salir":
    palabra=input("Nueva palabra: ");
    if(palabras!="salir"):
        palabras.append(palabra);

contador={}

for p in palabras:
    if p in contador.keys():
        contador[p]+=1
    else:
        contador[p]=1


print(contador)



    
