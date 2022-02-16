palabras=[]
palabra="";
temp="";
while palabra!="salir":
    palabra=input("Nueva palabra: ");
    if(palabras!="salir"):
        palabras.append(palabra);

conjunto=set(palabras)


if(len(conjunto)<len(palabras)):
    print("Hay dupicados")
else:
    print("No hay duplicados")