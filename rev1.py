    a=input("Enter the input")
    rev=0
    if(a>0):
        while(a>0):
            rem=a%10
            rev=rev*10+rem
            a=a/10
        print rev
    else:
        print "0"

