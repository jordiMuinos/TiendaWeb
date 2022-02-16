palabras=[]
palabra="";
temp="";
while palabra!="salir":
    palabra=input("Nueva palabra: ");
    palabras.append(palabra);
palabras.remove("salir")
temp=palabras[0]

for p in palabras:
    if len(p)<len(temp):
        temp=p

print(temp);