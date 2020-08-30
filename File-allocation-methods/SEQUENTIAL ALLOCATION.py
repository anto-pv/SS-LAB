'''SEQUENTIAL ALLOCATION'''
flag=1
success=1
size=int(input("Enter the storage size:\t"))
list=[0]*size
while(flag==1):
	st = int(input("Enter starting index:\t"))
	len = int(input("Enter length:\t"))
	for i in range(st,(st+len)):
		n=0
		if(list[i]==0):
			list[i]=1
			n=n+1
		else:
			print("already allocated...cannot continue..aborting...")
			success=0
			break
	if(success==1):
		print("allocated successfully:")
		print(list)
		n =input("Do you want to continue?(Y/N):\t")
		if(n!='Y' and n!='y'):
			flag=0
			break
	else:
		break




