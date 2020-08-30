'''INDEXED ALLOCATION'''
def main():
	global list
	flag=1
	success=1
	while(flag==1):
		st = int(input("Enter index block no:"))
		if(list[st]==0):
			list[st]=1
			n= int(input("Enter no.of blocks:"))
			for i in range(0,n):
				j=int(input("Enter the index number:"))
				if(list[j]==0):
					list[j]=1
				else:
					print("This position is already allocated...\naborting...")
					print(list)
					exit()
			if(success==1):
				print(list)
				break
		else:
			print("This position is already allocated.Try an unallocated one..")
size=int(input("Enter the storage size:"))
list=[0]*size
main()
while(1):
	lag=input("Do you want to allocate more(Y/N)\t:")
	if(lag=='Y' or lag=='y'):
		main()
	else:
		print(list)
		print("aborting......")
		exit()








