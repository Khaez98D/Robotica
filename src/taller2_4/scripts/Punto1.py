import numpy as np
import os
import matplotlib.pyplot as plt

#Posiciones
posRobot=np.array([1,0.5,np.pi/4])  #Respecto al marco inercial
posLaser=np.array([0.2,0,0])        #Respecto al marco del robot

#Carga los dato
pathArchivo = os.path.join(os.path.dirname(os.path.dirname(__file__)),'docs/laserscan.dat')
pathDirectorio = os.path.join(os.path.dirname(os.path.dirname(__file__)),'results')
laserdata = np.loadtxt(pathArchivo)
angle_min,angle_max=-np.pi/2,np.pi/2
theta = np.linspace(angle_min, angle_max, len(laserdata))

def R(o):
    return np.array([
        [np.cos(o),np.sin(o),0],
        [-np.sin(o),np.cos(o),0],
        [0,0,1],
    ])

def Rinv(o):
    return np.array([
        [np.cos(o),-np.sin(o),0],
        [np.sin(o),np.cos(o),0],
        [0,0,1],
    ])

if __name__ == '__main__':
    
    R=Rinv(posRobot[2])  #Matriz del marco del robot al marco global
    posLaserGlobal = posRobot+np.matmul(R,posLaser)
    RL= np.zeros(shape=(len(laserdata),3))   #Distancias medidas por el laser
    for i in range(len(laserdata)):
        x=np.array([np.cos(theta[i])*laserdata[i],np.sin(theta[i])*laserdata[i],theta[i]])
        RL[i]=(posLaserGlobal + np.matmul(R,x))
    
    #Grafica literal A 
    plt.figure(1)
    plt.scatter(theta,laserdata)
    plt.xlabel(r'Angulo (rad)')
    plt.ylabel(r'Distancia al laser (cm)')
    plt.title(r'Mediciones del laser vs Angulo')
    plt.grid()
    plt.savefig(os.path.join(pathDirectorio,'grafica1A.png'))



    #Graficac literal B
    plt.figure(2)
    plt.xlabel(r'Distancia X (m)')
    plt.ylabel(r'Distancia Y (m)')
    plt.title(r'Grafica Robot y Laser')
    plt.scatter(posRobot[0], posRobot[1],color='blue',marker='x')
    plt.scatter(posLaserGlobal[0],posLaserGlobal[1],color='red', marker='x')
    plt.scatter(RL[:,0],RL[:,1],color='black')
    
    plt.savefig(os.path.join(pathDirectorio,'grafica1C.png'))