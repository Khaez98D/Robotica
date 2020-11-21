#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os;
import sys;
import cv2;
import math;
import time;
import subprocess;
import numpy as np;
from heapq import heappop, heappush;
# from scipy.ndimage import gaussian_filter;

START = ();
END = ();

def app(griFile):
    #Obtener gridmap
	gridmap = cv2.imread(griFile);
	gridmap = cv2.blur(gridmap,(5,5));
	# gridmap = gaussian_filter(gridmap, sigma=2);
	gridmapN = cv2.imread(griFile, cv2.IMREAD_GRAYSCALE);
	gridmapN = 1 - gridmapN/255;
	height, width = gridmapN.shape;
	probFree = 0.8;

    # Crear grafo con el espacio vacío
	graph = gridmapToGraph(gridmapN, height, width, probFree);

	imgWinName = "Mapa del entorno";
	print("Aparecerá el mapa en la pantalla.\nPor favor seleccione la ubicación actual del robot");
	print("Posteriormente seleccione el destino deseado del robot. \n");
	time.sleep(2);

	def mouseHandler(event, x, y, flags, params):
		global START;
		global END;
		if event == cv2.EVENT_LBUTTONUP:
			if not START:
				cv2.circle(gridmap, (x,y), 10, (52, 232, 235), 2);
				cv2.circle(gridmap, (x,y), 2, (52, 232, 235), -1);
				cv2.imshow(imgWinName, gridmap);
				START = (y,x);
			elif not END and START:
				cv2.circle(gridmap, (x,y), 10, (52, 232, 0), 2);
				cv2.circle(gridmap, (x,y), 2, (52, 232, 0), -1);
				cv2.imshow(imgWinName, gridmap);
				END = (y,x);

	cv2.namedWindow(imgWinName);
	cv2.setMouseCallback(imgWinName, mouseHandler);

	terminoRuta = False;	# Bandera para saber que se ha encontrado una ruta
	puntos = [];			# Lista de puntos para completar la ruta

	while True:
        #Dibuja un nuevo frame
		cv2.imshow(imgWinName, gridmap);

        #Si hay interrupciones por ESC cierra el programa
		if cv2.waitKey(10) == 27:
			break;

        #Si ya se determinó los puntos de la ruta se guarda la imagen y se empieza el movimeinto
		if terminoRuta and puntos:
			#Cambio de archivo para guardar la ruta
			rutaFile = griFile.replace("gridmap.png", "ruta.png");
			cv2.imwrite(rutaFile, gridmap);
			print(puntos, "\n");
			print("Control de posición...");
			time.sleep(2);
			break;

        # Si ya se seleccionó el punto inicial y final se busca la ruta
		if START and END and not terminoRuta:
			print("Calculando ruta, por favor espere...")
			ruta = Astar(graph, START, END, gridmap, gridmapN, probFree);

        	#Si ya encontró la ruta se realiza ahora el control de posición punto a punto
			puntos = darPuntosRuta(ruta, 0.0046);
			terminoRuta = True;


	cv2.destroyAllWindows();
	return puntos;

def gridmapToGraph(gridmap, height, width, maxProbFree):
	graph = {(i, j): [] for j in range(width) for i in range(height) if gridmap[i][j]<maxProbFree}
	for row, col in graph.keys():
		if row < height - 1 and gridmap[row + 1][col]<maxProbFree:
			graph[(row, col)].append(("S", (row + 1, col)));
			graph[(row + 1, col)].append(("N", (row, col)));
		if col < width - 1 and gridmap[row][col + 1]<maxProbFree:
			graph[(row, col)].append(("E", (row, col + 1)));
			graph[(row, col + 1)].append(("W", (row, col)));

	return graph;

def heuristic(acc, end, gridmap, probFree):
	return ( (acc[0] - end[0])**2 + (acc[1] - end[1])**2 )**(1/2) - distanciaAObstaculo(acc, gridmap, probFree);

def distanciaAObstaculo(acc, gridmapN, probFree):
	row, col = acc;
	height, width = gridmapN.shape;
	dst = [0,0,0,0];
	for r in range(row, row+100):
		if r < height - 1:
			if gridmapN[r + 1][col]<probFree:
				dst[0] += gridmapN[r + 1][col]*50;
			else:
				break;

	for r in range(row, row-100, -1):
		if r - 1 > 0:
			if gridmapN[r - 1][col]<probFree:
				dst[1] += gridmapN[r - 1][col]*50;
			else:
				break;

	for c in range(col, col+100):
		if c + 1 < width:
			if gridmapN[row][c+1]<probFree:
				dst[2] += gridmapN[row][c+1]*50;
			else:
				break;

	for c in range(col, col-100, -1):
		if c - 1 > 0:
			if gridmapN[row][c-1]<probFree:
				dst[3] += gridmapN[row][c]*50;
			else:
				break;

	return min(dst);

def Astar(graph, START, END, gridmap, gridmapN, probFree):
	nodos = [];
	nodosV = set();
	heappush(nodos, (0 + heuristic(START, END, gridmapN, probFree), 0, START, ""));
	count = 0;

	while nodos:
        # Saco el nodo de menor costo en la lista
		nodoActual = heappop(nodos);

		#Comprueba que nodoActual no sea el nodoDestino, si lo es se retorna la ruta
		if nodoActual[2] == END:
			return nodoActual[3];

        #Si el nodo no ha sido visitado se agrega a la lista, se pinta en el mapa y se expande en sus vecinos
		if nodoActual[2] not in nodosV:
            # Se agrega a la lista de nodos visitados
			count += 1;
			nodosV.add(nodoActual[2]);

            # Se obtiene la mejor Ruta hasta este nodo, para añadirla a sus vecinos
			path = nodoActual[3];

            #Se pinta en el mapa
			gridmap[nodoActual[2]] = [255,0,0];

            # Se expande este nodo en sus vecinos
			for vecino in graph[nodoActual[2]]:
				costoN = nodoActual[1] + heuristic(vecino[1], END, gridmapN, probFree);
				costoT = nodoActual[1] + (gridmapN[nodoActual[2]]);
				heappush(nodos, (costoN, costoT, vecino[1], path+vecino[0]));

	print("NO HAY RUTA");
	return "NO HAY RUTA";

def darPuntosRuta(ruta, dim):
	puntos = [];
	x = 0.0;
	y = 0.0;
	if ruta == "NO HAY RUTA":
		raise NameError('HiThere');
	else:
		i = 0;
		while i < len(ruta):
			l = ruta[i];
			count = 1;
			
			if i+1 < len(ruta) and l == ruta[i+1]:
				for ls in range(i,len(ruta)):
					if ruta[ls] == l:
						count += 1;
					else:
						break;

				if l == 'N':
					x = x - count*dim;
				elif l == 'S':
					x = x + count*dim;
				elif l == 'W':
					y = y - count*dim;
				elif l == 'E':
					y = y + count*dim;

				i = i + count;


			elif i+3 < len(ruta) and ( (l + ruta[i+1]) == (ruta[i+2] + ruta[i+3]) ):
				ls = i+2;
				while ls < len(ruta):
					if ls+1 < len(ruta):
						if (l + ruta[i+1]) == (ruta[ls] + ruta[ls+1]):
							count += 1;
							ls += 2;
						else:
							break;
					else:
						break;

				if (l + ruta[i+1]) == 'NW':
					x = x - count*dim;
					y = y - count*dim;
				elif (l + ruta[i+1]) == 'NE':
					x = x - count*dim;
					y = y + count*dim;
				elif (l + ruta[i+1]) == 'SW':
					x = x + count*dim;
					y = y - count*dim;
				elif (l + ruta[i+1]) == 'SE':
					x = x + count*dim;
					y = y + count*dim;

				i = i + 2*count;

			else:
				if l == 'N':
					x = x - count*dim;
				elif l == 'S':
					x = x + count*dim;
				elif l == 'W':
					y = y - count*dim;
				elif l == 'E':
					y = y + count*dim;
				i += 1;

			puntos.append([x,y,0.0]);

		return puntos;

if __name__ == "__main__":
	try:
		name = "senecabot_navigator.py";
		path = os.path.abspath(__file__).replace("scripts"+os.path.sep+name, "results"+os.path.sep+"gridmap.png");
		puntos = app(path);

		puntos = str(puntos).replace("],", "];").replace("[[", "[").replace("]]","]");

		test = subprocess.Popen(["rosrun","taller4_4","senecabot_drawer.py", puntos], stdout=subprocess.PIPE);
		output = test.communicate()[0];
		print(output);
		
	except Exception as e:
		print("ERROR");
		raise

