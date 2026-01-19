num=int(input("enter a number:"))
if num<=1:
    print("not prime")
else:
    is_prime=true
    for i in range(2,num):
        if num%i==0:        
            is_prime=False
            break
    if is_prime:
        print("prime")
    else:
        print("not prime")
        


    
