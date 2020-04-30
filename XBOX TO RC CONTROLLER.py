############### CONFIGURACION

SENSIBILIDAD = 100

########### stick izquierdo

var_izquierda_stick_X = filters.deadband(xbox360[0].leftStickX, 0.1)

Resultado1a= var_izquierda_stick_X * 100
Resultado1b= Resultado1a/1
Resultado1c = vJoy[0].axisMax * Resultado1b
Resultado_final1 = Resultado1c / 100 
vJoy[0].x= Resultado_final1


var_izquierda_stick_Y = filters.deadband(xbox360[0].leftStickY, 0.1)


Resultado1a1= var_izquierda_stick_Y * 100
Resultado1b1= Resultado1a1/1
Resultado1c1 = 1  * Resultado1b1
Resultado_final11 = Resultado1c1 / 100 





if(var_izquierda_stick_Y>0 and vJoy[0].y <= vJoy[0].axisMax):
		vJoy[0].y += Resultado_final11 * SENSIBILIDAD

		
elif(var_izquierda_stick_Y<0 and vJoy[0].y >= -vJoy[0].axisMax):
	vJoy[0].y += Resultado_final11 * SENSIBILIDAD






############ stick derecho

var_derecho_stick_Y = filters.deadband(xbox360[0].rightStickY, 0.1)




Resultado2a= var_derecho_stick_Y * 100
Resultado2b= Resultado2a/1
Resultado2c = vJoy[0].axisMax * Resultado2b
Resultado_final2 = Resultado2c / 100 
vJoy[0].ry= Resultado_final2


var_derecho_stick_X = filters.deadband(xbox360[0].rightStickX, 0.1)

Resultado3a= var_derecho_stick_X * 100
Resultado3b= Resultado3a/1
Resultado3c = vJoy[0].axisMax * Resultado3b
Resultado_final3 = Resultado3c / 100 
vJoy[0].rx= Resultado_final3


####### boton centrar sticks
if(xbox360[0].back):
	vJoy[0].y=0
	
	
	
	
######## resto de botones

if (xbox360[0].a):
	diagnostics.debug("A")
	vJoy[0].setButton(0,int(xbox360[0].a))
else:
	vJoy[0].setButton(0, 0)





if (xbox360[0].b):
	diagnostics.debug("B")
	vJoy[0].setButton(1,int(xbox360[0].b))
else:
	vJoy[0].setButton(1, 0)
	




if (xbox360[0].x):
	diagnostics.debug("X")
	vJoy[0].setButton(2,int(xbox360[0].x))
else:
	vJoy[0].setButton(2, 0)
		




if (xbox360[0].y):
	diagnostics.debug("Y")
	vJoy[0].setButton(3,int(xbox360[0].y))
else:
	vJoy[0].setButton(3, 0)





if (xbox360[0].leftShoulder):
	diagnostics.debug("L SHOULDER")
	vJoy[0].setButton(4,int(xbox360[0].leftShoulder))
else:
	vJoy[0].setButton(4, 0)





if (xbox360[0].leftTrigger):
	diagnostics.debug("L TRIGGER")
	vJoy[0].setButton(5,int(xbox360[0].leftTrigger))
else:
	vJoy[0].setButton(5, 0)





if (xbox360[0].rightShoulder):
	diagnostics.debug("R SHOULDER")
	vJoy[0].setButton(6,int(xbox360[0].rightShoulder))
else:
	vJoy[0].setButton(6, 0)




if (xbox360[0].rightTrigger):
	diagnostics.debug("R TRIGGER")
	vJoy[0].setButton(7,int(xbox360[0].rightTrigger))
else:
	vJoy[0].setButton(7, 0)