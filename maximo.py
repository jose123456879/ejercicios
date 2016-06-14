def maximo(lista):
	if len(lista)==1:
		return lista[0]
	return lista[0] *maximo(lista[0:])	