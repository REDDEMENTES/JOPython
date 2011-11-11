#Variables Globales
v =[] #Vertices
p = [] # Punto a buscar
b = [] # Lista para guardar el bounding

entrada= 0 # Variable para manejar el menu

#Definicion de funciones
def leer_poligono():
	#Funcion que lee del archivo poligono.txt
	#los puntos (x,y) y los retorna en una lista
	#de la forma [(x,y),(x,y)]
	f = open("poligono.txt")
	lines = f.readlines()
	f.close
	vertices=[]
	for l in lines:
		vertices.append((l[1],l[3]))
	return vertices

def leer_punto():
	#Funcion que el el punto (x,y) del archivo
	#punto.txt el cual se utiliza en la funcion
	#in_bounding para conocer si se encuentra dentro
	f = open("punto.txt")
	l= f.readline()
	punto=[]
	punto.append((l[0],l[2]))
	return punto

def bounding_box(vertices):
	#Funcion que encuentra el boundingbox de los
	#vertices del poligono. Retorna una lista de la
	#forma [(xmin,xmax),(ymin,ymax)] que se encuentran
	#comparando el elemento x mayor y menor de la lista de
	#vertices
	vertices.sort()
	bound=[]
	bound.append((vertices[0][0],vertices[len(vertices)-1][0]))
	r = sorted(vertices, key=lambda axis: axis[1])
	bound.append((r[0][1],r[len(r)-1][1]))
	return  bound

def in_bounding(punto,bounding):
	#Funcion que analiza si el punto opntenido en leer_punto
	#se encuentra en el bounding que se calcula en la funcion
	#bounding_box
	if punto[0][0]>=bounding[0][0] and punto[0][0]<=bounding[0][1] and punto[0][1]>=bounding[1][0] and punto[0][1]<=bounding[1][1]:
		return True
	else:
		return False

#Programa Principal

print "1. Leer vertices de archivo poligono.txt"
print "2. Leer punto de archivo punto.txt"
print "3. Generar Bounding Box"
print "4. Comprobar punto dentro de bounding box"
print "5. Salir de la aplicacion"

while (entrada!=5):
	entrada = int(raw_input(">>"))
	if entrada == 1:
		v = leer_poligono()
	if entrada == 2:
		p = leer_punto()
	if entrada == 3:
		b = bounding_box(v)
	if entrada ==4:
		if in_bounding(p,b):
			print "El punto esta dentro"
		else:
			print "El punto no esta dentro"

