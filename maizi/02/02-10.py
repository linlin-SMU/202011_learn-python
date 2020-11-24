import random
command = 'Y'
while command == 'Y':  # == 表示逻辑判断
    computer = random.randint(1,3)
    print(computer)
    # 环境变量为指定某个程序的路径，因此终端（cmd、pycharm）可以直接找到，
    player = input('请出招：')
    if player == 4:
        command = player
        quit
    elif player > 0 and < 4:
        if (player ==1 and computer ==3) or (player == 2 and computer == 1) or (player == 3 and computer ==1):
            print('player')
        elif (player == 1 and computer == 1):
            print('balance')
        else:
            print('computer')
print('Thank you for using it!')