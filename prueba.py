from maximo import maximo
opc="si"
lista=[]
while opc=="si":
	n=int(input("ingrese: "))
	lista.append(n)
	opc=input("desea continuar? ")
print(maximo(lista))	