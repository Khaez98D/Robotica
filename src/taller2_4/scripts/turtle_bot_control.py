#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import sys;
import rospy;
import math;
import _thread;
from geometry_msgs.msg import Twist;
from std_msgs.msg import Float32;
import matplotlib.pyplot as plt;
import matplotlib.animation as animation;


#Clase encargada de controlar la posición del robot y llevarlo a la posición final indicada por parámetro
class Control:

	#Método constructor del controlador
	def __init__(self, pPosF):

		#Argumentos de la clase
		self.posF = pPosF;			#Posición deseada final del robot [x, y, theta]
		self.xPos = [0.0];			#Posición actual X del robot en el marco inercial
		self.yPos = [0.0];			#Posición actual Y del robot en el marco inercial
		self.orie = [0.0];			#Orientación actual del robot en el marco inercial
		self.xPosE = [0.0];			#Posición estimada X del robot en el marco inercial
		self.yPosE = [0.0];			#Posición estimada Y del robot en el marco inercial
		self.orieE = [-0.7854];		#Orientación estimada del robot en el marco inercial
		self.errX = [-pPosF[0]];	#Error de posición X del robot
		self.errY = [-pPosF[1]];	#Error de posición Y del robot
		self.errTh = [-pPosF[2]];	#Error de orientación del robot
		self.simTime = [0.0];		#Tiempo de simulación leído de V-REP
		self.actTime = 0.0;			#Tiempo actual de simulación
		self.acabo = False;			#Determina si ha llegado a la posición deseada

		#Iniciar el nodo de ROS
		rospy.init_node('turtle_bot_control');
		
		#Iniciar el publicador para controlar el robot
		self.pub = rospy.Publisher('turtlebot_cmdVel', Twist, queue_size=5);
		self.rate = rospy.Rate(2);

		#Iniciar el subscriptor para recibir la posición y orientación actual, así como el tiempo
		rospy.Subscriber('turtlebot_position', Twist, self.getPos);
		rospy.Subscriber('turtlebot_orientation', Float32, self.getOri);
		rospy.Subscriber('simulationTime', Float32, self.getTime);

		#Crear figura para graficar la posición en tiempo real
		self.posPlot = plt.figure();
		self.ax1 = self.posPlot.add_subplot(1,1,1);
		livePlot = animation.FuncAnimation(self.posPlot, self.actPlot, interval=200);

		#Actualizar tiempo para compensar por el tiempo de inicio del nodo
		self.simTime.append(self.actTime);

		#Iniciar thread encargado del control del robot
		_thread.start_new_thread(self.controlarRobot, ());

		#Dejar nodo a la escucha de sus subcripciones pero evita ocupar tiempo de procesameinto
		rospy.sleep(0.2);
		plt.show();

		if self.acabo:
			#Graficar error de posición
			errPlot = plt.figure(figsize=(8,6));
			ax2 = errPlot.add_subplot(3,1,1);
			ax3 = errPlot.add_subplot(3,1,2);
			ax4 = errPlot.add_subplot(3,1,3);

			self.simTime.pop();

			ax2.plot(self.simTime, self.errX);
			ax3.plot(self.simTime, self.errY);
			ax4.plot(self.simTime, self.errTh);

			#Formato de gráficas
			ax2.set_title('Error de posición en X durante la trayectoria');
			ax2.set_xlabel('Tiempo [s]');
			ax2.set_ylabel('Error X [m]');

			ax3.set_title('Error de posición en Y durante la trayectoria');
			ax3.set_xlabel('Tiempo [s]');
			ax3.set_ylabel('Error Y [m]');

			ax4.set_title('Error de orientación durante la trayectoria');
			ax4.set_xlabel('Tiempo [s]');
			ax4.set_ylabel('Error [rad]');

			plt.subplots_adjust(top = 0, bottom=0, hspace=1.5, wspace=1.5);
			errPlot.savefig("error_punto4.png");
			plt.show();

		


	#Método encargado de actualizar la posición actual del robot
	def getPos(self, msg):
		if msg.linear.x != self.xPos[-1] or msg.linear.y != self.yPos[-1]:
			self.xPos.append(msg.linear.x);
			self.yPos.append(msg.linear.y);

	#Método encargado de actualizar la orientación actual del robot
	def getOri(self, msg):
		if msg.data != self.orie[-1]:
			self.orie.append(msg.data);

	#Método encargado de actualizar el tiempo de simulación
	def getTime(self, msg):
		self.actTime = msg.data;

	#Método encargado de actualizar la gráfica de posición del robot
	def actPlot(self, i):
		#Posiciones reales y estimadas actuales
		actX = self.xPos[-1];
		actY = self.yPos[-1];
		actXE = self.xPosE[-1];
		actYE = self.yPosE[-1];

		#Vaciar gráfica
		self.ax1.clear();
		self.ax1.grid();

		#Graficar posición Real
		self.ax1.plot(self.xPos, self.yPos, label='Real', color='r');
		self.ax1.scatter(actX, actY, color='r');
		self.ax1.quiver(actX, actY, math.cos(self.orie[-1]), math.sin(self.orie[-1]), color='r');#, scale=20);

		#Graficar posición Estimada
		self.ax1.plot(self.xPosE, self.yPosE, '--g', label='Estimada');
		self.ax1.scatter(actXE, actYE, color='g');
		self.ax1.quiver(actXE, actYE, math.cos(self.orieE[-1]), math.sin(self.orieE[-1]), color='g');#, scale=20);

		#Formato de gráfica
		self.ax1.axis((-2.5,2.5,-2.5,2.5));
		self.ax1.set_title('Posición del Robot');
		self.ax1.set_xlabel('X [m]');
		self.ax1.set_ylabel('Y [m]');
		self.ax1.legend();


	#Método encargado de controlar el robot por un Thread comunicándose con el tópico de velocidades
	def controlarRobot(self):
		#Mientras no se cierre la simulación o se haya llegado a la posición final
		while not rospy.is_shutdown() or not self.acabo:
			#Mensaje en el que se enviará el comando de control
			msg = Twist();

			#Constantes para el control de posición
			Kp = 0.47;
			Ka = 0.5;
			Kb = -0.5;

			#Distancias a recorrer en ambos ejes
			dx = self.posF[0] - self.xPos[-1];
			dy = self.posF[1] - self.yPos[-1];

			#Calcular el error
			self.errX.append(abs(dx));
			self.errY.append(abs(dy));
			self.errTh.append(abs(self.orie[-1] - self.posF[2]));

			#Calcular errores de orientación a, b y error de posición p
			a = math.atan2(dy, dx) - self.orie[-1];
			p = math.sqrt(dx**2 + dy**2);
			b = self.posF[2] - self.orie[-1];

	    	#Estimación de la etapa de control
			errThre = 0.15;
			controlState = 3;
			if abs(a) >= errThre and abs(p) >= errThre:
				controlState = 0;
			if abs(p) >= errThre and abs(a) <= errThre:
				controlState = 1;
			if abs(b) >= errThre and abs(p) <= errThre:
				controlState = 2;

			if abs(p) <= errThre and abs(b) <= errThre:
				self.acabo = True;


			#El control de posición se realiza en 3 etapas, actualizando la velocidad lineal o angular
			linVel = 0.0;
			angVel = 0.0;

			#Etapa 1 - Control de orientación para el avance en línea recta
			#VelocidadAngular de a = Kp*Sin(a) - Ka*a - Kb*b
			if controlState == 0:
				msg.linear.x = linVel;
				angVel = -Kp*math.sin(a) + Ka*a# + Kb*b;
				if abs(angVel) < 0.4:
					angVel = angVel/abs(angVel) * 0.4;
				msg.angular.z = angVel;

		    #Etapa 2 - Control de distancia hasta punto final
		    #Velocidad lineal p = -Kp*p*Cos(a)
			if controlState == 1:
				linVel = Kp*p*math.cos(a);
				if abs(linVel) < 0.3:
					linVel = linVel/abs(linVel) * 0.3;
				msg.linear.x = linVel;
				msg.angular.z = angVel;

			#Etapa 3 - Control de orientación final
		    #Velocidad lineal de b = -Kp*Sin(a)
			if controlState == 2:
				msg.linear.x = linVel;
				angVel = Kp*math.sin(b) - Kb*b;
				if abs(angVel) < 0.4:
					angVel = angVel/abs(angVel) * 0.4;
				msg.angular.z = angVel;

			#Si ha finalizado envía un comando para deternerse
			if self.acabo:
				msg.linear.x = linVel;
				msg.angular.z = angVel;

			#Calcular posición estimada del robot
			self.simTime.append(self.actTime);
			self.estimarPos(linVel, angVel, self.xPosE[-1], self.yPosE[-1], self.orieE[-1]);

		    #Enviar comando de control y comprobar si ya ha acabado
			self.pub.publish(msg);
			if self.acabo:
				break;
			self.rate.sleep();

		#Guardar gráfica de trayectoria
		self.posPlot.savefig('./trayectoria_punto4.png');
		plt.close();


	#Método encargado de calcular la posición estimada del robot para el perfil de velocidades dado
	def estimarPos(self, linVel, angVel, x, y, th):
		#dt de estimación
		dt = self.simTime[-1] - self.simTime[-2];	# [s]

		#Actualización de psoición estimada por Integración Numérica
		self.xPosE.append(x + linVel * math.cos(th) * dt);
		self.yPosE.append(y + linVel * math.sin(th) * dt);
		self.orieE.append(th + angVel * dt);
		#self.xPosE.append(math.cos(angVel*dt)*(R*math.sin(th)) + math.sin(angVel*dt)*(R*math.cos(th)) + x-R*math.sin(th));
		#self.yPosE.append(math.sin(angVel*dt)*(R*math.sin(th)) - math.cos(angVel*dt)*(R*math.cos(th)) + y+R*math.cos(th));
		#self.orieE.append(th + angVel*dt);



posF = [float(i) for i in sys.argv if i != __file__];
if posF == []:
	posF = [-2,-2, -3*math.pi/4];

#Ejecución de este Script
if __name__ == '__main__':
    try:
        app = Control(posF);
    except Exception as e:
        raise;