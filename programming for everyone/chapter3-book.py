
#1
EH = input('Enter Hours:')
ER = input('Enter Rates:')
FH = float(EH)
FR = float(ER)
if FH > 40:
    FPay = (FH - 40) * 1.5 * FR + 40 * FR
else:
    FPay = FH * FR
print('Pay:',FPay)