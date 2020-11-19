#!/usr/bin/python3
# -*- coding: utf-8 -*-

import cv2;
import time;
import sys;
import os;
import math;
import numpy as np;
from heapq import heappop, heappush;
# from scipy.ndimage import gaussian_filter;

START = ();
END = ();

def app(griFile):
    #Obtener gridmap
    path = os.path.abspath(__file__).replace("scripts"+os.path.sep+__file__, "results"+os.path.sep+griFile);
    # print("Ruta: ", path);
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
    print("Aparecerá el mapa en la pantalla, por favor seleccione la ubicación actual del robot");
    print("Posteriormente seleccione el destino deseado del robot.");
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

    terminoRuta = False;

    while True:
        #Dibuja un nuevo frame
        cv2.imshow(imgWinName, gridmap);

        #Si hay interrupciones por ESC cierra el programa
        if cv2.waitKey(20) == 27:
            break;

        #Si ya encontró la ruta se realiza ahora el control de posición punto a punto
        if terminoRuta:
            print("Control de posición");

        # Si ya se seleccionó el punto inicial y final se busca la ruta
        if START and END and not terminoRuta:
            ruta = Astar(graph, START, END, gridmap, gridmapN, probFree);
            terminoRuta = True;


    cv2.destroyAllWindows();

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
            print("Path: ", len(nodoActual[3]));
            print("Nodos: ", count);
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

    print("Nodos: ", count);
    print("NO HAY RUTA");
    return "NO HAY RUTA";

if __name__ == "__main__":
    args = sys.argv;
    try:
        app = app(args[1]);
    except Exception as e:
        print("ERROR -- Debe introducir un nombre de archivo válido. Incluya la extensión (.mp4).");
        raise

