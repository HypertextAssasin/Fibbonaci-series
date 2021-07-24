x=int(input("Enter how many numbers of the fibbonaci series you want to print."))
list1=[0,1]
if x == 1:
    print("0")
elif x == 2:
    print(0) 
    print("1")
else:
    
    for i in range(1,x):
        nextNum = list1[i] + list1[i-1]
        list1.append(nextNum) 
    for i in list1:
        print(i)
                                                            
    
  