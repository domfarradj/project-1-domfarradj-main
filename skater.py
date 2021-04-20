#Project 1
#
#Name: Dominic Farradj
#Instructor: Workman
#Section: 03
from funcs import *

def main():
	pounds=int(input('How much do you weigh (pounds)? '))
	distance=float(input('How far away is your professor (meters)? '))
	obj=str(input('Will you throw a rotten (t)omato, banana cream (p)ie, (r)ock, (l)ightsaber, or lawn (g)nome? '))
	weight=poundsToKG(pounds)
	mass=getMassObject(obj)
	print("\nNice throw! ", end = '')
	
	if mass <= 0.1:
  		print("You're going to get an F!")
	
	if mass > 0.1 and mass <= 1.0:
  		print("Make sure your professor is OK.")
	
	if mass > 1.0:
		if distance<20:
   			print("How far away is the hospital?")
		else: 
			print("RIP professor.")
	
	velObject=getVelocityObject(distance)
	veloSkater = getVelocitySkater(weight,mass,velObject)
	veloSkater=round(veloSkater, 3)
	print('Velocity of skater:', veloSkater, 'm/s')
	
	if  veloSkater < 0.2:
  		print("My grandmother skates faster than you!")
	
	if veloSkater >= 0.2 and veloSkater < 1.0:
  		return veloSkater
	
	if veloSkater>= 1.0:
  		print("Look out for that railing!!!")


  
  		
if __name__ == '__main__':
   main()
