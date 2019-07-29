#!/usr/bin/env python
# -*- coding: utf-8 -*-
archivo = open("./input.htm", "tr")
datos = ""
resultados = []

for linea in archivo.readlines():
    datos += linea
archivo.close()


todos = ['Alio', 'javi c.', 'RauL', 'Dani Sanchez B', 'Ruby', 'Adrian Rodriguez Besoy',
         'Potes', 'Roberto Argaña', 'im mvp', 'Pablo', 'lombra', 'RAGNAR LODBROK']
grupoA = ['Alio', 'javi c.', 'RauL']
grupoB = ['Dani Sanchez B', 'Ruby', 'Adrian Rodriguez Besoy']
grupoC = ['Potes', 'Roberto Argaña', 'im mvp']
grupoD = ['RAGNAR LODBROK', 'Pablo', 'lombra']
grupos = [grupoA, grupoB, grupoC, grupoD]


datos = datos[datos.find('user-list'):]
clasificacionFinal = []

def caparDatosParaJornada():
    global datos
    corte = datos.find('<div class="panel panel-gameweek standings-private" style="display: block;">')
    datos = datos[corte:]

def encuentraDatos(datos):
    name = ''
    points = ''
    jugadores = ''
    for jugador in todos:
        posAName = datos.find('data-title="')+12
        posBName = datos.find('><div class="position')-1
        name = datos[posAName:posBName]

        posAJugadores = datos.find('<div class="played">')+20
        posBJugadores = datos.find('</div></div><div class="points">')-9
        jugadores = datos[posAJugadores:posBJugadores]

        posAPoints = datos.find('</div></div><div class="points">')+32
        posBPoints = datos.find('<span>pts</span></div></a>')-1
        points = datos[posAPoints:posBPoints]

        datos = datos[posBPoints+28:]
        resultados.append(
            {'nombre': u''+name, 'puntos': points, 'jugadores': jugadores})


def compruebaIntegrantes(integrantes):
    for jugador in resultados:
        if (integrantes.index(jugador.get('nombre')) < 0):
            print('####################################################')
            print(jugador.get('nombre')+' no se encuentra en la clasificacion')
            print('####################################################')
            return 0
    return 1


def generaResultados():
    for grupo in grupos:
        puntosTotales = 0
        jugadoresTotales = 0
        NombreConjunto = ""
        for jugador in grupo:
            for coincidencia in resultados:
                if(coincidencia.get('nombre') == jugador):
                    puntosTotales += int(coincidencia.get('puntos'))
                    jugadoresTotales += int(coincidencia.get('jugadores'))
                    NombreConjunto += " | "+coincidencia.get('nombre')
        # print(NombreConjunto+"\n Puntos:"+str(puntosTotales)+"\n Valor de Equipo:"+str(jugadoresTotal))
        # print("----------------------------------------")

        clasificacionFinal.append({'nombre': NombreConjunto+" |", 'puntos': str(
            puntosTotales), 'jugadores': str(jugadoresTotales)+"/33 jugadores"})


def ordenaResultados():
    global clasificacionFinal
    clasificacionFinal=sorted(
        clasificacionFinal, key=lambda elem: elem['puntos'], reverse=True)


def imprimeResultados():
    global clasificacionFinal
    print(' ')
    i=1
    for elem in clasificacionFinal:
        print(str(i)+'º ### '+elem['nombre']+' ####')
        print('Puntos: '+elem['puntos']+' pts')
        print('Valor de Equipo:  '+elem['jugadores'])
        print('----------------------------------------')
        i += 1


def escribeResultados():
	global clasificacionFinal
	f=open('result.html', 'w')
	cabecera='<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><meta http-equiv="X-UA-Compatible" content="ie=edge"><link rel="stylesheet" type="text/css" href="result.css"><title>Clasificación Trapis-League</title></head><body><div class="listInside"><ul class="user-list">'
	footer='</ul></div></body></html>'
	contenido=''
	i=1
	for elem in clasificacionFinal:
		contenido1='<li><div class="user-row"><div class="btn btn-sw-link user" href="users/5092913/alio" data-title="Alio"><div class="position">'+str(i)+'º</div><div class="pic" style="background-color: #E57373"><span class="nombre-grupo"></span></div><div class="name"><h2 class="size">' + \
            elem['nombre']+'</h2><div class="played">'+elem['jugadores'] + \
            '</div></div><div class="points">' + \
            elem['puntos']+'<span>pts</span></div></div></div></li>'
		i += 1
		contenido += contenido1
	completo=''+cabecera+contenido+footer
	f.write(completo)
	f.close()

caparDatosParaJornada()
encuentraDatos(datos)
if(compruebaIntegrantes(todos)):
    compruebaIntegrantes(todos)
    generaResultados()
    ordenaResultados()
    escribeResultados()
