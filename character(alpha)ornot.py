c=input("Enter the value")
    d=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    if(c in d):
        print("alphabet")
    elif(type(c==int)):
        print("number")
    else:
        print("unknown")
