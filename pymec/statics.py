# -*- coding: utf-8 -*-
import numpy as np
from numpy import sin,cos,tan,arccos,arctan,arcsin,pi
from core import Vector, Point

def fma2vect(mag,*angles,**kwargs):
	"""
	Convierte una fuerza expresada en mediante su magnitud y
	ángulos directores a la forma vectorial cartesiana.
	"""
	if len(angles)==3:
		angles = [k*pi/180 for k in angles]
		return Vector(mag*cos(angles[0]), mag*cos(angles[1]), mag*cos(angles[2]))
	elif len(angles)==1:
		angle = angles[0]*pi/180
		return Vector(mag*cos(angle), mag*sin(angle))
	elif bool(kwargs) and not(bool(angles)):
		phi = (kwargs.get('phi'))*pi/180
		theta = (kwargs.get('theta'))*pi/180
		return Vector(mag*sin(phi)*cos(theta), mag*sin(phi)*sin(theta), mag*cos(phi))
		
def posvect(a,b):
	"""
	Devuelve el vector de posición del punto a al punto b.
	"""
	return Vector(np.array(b.coords) - np.array(a.coords))


def moment(u,v):
	""" --- """
	return Vector(np.cross(u.comps, v.comps))
	
def sumforces(*forces):
	"""
	Devuelve la fuerza resultante (FR), magnitud (mag) y 
	dirección (direc) de una sumatoria de fuerzas
	"""
	FR = Vector(0,0) if len(forces[0].comps)==2 else Vector(0,0,0)
	for f in forces:
		FR += f
	mag = FR.norm()
	direc = dirang(FR) if len(FR.comps)==3 else arctan(FR.y/FR.x)*180/pi
	return FR, mag, direc

def dircos(v):
	"""
	Calcula los cosenos directores del vector v
	"""
	magv = v.norm()
	return [k/magv for k in v.comps]
	
def dirang(v):
	"""
	Calcula los ángulos directores del vector v
	"""
	dc = dircos(v)
	return [arccos(k)*180/pi for k in dc] # Degrees


def test():
	a = Vector(1,2,4)
	b = Vector(3,5,2)
	print a,b
	print "Suma: ",a+b
	print "Resta: ",a-b
	print "*: ",a*b
	
if __name__=='__main__':
	test()
