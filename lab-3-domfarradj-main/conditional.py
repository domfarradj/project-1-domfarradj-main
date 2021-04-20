def max_101(x,y):
	if x>y:
		return(int(x))
	if y>x:
		return(int(y)) 
		


def max_of_three(x,y,z):
	if x>y and x>z:
		return(int(x))
	elif y>x and y>z:
		return(int(y))
	else:
		return(int(z))


def rental_late_fee(x):
	if x<=0:
		return(0)
	elif x<=9 :
		return(5)
	elif x<= 15:
		return(7)
	elif x<=24:
		return(19)
	else:
		return(100)
		


