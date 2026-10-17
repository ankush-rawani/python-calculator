#Calculator
while True:
    print("1.addition")
    print("2.subtraction")
    print("3.multiplication")
    print("4.division")
    print("5.modulus")
    print("6.factorial")
    print("7.power")
    print("8.percentage")
    print("9.square root")
    print("10.absolute")
    print("11.exit")
    U_input=int(input("Enter your choice"))   #U_input here and every time in code is user input
    if U_input==11:
        print("THANK YOU")
        break
    elif U_input==6:
        num = int(input("Enter a number: "))
        fact=1
        if num<0:
            print("invalid")
        else:
            for i in range(1, num + 1):
                fact = fact * i
            print("Factorial:", fact)
    elif U_input in (1,2,3,4,5,7,8):
        Num_1=float(input("Enter 1st number"))
        Num_2=float(input("Enter 2nd number"))  
        if U_input==1:
            print(Num_1 + Num_2)
        elif U_input==2:
            print(Num_1 - Num_2)
        elif U_input==3:
            print(Num_1 * Num_2)
        elif U_input==4:
            if Num_2!=0:
                print(Num_1 / Num_2)
            else:
                print("division by zero is not possible")
        elif U_input==5:
             if Num_2!=0:
                print(Num_1 % Num_2)
             else:
                print("division by zero is not possible")
        elif U_input==7:
            print(Num_1**Num_2)
        elif U_input==8:
            Percent=Num_1/100
            print(Percent*Num_2)
    elif U_input==9:
        num1=float(input("Enter number whose sqrt is need"))
        if num1<0:
            print("sqrt does not exist for negative number's")
        else:
            print(num1**0.5)
    elif U_input==10:
        NUM=float(input("Enter number"))
        print(abs(NUM))
    else:
        print("Invalid choice! Please select 1 to 11.")

           
