def computegrade(Vera):
    Ts = input('Enter your score:')
    try:
        Fs = float(Ts)
        Fs <= 1  #how to limit the Fs less than 1？？？
    except:
        print('Enter a number less than 1, please')

    if Fs >= 0.9 and Fs <= 1:
        pass
        return'A'
    elif Fs >= 0.8 and Fs < 0.9:
        return'B'
    else:
        return'bad score'

Lily = 124
print('Lily Grade: ', computegrade(Lily))
