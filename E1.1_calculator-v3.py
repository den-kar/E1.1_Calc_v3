def getCalcOperation():
    calcOperations = ["+", "-", "*", "/", "%", "**", "!"]
    while True:
        calcOp = input("Wählen + - * / % ** ! : ")
        if calcOp not in calcOperations:
            print ("Keine gültige Rechenoperation. Nochmal")
            continue
        else:
            break
    return calcOp

def getNumber(n,calcOp):
    while True:
        try:
            number = float(input("Ganze Zahl " + str(n) + "          : "))
            if calcOp == "!" and (number < 0 or number != int(number)):
                print ("Faktultät nur mit ganzen Zahlen größer gleich 0. Nochmal")
                continue
            elif calcOp == "/" and number == 0:
                print ("Nicht durch 0 teilbar. Nochmal")
                continue
        except ValueError:
            print ("Das war keine ganze Zahl. Nochmal")
            continue
        else:
            break
    return number

def calculation(number1,number2,calcOp):
    while True:
        if calcOp == "!":
            erg = 1
            number1 = int(number1)
            for i in range(2,number1+1):
                erg *= i
            print ("Ergebis               : " + str(erg))
            break
        else:
            erg = eval(str(number1) + calcOp + str(number2))
            print ("Ergebis               : " + str(erg))
            break

while True:
    print ("""
Calculator start: """)
    calcOp = getCalcOperation()
    num1 = getNumber(1,calcOp)
    if calcOp == "!":
        num2 = 0
    else:
        num2 = getNumber(2,calcOp)
    calculation(num1,num2,calcOp)
    
    restartInputList = ["y", "yes", "j", "ja"]
    restartCalculation = input("""
Nochmal?
Ja            [   y   ]
Nein          [any key]
""")
    if restartCalculation.lower() not in restartInputList:
        break
