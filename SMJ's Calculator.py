def rep():
    while True:
        z = input("\nDo You Want To Repeat ? (Yes/No) : ")
        if z.lower() == "no" :
            print("\nThank You For Using SMJ's Calculator !!!")
            c=0
            break
            
        elif z.lower() == "yes" :
            c=1
            break
            
        else:
            print("\nPlease Enter a Valid Response !!!")
            continue
    return c


print("\tSMJ's CALCULATOR !!!")
print("\t--------------------")
while True : 
    x = input("\nEnter The Exprerssion To Be Executed  : ")
    y = eval(x)
    print("Answer : ", y)
    d=rep()
    if d==0:
        break
