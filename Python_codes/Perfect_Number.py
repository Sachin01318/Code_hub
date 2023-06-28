try :
    num=int(input("Enter the number : "))
    divisor=1
    sum=0

    while num > divisor:
        if num % divisor==0:
            sum = sum + divisor
        divisor+=1
    if sum==num :
        print(f"{num} is perfect number")
    else:
        print(f"{num} is not perfect number")
except ValueError:
        print("You have Entered invalid number , Please Enter Integer number")




