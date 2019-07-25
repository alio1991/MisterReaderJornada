#!/usr/bin/env python
# -*- coding: utf-8 -*-
archivo = open("./input.htm", "tr")
datos = ""
resultados = [] 

for linea in archivo.readlines():
    datos += linea
    # if(linea.find())
archivo.close()


todos = ['Alio','javi c.','RauL','Dani Sanchez B','Ruby','Adrian Rodriguez Besoy','Potes','Roberto ArgaÃ±a','im mvp','Pablo','lombra']#,'RAGNAR LODBROK']
grupoA = ['Alio','javi c.','RauL']
grupoB = ['Dani Sanchez B','Ruby','Adrian Rodriguez Besoy']
grupoC = ['Potes','Roberto ArgaÃ±a','im mvp']
grupoD = ['Pablo','lombra']
grupos = [grupoA,grupoB,grupoC,grupoD]
# grupoD = ['RAGNAR LODBROK','Pablo','lombra']

datos = datos[datos.find('user-list'):]
clasificacionFinal = []

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
        resultados.append({'nombre': u''+name, 'puntos':points, 'valorEquipo':money})


def compruebaIntegrantes(integrantes):
    for jugador in resultados:
        if (integrantes.index(jugador.get('nombre'))<0):
            print('####################################################')
            print(jugador.get('nombre')+' no se encuentra en la clasificacion')
            print('####################################################')
            return 0
    return 1
    


def generaResultados():
    for grupo in grupos:
        puntosTotales = 0
        valorEquipoTotal = 0
        NombreConjunto = ""
        for jugador in grupo:
            for coincidencia in resultados:
                if(coincidencia.get('nombre') == jugador):
                    puntosTotales += int(coincidencia.get('puntos'))
                    valorEquipoTotal += float(coincidencia.get('valorEquipo')[0:6])
                    NombreConjunto += " | "+coincidencia.get('nombre')
        # print(NombreConjunto+"\n Puntos:"+str(puntosTotales)+"\n Valor de Equipo:"+str(valorEquipoTotal))
        # print("----------------------------------------")

        clasificacionFinal.append({'nombre': NombreConjunto+" |", 'puntos':str(puntosTotales), 'valorEquipo':str(valorEquipoTotal)})

def ordenaResultados():
    global clasificacionFinal
    clasificacionFinal = sorted(clasificacionFinal, key=lambda elem: elem['valorEquipo'], reverse=True)
    clasificacionFinal = sorted(clasificacionFinal, key=lambda elem: elem['puntos'], reverse=True)


def imprimeResultados():
    global clasificacionFinal
    for elem in clasificacionFinal:
        print('##### '+elem['nombre']+' ####')
        print('Puntos: '+elem['puntos'])
        print('Valor de Equipo:  '+elem['valorEquipo'])
        print('----------------------------------------')



encuentraDatos(datos)
if(compruebaIntegrantes(todos)):
    compruebaIntegrantes(todos)
    generaResultados()
    ordenaResultados()
    imprimeResultados()
