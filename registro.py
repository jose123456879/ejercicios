oo="si"
lista_de_estuduantes=[ ]
lista_notas=[ ]

while oo=="si":
	print("1. crear estuduante \n 2. ingrese nota \n 3. reporte de notas \n 4. salir")
	opc=int(input("elija una opcion: "))
	if opc==1:
		e=input("ingrese un nombre:" )
		lista_de_estuduantes.append(e)
	if opc==2:
		nota=int(input("ingrese una nota: "))
		lista_notas.append(nota)
	if opc==3:
		notas_estudiante={
		"Alumno":"lista_de_estuduantes[e]",
		"notas":"lista_notas[nota]"
		}
		print(notas_estudiante)

	oo=input("desea continuar?")