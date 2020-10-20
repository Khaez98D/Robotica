#!/usr/bin/python3
# -*- coding: utf-8 -*-

import cv2;
import time;
import sys;
import os;
import math;
import numpy as np;


class futVideo:

    def __init__(self, videoFile):
        #Obtener primer frame del video
        sep = os.path.sep;
        path = os.path.abspath(__file__).replace("scripts"+sep+__file__, "docs"+sep+args[1]);
        vid = cv2.VideoCapture(path);
        _, fFrame = vid.read();
        vid.release();

        #Obtener la Matriz de transformación de perspectiva (M) de manera manual seleccionando
        # las esquinas de la cancha
        M = self.selecEsquinas(fFrame);

        #Procesar video para guardar con las adiciones de los números de cada jugador
        self.procesVideo(path, M);

    def selecEsquinas(self, frame):
        #Reescalar imagen para dimensión de 900x600
        # dimScale = [frame.shape[0]/900, frame.shape[1]/600];
        reFrame = cv2.resize(frame, (900,600), interpolation = cv2.INTER_AREA);

        imgWinName = "Selección de esquinas";

        esquinas = [];
        nuevasEsquinas = np.array([[0,0], [900,0], [0,600], [900,600]], np.float32);

        print("Aparecerá una imagen en la pantalla, por favor seleccione las 4 esquinas de la cancha");
        print("Realice la selección en el siguiente orden:");
        print(".1    .2\n.3    .4\n \nDespués de seleccionar las 4 esquinas presione ESC");
        time.sleep(3);

        def mouseHandler(event, x, y, flags, params):
            if event == cv2.EVENT_LBUTTONUP:
                cv2.circle(reFrame, (x,y), 10, (52, 232, 235), 2);
                cv2.circle(reFrame, (x,y), 2, (52, 232, 235), -1);
                esquinas.append([x,y]);

        cv2.namedWindow(imgWinName);
        cv2.setMouseCallback(imgWinName, mouseHandler);

        while True:
            cv2.imshow(imgWinName, reFrame);
            if cv2.waitKey(20) == 27:
                cv2.destroyAllWindows();
                break;

        M = cv2.getPerspectiveTransform(np.array(esquinas, np.float32), nuevasEsquinas);
        return M;
        # dst = cv2.warpPerspective(reFrame, M, (900,600));


    # Algoritmo para colocar los números de cada jugador sobre el video y guardar el resultado
    def procesVideo(self, videoFile, M):
        #Abrir video
        vid = cv2.VideoCapture(videoFile);

        #Definir codificación para guardar video y ruta de salida
        sep = os.path.sep;
        pathS = videoFile.replace("docs"+sep, "results"+sep).replace(".mp4", "-res.mp4");
        out = cv2.VideoWriter(pathS, 0x7634706d, 30.0, (900,600));

        #Colores HSV de los equipos y de los núemros para las máscaras
        hsvAzul = np.array([ [110,180,180], [125,255,255] ], np.float32);
        hsvAmar = np.array([ [31,96,40], [40,255,255] ], np.float32);
        hsvVerd = np.array([ [48,177,177], [78,255,255] ], np.float32);
        hsvMage = np.array([ [141,200,148], [179,255,255] ], np.float32);

        #Procesar frame por frame
        while vid.isOpened():
            ret, frame = vid.read();

            if ret:
                #Redimensionar frame
                reFrame = cv2.resize(frame, (900,600), interpolation = cv2.INTER_AREA);
                frame = cv2.warpPerspective(reFrame, M, (900,600));

                #Máscara para Equipo Azul
                hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV);
                maskAz = cv2.inRange(hsv, hsvAzul[0], hsvAzul[1]);
                maskAz = cv2.erode(maskAz, None, iterations = 1);
                maskAz = cv2.dilate(maskAz, None, iterations = 2);

                #Máscara para Equipo Amarillo
                hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV);
                maskAm = cv2.inRange(hsv, hsvAmar[0], hsvAmar[1]);
                maskAm = cv2.erode(maskAm, None, iterations = 1);
                maskAm = cv2.dilate(maskAm, None, iterations = 2);

                #Máscara para Números Verdes
                hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV);
                maskVe = cv2.inRange(hsv, hsvVerd[0], hsvVerd[1]);
                maskVe = cv2.erode(maskVe, None, iterations = 1);
                maskVe = cv2.dilate(maskVe, None, iterations = 2);

                #Máscara para Números Magenta
                hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV);
                maskMa = cv2.inRange(hsv, hsvMage[0], hsvMage[1]);
                maskMa = cv2.erode(maskMa, None, iterations = 1);
                maskMa = cv2.dilate(maskMa, None, iterations = 2);

                #Hallar contornos de colores
                contAz, _ = cv2.findContours(maskAz, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE);
                contAm, _ = cv2.findContours(maskAm, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE);
                contVe, _ = cv2.findContours(maskVe, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE);
                contMa, _ = cv2.findContours(maskMa, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE);

                #Proceso para equipo Azul
                for cAz in contAz:
                    #Hallar centros de cada jugador del equipo
                    ((xAz, yAz), _) = cv2.minEnclosingCircle(cAz);
                    xAz = int(xAz);
                    yAz = int(yAz);

                    #Buscar circulos Verdes y Magentas de este jugador
                    cenVe = [];
                    cenMa = [];
                    for cVe in contVe:
                        ((xVe, yVe), _) = cv2.minEnclosingCircle(cVe);
                        if abs(xVe - xAz) < 15 and abs(yVe - yAz) < 15:
                            cenVe.append((int(xVe), int(yVe)));
                    for cMa in contMa:
                        ((xMa, yMa), _) = cv2.minEnclosingCircle(cMa);
                        if abs(xMa - xAz) < 15 and abs(yMa - yAz) < 15:
                            cenMa.append((int(xMa), int(yMa)));


                    #Determinar núemros de cada jugador
                    font = cv2.FONT_HERSHEY_SIMPLEX;
                    if len(cenVe) == 3:
                        cv2.putText(frame,'2',(xAz+5,yAz-5), font, 1,(255,0,0),2);
                    elif len(cenMa) == 3:
                        cv2.putText(frame,'0',(xAz+5,yAz-5), font, 1,(255,0,0),2);
                    else:
                        if len(cenVe) == 2 and len(cenMa) == 2:
                            #Distancia entre los 2 circulos verdes
                            distVe = math.sqrt((cenVe[0][0] - cenVe[1][0])**2 + (cenVe[0][1] - cenVe[1][1])**2);

                            #Distancia máxima entre un verde y un magenta
                            disMax1 = math.sqrt((cenVe[0][0] - cenMa[0][0])**2 + (cenVe[0][1] - cenMa[0][1])**2);
                            disMax2 = math.sqrt((cenVe[0][0] - cenMa[1][0])**2 + (cenVe[0][1] - cenMa[1][1])**2);
                            disMax = max(disMax1, disMax2);

                            #Si la distancia entre verdes es menor que entre el verde y el magenta será código 1
                            if distVe <= disMax:
                                cv2.putText(frame,'1',(xAz+5,yAz-5), font, 1,(255,0,0),2);
                            else:
                                cv2.putText(frame,'3',(xAz+5,yAz-5), font, 1,(255,0,0),2);

                #Proceso para equipo Amarillo
                for cAm in contAm:
                    #Hallar centros de cada jugador del equipo
                    ((xAm, yAm), _) = cv2.minEnclosingCircle(cAm);
                    xAm = int(xAm);
                    yAm = int(yAm);

                    #Buscar circulos Verdes y Magentas de este jugador
                    cenVe = [];
                    cenMa = [];
                    for cVe in contVe:
                        ((xVe, yVe), _) = cv2.minEnclosingCircle(cVe);
                        if abs(xVe - xAm) < 15 and abs(yVe - yAm) < 15:
                            cenVe.append((int(xVe), int(yVe)));

                    for cMa in contMa:
                        ((xMa, yMa), _) = cv2.minEnclosingCircle(cMa);
                        if abs(xMa - xAm) < 15 and abs(yMa - yAm) < 15:
                            cenMa.append((int(xMa), int(yMa)));

                    #Determinar núemros de cada jugador
                    font = cv2.FONT_HERSHEY_SIMPLEX;
                    if len(cenVe) == 3:
                        cv2.putText(frame,'2',(xAm+5,yAm-5), font, 1,(0,255,255),2);
                    elif len(cenMa) == 3:
                        cv2.putText(frame,'0',(xAm+5,yAm-5), font, 1,(0,255,255),2);
                    else:
                        if len(cenVe) == 2 and len(cenMa) == 2:
                            #Distancia entre los 2 circulos verdes
                            distVe = math.sqrt((cenVe[0][0] - cenVe[1][0])**2 + (cenVe[0][1] - cenVe[1][1])**2);

                            #Distancia máxima entre un verde y un magenta
                            disMax1 = math.sqrt((cenVe[0][0] - cenMa[0][0])**2 + (cenVe[0][1] - cenMa[0][1])**2);
                            disMax2 = math.sqrt((cenVe[0][0] - cenMa[1][0])**2 + (cenVe[0][1] - cenMa[1][1])**2);
                            disMax = max(disMax1, disMax2);

                            #Si la distancia entre verdes es menor que entre el verde y el magenta será código 1
                            if distVe <= disMax:
                                cv2.putText(frame,'1',(xAm+5,yAm-5), font, 1,(0,255,255),2);
                            else:
                                cv2.putText(frame,'3',(xAm+5,yAm-5), font, 1,(0,255,255),2);


                #Guardar frame en el video de salida
                out.write(frame);


                #Mostrar video con las adiciones
                cv2.imshow("Video " + videoFile, frame);

                if cv2.waitKey(20) == 27:
                    cv2.destroyAllWindows();
                    break;
            else:
                break;


        #Cerrar video y salida
        vid.release();
        out.release();
        cv2.destroyAllWindows();



if __name__ == "__main__":
    args = sys.argv;
    try:
        app = futVideo(args[1]);
    except Exception as e:
        print("ERROR -- Debe introducir un nombre de archivo válido. Incluya la extensión (.mp4).");
        raise
