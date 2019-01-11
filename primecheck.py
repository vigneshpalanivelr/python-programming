a,b1= [int(x) for x in input().split()]  
for num in range(a,b1+1):  
   if num > 1:  
       for i in range(2,num):  
           if (num % i) == 0:  
               break  
       else:  
           print(num,'')
