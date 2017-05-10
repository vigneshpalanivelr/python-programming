a=input("Enter the first interval")
    b=input("enter the second interval")
    if(a>0):
        if(a%2==0):
            a=a+2
            while(a<b):
                print"printng", a
                a=a+2
        else:
            a=a+1
            while(a<b):
                print"printng", a
                a=a+2
    else:
        print"type positive input"

