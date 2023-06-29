print("This program is to check prime number or not")
num=int(input("Enter Number : "))

i=2
while num >i:
    if num%i==0:
        print("Its not prime num")
        break

    i+=1
if num==i:
    print("Its prime number")







