"""
Craps赌博游戏
玩家摇两颗色子 如果第一次摇出7点或11点 玩家胜
如果摇出2点 3点 12点 庄家胜 其他情况游戏继续
玩家再次要色子 如果摇出7点 庄家胜
如果摇出第一次摇的点数 玩家胜
否则游戏继续 玩家继续摇色子
玩家进入游戏时有1000元的赌注 全部输光游戏结束

Version: 0.1
Author: 骆昊
Date: 2018-03-02
"""
from random import randint

while True:
    YesOrNo = str(input('是否确定变卖家当来参与游戏(YES/NO):')).upper()
    if YesOrNo == 'NO':
        print('你确定你的意志足够坚定？也许吧朋友。真正的深渊来自于人们的内心')
        break
    elif YesOrNo == 'YES':
        print('欢迎进入深渊! 我尊贵的客人')
    else:
        print('小鬼，你确定面对深渊你的小伎俩是否真的有效？')
    money = int(input('你的总资产为:'))
    while money > 0:
        needs_go_on = False
        while True:
            debt = int(input('请下注(%d): ' % money))
            if 0 < debt <= money:
                break
            else:
                print('尊贵的客人，您剩余的资产为:(%d)' % money)
        first = randint(1, 6) + randint(1, 6)
        print('玩家摇出了%d点' % first)
        if first == 7 or first == 11:
            money += debt
            print('玩家胜! 客人您的手气可真是旺啊，想必客人今天一定会大杀四方。')
        elif first == 2 or first == 3 or first == 12:
            money -= debt
            print('庄家胜! 要不是客人您手下留情，庄家肯定是要输的。')
        else:
            needs_go_on = True

        while needs_go_on:
            current = randint(1, 6) + randint(1, 6)
            print('玩家摇出了%d点' % current)
            if current == 7:
                money -= debt
                needs_go_on = False
                print('庄家胜! 好险啊，客人是我见过手气最好的那一批客人。')
            elif current == first:
                money += debt
                needs_go_on = False
                print('玩家胜! 客人您的手气可真是旺啊，想必客人今天一定会大杀四方。')

    print('你破产了, 游戏结束!你小子最好别闹事，乖乖滚蛋! ')


if __name__ == '__main__':
    print()
