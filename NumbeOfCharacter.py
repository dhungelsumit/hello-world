def calculate(a,b,count,i):
    if i<len(a):
        if a[i]==b:
            count=count+1
            i=i+1
        else:
            i=i+1
        calculate(a,b,count,i)
    else:
        print(count)
      




def inputa():
    b=input("Enter the character ")
    if len(b)>1 or len(b)==0:
        inputa()
    else:
        return b
a=input("Enter the sentence ")
b=inputa()
count=0
i=0
calculate(a,b,count,i)
 
