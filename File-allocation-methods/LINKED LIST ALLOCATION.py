'''LINKED LIST ALLOCATION'''
def loop():
	global list
	global ind
	global size,l
	val = int(input("Enter next index :"))
	if(list[val]==0):
		list[val]=1
		ind[l]=val
		l+=1
	else:
		print("already allocated....aborting....")
		print(list)
		for i in range(0,l):
			if(ind[i]==-1):
				print()
			else:
				print(ind[i],'-->',end='')
def main():
	global list
	global ind
	global size
	global l
	success=0
	flag="Y"
	leng=int(input("Enter the number of blocks"))
	st = int(input("Enter starting index:"))
	if(list[st]==0):
		list[st]=1
		ind[l]=st
		l+=1
		for i in range(0,leng-1):
			loop()
		success =1
		if(success==1):
			print("successfully allocated")	
			print(list)
			for i in range(0,l):
				if(ind[i]==-1):
					print()
				else:
					print(ind[i],'-->',end='')
	else:
		print(list)
		print("This position is already allocated.Try an unallocated one..")

size=int(input("Enter the storage size:\t"))
list=[0]*2*size
ind=[0]*size
l=0
main()
while(1):
	flag=input("\nDo yo wnat to allocate more(Y/N):\t")
	if(flag=='Y'or flag=='y'):
		ind[l]=-1
		l+=1
		main()
	else:
		print(list)
		for i in range(0,l):
			if(ind[i]==-1):
				print()
			else:
				print(ind[i],'-->',end='')
		print("\naborting......")
		exit()