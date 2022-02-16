palabras=[]
palabra="";
temp="";
while palabra!="salir":
    palabra=input("Nueva palabra: ");
    palabras.append(palabra);
palabras.remove("salir")
temp=""

for i,p in enumerate(palabras):
    if len(p)<len(temp) or temp=="":
        temp=p

print(temp);