i=input("enter the value")
    count=0
    if(i<0):
        print("enter positive  integer")
    else:
        while(i!=0):
            i=i/10
            count=count+1
    print"count=",count


