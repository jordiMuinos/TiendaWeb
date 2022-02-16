palabras=[]
palabra="";
temp="";
while palabra!="salir":
    palabra=input("Nueva palabra: ");
    if(palabras!="salir"):
        palabras.append(palabra);

contador={}

for p in palabras:
    if p not in contador.keys():
        contador[p]=palabras.cont(p);

print(contador)