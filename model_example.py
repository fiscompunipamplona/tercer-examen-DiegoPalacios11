from numpy import array, linspace
from math import sin, cos, pi
from pylab import plot, xlabel, ylabel, show
from scipy.integrate import odeint # para solucionar ecuaciones diferenciales

from vpython import sphere, scene, vector, color, arrow, text, sleep #sleep--particula que se propaga en un campo magnetico

arrow_size = 0.1 #tamaño del arreglo

arrow_x = arrow(pos=vector(0,0,0), axis=vector(arrow_size,0,0), color=color.red)
arrow_y = arrow(pos=vector(0,0,0), axis=vector(0,arrow_size,0), color=color.green)
arrow_z = arrow(pos=vector(0,0,0), axis=vector(0,0,arrow_size))

R = 0.01#tamaño de la particula esferica
b=1.0 #Magnitud campo magnetico

def func (conds, dx, dy, dz, b): #se define la funcion con: condiciones iniciales, variable temporal, y parametros (g,l). funicon que devuelve los valores de theta y omega
    dx = conds[10.0]
    dvx = (q/R)*b*(conds[1])
    dy = conds[1] 
    dvy = (q/R)*b*(conds[1])
    dz = 2.0 
    return array([dx, dvx, dy, dvy, dz, dvz], float) #retorna a los arreglos anteriores

g = 9.81
l = 0.1

thes = 45*pi/180. #conversion a Rad
omes = 0.

initcond = array([thes,omes], float) 	#arreglo de condiciones iniciales

n_steps = 1000 	#numero de pasos
t_start = 0.	#tiempo inicial
t_final = 15.	#tiempo final
t_delta = (t_final - t_start) / n_steps	# paso temporal (grosor)
t = linspace(t_start, t_final, n_steps)	#Arreglo diferencial con las condiciones del grosor temporal

solu, outodeint = odeint( func, initcond, t, args = (g, l), full_output=True)	#solucion de la Ecu difer

theta, omega = solu.T	#matriz de 2*2 ( columnas para los pasos) solucion para cada paso de theta y omega , se definen las variables y solu.t devuelve la matriz transpuesta en los valores de theta y omega


# =====================

scene.range = 0.2 #  tamaño de la pantalla a visualizar

xp = l*sin(thes)	#coordenadas cartesianas de la esfera con el angulo inicial
yp = -l*cos(thes)	#igual
zp = 0.			#igual

sleeptime = 0.0001	#tiempo con que la maquina actualiza la posicion de la particula

prtcl = sphere(pos=vector(xp,yp,zp), radius=R, color=color.cyan)	#Define la particula con coordenadas iniciales dadas xp,yp,zp

time_i = 0	#defino contador que se mueve en el espacio que se soluciona la Ecuf difencial
t_run = 0	#con el que se corre la animacion

#for i in omega:
#    print(i)


while t_run < t_final:		#condicion para la animacion
    sleep(sleeptime)		#duerme
    prtcl.pos = vector( l*sin(theta[time_i]), -l*cos(theta[time_i]), zp )	#actualiza posicion de la particula aumenta el contador
    
    t_run += t_delta	#contadores y acumuladores
    time_i += 1		#igual

