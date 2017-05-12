    a=input("Enter the number")
    b=a-1
    if(a>0):
        for i in range(1,b):
            a=a*b
            b=b-1
        print"factorial",a
    else:
        print"Enter positiive only"
