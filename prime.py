#TO FIND PRIME NUMBERS BETWEEN TWO NUMBERS

a=int(input("Enter first number "))
b=int(input("Enter second number "))

if a>b:
    temp=b
    b=a
    a=temp


for num in range (a,b+1):
    if num > 1:
       for i in range(2,num):
           if (num % i) == 0:
               break
       else:
           print(num)
