from numpy import array, linspace, shape,matrix,transpose
from math import sin, cos, pi, sqrt
from pylab import plot, xlabel, ylabel, show
from scipy.integrate import odeint

from vpython import *  #sphere, scene, vector, color, arrow, text, sleep 
#scene.background = color.grey(.5)


sol = sphere(pos=vec(0,0,0), radius=1, color=color.yellow,text='sol')



##############################################################
# Planet jupiter
Q1= 5.20#UA
e1= 0.048
a1= Q1/(1+e1) #UA
b1= sqrt((1-(e1*e1))*(a1*a1)) #AU
q1= 2*a1 - Q1 #UA
tha=(45*pi)/180.# angulo inicial   
################################################################
# Planet saturno
Q2= 9.54#UA
e2= 0.054
a2= Q2/(1+e2) #UA
b2= sqrt((1-(e2*e2))*(a2*a2)) #AU
q2= 2*a2 - Q2 #UA
################################################################
# Planet urano
Q3= 19.22#UA
e3= 0.047
a3= Q3/(1+e3) #UA
b3= sqrt((1-(e3*e3))*(a3*a3)) #AU
q3= 2*a3 - Q3 #UA
################################################################
# Planet neptuno
Q4= 30.06#UA
e4= 0.008
a4= Q4/(1+e4) #UA
b4= sqrt((1-(e4*e4))*(a4*a4)) #AU
q4= 2*a4 - Q4 #UA




################################################################
# definimos las funciones de los planetas

def orbit1(init1, t1):
    
    dx1 =  init1[0]
    dy1 =  init1[1]
    dth1 = init1[4] 
    GM = 4*pi*pi # UA^3 / yr^2
    r1 = (a1*(1-e1*e1))/(1+e1*cos(tha))
    ac1 = -GM / (r1*r1*r1)

    dv_x1 = ac1*init1[2]
    dv_y1 = ac1*init1[3]
    
    dthe1 = (sqrt(((dv_x1*dv_x1)/((2/r1)-(1/a1))) + (dv_y1*dv_y1)/((2/r1)-(1/b1)))) 
   
    return array([dv_x1, dv_y1, dx1, dy1, dthe1], float) 

 ####################################################################   
def orbit2(init2, t2):
    
    dx2 =  init2[0]
    dy2 =  init2[1]
    dth2 = init2[4] 
    GM = 4*pi*pi # UA^3 / yr^2
    r2 = (a2*(1-e2*e2))/(1+e2*cos(tha))
    ac2 = -GM / (r2*r2*r2)

    dv_x2 = ac2*init2[2]
    dv_y2 = ac2*init2[3]
    
    dthe2 = (sqrt(((dv_x2*dv_x2)/((2/r2)-(1/a2))) + (dv_y2*dv_y2)/((2/r2)-(1/b2)))) 
   
    return array([dv_x2, dv_y2, dx2, dy2, dthe2], float) 


##############################################################
 ####################################################################   
def orbit3(init3, t3):
    
    dx3 =  init3[0]
    dy3 =  init3[1]
    dth3 = init3[4] 
    GM = 4*pi*pi # UA^3 / yr^2
    r3 = (a3*(1-e3*e3))/(1+e3*cos(tha))
    ac3 = -GM / (r3*r3*r3)

    dv_x3 = ac3*init3[2]
    dv_y3 = ac3*init3[3]
    
    dthe3 = (sqrt(((dv_x3*dv_x3)/((2/r3)-(1/a3))) + (dv_y3*dv_y3)/((2/r3)-(1/b3)))) 
   
    return array([dv_x3, dv_y3, dx3, dy3, dthe3], float) 

####################################################################   
def orbit4(init4, t4):
    
    dx4 =  init4[0]
    dy4 =  init4[1]
    dth4 = init4[4] 
    GM = 4*pi*pi # UA^3 / yr^2
    r4 = (a4*(1-e4*e4))/(1+e4*cos(tha))
    ac4 = -GM / (r4*r4*r4)

    dv_x4 = ac4*init4[2]
    dv_y4 = ac4*init4[3]
    
    dthe4 = (sqrt(((dv_x4*dv_x4)/((2/r4)-(1/a4))) + (dv_y4*dv_y4)/((2/r4)-(1/b4)))) 
   
    return array([dv_x4, dv_y4, dx4, dy4, dthe4], float) 


##############################################################

n_steps = 10000
t_start = 0.
t_final = 150.
t_delta = (t_final - t_start) / n_steps # saltos 
t1 = linspace(t_start, t_final, n_steps) # vector tiempo (int,end,lapse)
t2 = linspace(t_start, t_final, n_steps) # vector tiempo (int,end,lapse)
t3 = linspace(t_start, t_final, n_steps) # vector tiempo (int,end,lapse)
t4 = linspace(t_start, t_final, n_steps) # vector tiempo (int,end,lapse)
##########################################################################################################3
init1 = [0., 2.*pi, a1, 0, 0]
sol,outodeint1 = odeint(orbit1, init1, t1, full_output=True)# parametros (funcion,y(0),tiempo)
vxx1, vyy1, xx1, yy1, th1 = sol.T
#############################################################################################################
init2 = [0., 2.*pi, a2, 0, 0]
sol2,outodeint2 = odeint(orbit2, init2, t2, full_output=True)# parametros (funcion,y(0),tiempo)
vxx2, vyy2, xx2, yy2, th2 = sol2.T
#############################################################################################################
init3 = [0., 2.*pi, a3, 0, 0]
sol3,outodeint3 = odeint(orbit3, init3, t3, full_output=True)# parametros (funcion,y(0),tiempo)
vxx3, vyy3, xx3, yy3, th3 = sol3.T
#############################################################################################################
init4 = [0., 2.*pi, a4, 0, 0]
sol4,outodeint4 = odeint(orbit4, init4, t4, full_output=True)# parametros (funcion,y(0),tiempo)
vxx4, vyy4, xx4, yy4, th4 = sol4.T

# =====================
 # parte del sistema 
    
scene.range = 1# m tamaño del sistema 

xp1 = 5.20 # condicion inicil 
xp2 = 9.54
xp3 = 19.22
xp4 = 30.06
yp = 0.  # condiciones iniciales 
zp = 0.


sleeptime = 0.0001 # tiempo entre cada intervalo 

prtcl1 = sphere(pos=vector(xp1,yp,zp), radius=0.5, color=color.red, make_trail=True, )

prtcl2 = sphere(pos=vector(xp2,yp,zp), radius=0.9, color=color.yellow, make_trail=True, )

prtcl3 = sphere(pos=vector(xp3,yp,zp), radius=1, color=color.blue, make_trail=True, )

prtcl4 = sphere(pos=vector(xp4,yp,zp), radius=2, color=color.green, make_trail=True )


###################################################################################################################
angles=array((7.005,3.394,0,1.850,1.303,2.489,0.773,1.7770))*pi/180 

time_i = 0 #          
t_run = 0   #   

angles=array((7.005,3.394,0,1.850,1.303,2.489,0.773,1.7770))*pi/180 

Mrotju=matrix([[1,0,0],[0,cos(angles[4]),-sin(angles[4])],[0,sin(angles[4]),cos(angles[4])]])
Mrotsa=matrix([[1,0,0],[0,cos(angles[5]),-sin(angles[5])],[0,sin(angles[5]),cos(angles[5])]])
Mrotur=matrix([[1,0,0],[0,cos(angles[6]),-sin(angles[6])],[0,sin(angles[6]),cos(angles[6])]])
Mrotne=matrix([[1,0,0],[0,cos(angles[7]),-sin(angles[7])],[0,sin(angles[7]),cos(angles[7])]])

###################################################################################################################


while t_run < t_final:  # 
    sleep(sleeptime)
    ju = Mrotju*transpose(matrix([xx1[time_i],yy1[time_i], zp]))
    sa = Mrotsa*transpose(matrix([xx2[time_i],yy2[time_i], zp]))
    ur = Mrotur*transpose(matrix([xx3[time_i],yy3[time_i], zp]))
    ne =Mrotne*transpose(matrix([xx4[time_i],yy4[time_i], zp]))
    
    prtcl1.pos = vector(ju[0],ju[1],ju[2])
    prtcl2.pos = vector(sa[0],sa[1],sa[2])
    prtcl3.pos = vector(ur[0],ur[1],ur[2])
    prtcl4.pos = vector(ne[0],ne[1],ne[2])
    
    t_run += t_delta  # aumenta para evaluar en el tiempo 
    time_i += 1


