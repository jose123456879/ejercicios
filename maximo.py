def maximo(lista):
	if len(lista)==1:
		return lista[0]
	sublista=lista[1:]
	submax= maximo.sublista
	if lista[0] > submax:
		return lista[0]
	else:
		return submax 		
	