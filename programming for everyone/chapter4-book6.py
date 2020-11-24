def computepay(Vera):
    Wt = input('Enter your worktime:')
    Wr = input('Enter your pay rate:')
    try:
        Ft = float(Wt)
        Fr = float(Wr)
    except:
        print('Enter a number, please')

    if Ft > 40:
        APay = 40 * Fr + (Ft - 40) * Fr * 1.5
    else:
        APay = Ft * Fr
    return APay

Lily = 1234
print(computepay(Lily))
