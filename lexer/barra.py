from time import sleep

for i in range(101):
	
	print('['+'*'*i+' '*(100-i) + ']',i,'%', end='\r')
	
	sleep(0.099)
