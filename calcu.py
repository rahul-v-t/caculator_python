def calculator(a,b,c):
    if(c=="+"):
        sum = a + b
        print("sum is :",sum)
    elif(c=="-"):
        dif = a - b
        print("Difference is :",dif)
    elif(c=="*"):
        mul = a * b
        print("Product is :",mul)
    elif(c=="/"):
        div = a / b
        print("Division is :",div)
    else:
        print("Invalid operation")
calculator(2,4,"%")
