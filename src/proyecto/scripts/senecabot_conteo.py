#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cv2;
import rospy;
import numpy as np;
from sensor_msgs.msg import Image;
from cv_bridge import CvBridge, CvBridgeError;


class Conteo:

	def __init__(self):

		#Obtiene la imagen para realizar el conteo de modenas, se suscribe al tópico de 
		# la cámara para obtener la imagen
		self.bridge = CvBridge();
		self.image_sub = rospy.Subscriber("/camera_image", Image, self.getImage);

		#Obtiene la referencia de las esquinas del espacio de captura para realizar la
		# transformación de la imagen, esto para mantener un tamaño de monedas similar
		#M = self.selecEsquinas(self.frame);

	def getImage(self, data):

		imgWinName = "Conteo de monedas";

		try:
			print("Recuperando imagen");
			frame = self.bridge.imgmsg_to_cv2(data, "bgr8");
			self.image_sub.unregister();
		except CvBridgeError as e:
			raise;

		#Redimensionar frame
		frame = cv2.resize(frame, (640,480), interpolation = cv2.INTER_AREA);

		# Puntos de las esquinas encontradas y las deseadas
		esquinas = [];
		nuevasEsquinas = np.array([[0,0], [640,0], [0,480], [640,480]], np.float32);


		#Colores HSV de las esquinas
		hsvNegro = np.array([ [102,145,58], [136,240,194] ], np.float32);
		hsvMoned = np.array([ [0,0,55], [40,207,220] ], np.float32);


		#Máscara para monedas
		hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV);
		maskMon = cv2.inRange(hsv, hsvMoned[0], hsvMoned[1]);
		maskMon = cv2.erode(maskMon, None, iterations = 2);
		maskMon = cv2.dilate(maskMon, None, iterations = 3);

		#Hallar contornos de las monedas
		contEsq = cv2.findContours(maskMon, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0];

		#Hallar centros
		for cNe in contEsq:
			#Hallar centros de cada moneda
			((xNe, yNe), _) = cv2.minEnclosingCircle(cNe);
			print(int(xNe),int(yNe));
			esquinas.append([int(xNe),int(yNe)]);

		# Matriz de transformación de perspectiva
		#M = cv2.getPerspectiveTransform(np.array(esquinas, np.float32), nuevasEsquinas);

		#Cambiar perspectiva
		frame = cv2.warpPerspective(frame, M, (640,480));

		while True:
			cv2.imshow(imgWinName, frame);
			if cv2.waitKey(20) == 27:
				cv2.destroyAllWindows();
				break;

	def selecEsquinas(self, frame):
		imgWinName = "Esquinas";
		cv2.namedWindow(imgWinName);

		while True:
			cv2.imshow(imgWinName, frame);
			if cv2.waitKey(20) == 27:
				cv2.destroyAllWindows();
				break;


if __name__ == "__main__":
    try:
        app = Conteo();
        rospy.init_node('Senecabot_Conteo');
        rospy.spin();
    except KeyboardInterrupt:
    	cv2.destroyAllWindows();
    except Exception as e:
        print("ERROR -- ");
        raise