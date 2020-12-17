#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cv2;
import rospy;
import numpy as np;
from std_msgs.msg import String;
from sensor_msgs.msg import Image;
from cv_bridge import CvBridge, CvBridgeError;

monedas = 0;

class Conteo:

	def __init__(self):

		#Obtiene la imagen para realizar el conteo de modenas, se suscribe al tópico de 
		# la cámara para obtener la imagen
		self.bridge = CvBridge();
		pub = rospy.Publisher('/senecabot_coins', String, queue_size=10);
		self.image_sub = rospy.Subscriber("/camera_image", Image, self.getImage);
		rospy.init_node('Senecabot_Conteo');
		rate = rospy.Rate(5);

		#Espera a que se cuenten las mondeas para publicar
		global monedas;
		while monedas == 0:
			pass;
		pub.publish(str(monedas));


	def getImage(self, data):
		global monedas;

		imgWinName = "Conteo de monedas";

		try:
			frame = self.bridge.imgmsg_to_cv2(data, "bgr8");
			self.image_sub.unregister();
		except CvBridgeError as e:
			raise;

		#Redimensionar frame
		frame = cv2.resize(frame, (640,480), interpolation = cv2.INTER_AREA);

		while True:
			cv2.imshow("Imagen Original", frame);
			if cv2.waitKey(20) == 27:
				cv2.destroyAllWindows();
				break;


		#Colores HSV de las esquinas y las monedas
		hsvEsqui = np.array([ [98,85,72], [150,226,188] ], np.float32);
		hsvMoned = np.array([ [10,53,50], [38,235,190] ], np.float32);
		#hsvMoned = np.array([ [0,45,0], [56,193,255] ], np.float32);

		#Máscara para Esquinas
		hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV);
		maskEsq = cv2.inRange(hsv, hsvEsqui[0], hsvEsqui[1]);
		maskEsq = cv2.erode(maskEsq, None, iterations = 1);
		maskEsq = cv2.dilate(maskEsq, None, iterations = 1);

		while True:
			cv2.imshow("Máscara Esquinas", maskEsq);
			if cv2.waitKey(20) == 27:
				cv2.destroyAllWindows();
				break;

		# Puntos de las esquinas encontradas y las deseadas
		esquinas = [];
		nuevasEsquinas = []; #np.array([[0,480], [640,480], [640,0], [0,0]], np.float32);

		#Hallar contornos de las esquinas
		contEsq = cv2.findContours(maskEsq, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0];

		#Hallar centros de las esquinas
		for cEs in contEsq:
			#Hallar centros de cada esquina
			((xEs, yEs), _) = cv2.minEnclosingCircle(cEs);
			#print(int(xEs),int(yEs));
			esquinas.append([int(xEs),int(yEs)]);

			if(xEs < 300 and yEs < 250):
				nuevasEsquinas.append([0,0]);
			elif(xEs < 300 and yEs >= 250):
				nuevasEsquinas.append([0,480]);
			elif(xEs >= 300 and yEs < 250):
				nuevasEsquinas.append([640,0]);
			elif(xEs >= 300 and yEs >= 250):
				nuevasEsquinas.append([640,480]);


		# Matriz de transformación de perspectiva
		esquinas = np.array(esquinas, np.float32);
		nuevasEsquinas = np.array(nuevasEsquinas, np.float32);
		M = cv2.getPerspectiveTransform(esquinas, nuevasEsquinas);

		#Cambiar perspectiva
		frame = cv2.warpPerspective(frame, M, (640,480));

		#Máscara para monedas
		hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV);
		maskMon = cv2.inRange(hsv, hsvMoned[0], hsvMoned[1]);
		maskMon = cv2.erode(maskMon, None, iterations = 5);
		maskMon = cv2.dilate(maskMon, None, iterations = 1);

		while True:
			cv2.imshow("Mascara Monedas", maskMon);
			if cv2.waitKey(20) == 27:
				cv2.destroyAllWindows();
				break;

		#Hallar contornos de las monedas
		contMon = cv2.findContours(maskMon, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0];

		monedasN = 0;

		#Hallar centros
		for cMo in contMon:
			#Hallar centros de cada moneda
			((xMo, yMo), rMo) = cv2.minEnclosingCircle(cMo);
			#print(int(xMo),int(yMo), int(rMo));

			if(rMo <= 36):
				monedasN += 100;
			elif(rMo <= 39 and yMo > 250):
				monedasN += 200;
			elif(rMo <= 42 and yMo < 250):
				monedasN += 500;
			elif(rMo > 42):
				monedasN += 1000;

		monedas = monedasN;


if __name__ == "__main__":
    try:
        app = Conteo();
    except KeyboardInterrupt:
    	cv2.destroyAllWindows();
    except Exception as e:
        print("ERROR -- ");
        raise