def sumar(lista):
    suma=0;
    for e in lista:
        suma=suma+e;
    return suma

numeros=[]
numero=""

while numero!="salir":
    numero=input("Nuevo numero: ");
    if(numero!="salir"):
        numeros.append(int(numero));
    

print(sumar(numeros))
