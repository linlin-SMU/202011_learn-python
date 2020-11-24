#2
print('Hello')
EH = input('Enter Hours:')
ER = input('Enter Rates:')
try:
     FH = float(EH)
     FR = float(ER)
     print(FH,FR)
except:
    print('Error, please enter numeric input')
    quit()

if FH > 40:
    FPay = (FH - 40) * 1.5 * FR + 40 * FR
else:
    FPay = FH * FR
print('Pay:',FPay)
