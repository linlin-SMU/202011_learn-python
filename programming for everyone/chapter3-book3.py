#3
score = input('what is the score?\n')
try:
    score1 = float (score)
except:
    print('Bad score')
    quit()
     
if score1 >= 0.9:
     print('A')
elif score1 >= 0.8:
     print('B')
elif score1 >= 0.7:
     print('C')
elif score1 >= 0.6:
     print('D')
else:
     print('F')
