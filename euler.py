
def euler_1():
	number = input('Number: ')
	for x in range(1,int(number)+1):
		if((x%3) == 0):
			print(str(x))
		else:
			if((x%5) == 0):
				print(str(x))

def euler_2():
	number = input('Enter Fibonnacci limit: ')
	n = 0
	l = [1,2]
	print(str(l[0]) + "\n" + str(l[1]))
	while(n < int(number)):		
		n = l[0] + l[1]
		if n < int(number):
			print(n)
			l[0] = l[1]
			l[1] = n

euler_2()