from time import sleep

for i in range(100):
	
	print('['+'*'*i+' '*(100-i) + ']',i,'%', end='\r')
	
	sleep(0.099)