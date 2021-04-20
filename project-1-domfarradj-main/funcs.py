from math import *


def poundsToKG(pounds):
   return pounds*0.453592


def getMassObject(letter):
	if letter =='t':
		return(0.1)
	elif letter=='p':
		return(1.0)
	elif letter=='r':
		return(3.0)
	elif letter=='g':
		return(5.3)
	elif letter=='l':
		return(9.07)
	else:
		return(0.0)


def getVelocityObject(distance):
   return sqrt((9.8*distance)/2)


def getVelocitySkater(massSkater, massObject, velObject):
   return massObject*velObject/massSkater 

