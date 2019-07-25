archivo = open("./input.htm", "tr")
datos = ""
resultados = [] 

for linea in archivo.readlines():
    datos += linea
    # if(linea.find())
archivo.close()


todos = ['Alio','javi c.','RauL','Dani Sanchez B','Ruby','Adrian Rodriguez Besoy','Potes','Roberto Argaña','im mvp','RAGNAR LODBROK','Pablo','lombra']
grupoA = ['Alio','javi c.','RauL']
grupoB = ['Dani Sanchez B','Ruby','Adrian Rodriguez Besoy']
grupoC = ['Potes','Roberto Argaña','im mvp']
grupoD = ['RAGNAR LODBROK','Pablo','lombra']

datos = datos[datos.find('user-list'):]
# encuentraDatos(todos)

# print(datos)
# print("-------------------------------------")

def encuentraDatos(datos):
    name = ''
    points = ''
    money = ''
    for jugador in todos:
        posAName = datos.find('data-title="')+12
        posBName = datos.find('><div class="position')-1
        name = datos[posAName:posBName]

        posAMoney= datos.find('<div class="played">')+20
        posBMoney = datos.find('</div></div><div class="points">')-1
        money = datos[posAMoney:posBMoney]

        posAPoints = datos.find('</div></div><div class="points">')+32
        posBPoints= datos.find('<span>pts</span></div></a>')-1
        points = datos[posAPoints:posBPoints]

        datos = datos[posBPoints+28:]
        resultados.append({'nombre': name, 'puntos':points, 'valorEquipo':money})


def compruebaIntegrantes(integrantes):
    for jugador in integrantes:
        if jugador not in datos:
            print('####################################################')
            print(jugador+' no se encuentra en el documento')
            print('####################################################')
            return 0
    return 1

def imprimeResultados():
    for player in resultados:
        print(player['nombre'])
        print(player['puntos'])
        print(player['valorEquipo'])
        print('-------------')


if(compruebaIntegrantes):
    compruebaIntegrantes(todos)
    encuentraDatos(datos)
    imprimeResultados()