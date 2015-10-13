def calculate(a,count):
    b=a
    b=b%10
    if b==7:
        count=count+1
    a=a//10
    if a==0:
        return count
    else:
        return calculate(a,count)

a=int(input("Enter a integer "))
count=0
sevens=(calculate(a,count))
print("Total number of 7 is ",sevens)    
