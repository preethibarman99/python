#for loop
num=int(input("enter the number"))
for i in range(2,int(num/2)):
    if num%i ==0:
        print("not prime")
        break
    else:
        print("prime number") 

        
        
