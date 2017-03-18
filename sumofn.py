a=input("Enter the number of natural numbers to sum")
    if a < 0:
         print("Enter a positive number")
    else:
        s= 0
    while(a > 0):
       s=s+a
       a=a-1
    print"The sum is",s
