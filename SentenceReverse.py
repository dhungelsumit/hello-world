def reverse():
    a=input("Enter a text ")
    print("\n")
    en=len(a)
    b=""
    for j in range(len(a)-1, -1, -1):
        if a[j]==" " or j==0:
            st=j+1
            if j==0:
                st=0
            for k in range (st,en):
                b=b+a[k]
            b=b+" "    
            en=st
        
    
    print(b)

reverse()
