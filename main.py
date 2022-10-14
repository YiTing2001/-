import random

player = []
ai = []

def init():
    for i in range(0,3) :
        player.append([0,0,0])
        ai.append([0,0,0])

def check():
    p=0
    a=0
    for i in range(0,3):
        for j in range(0,3):
            if(player[i][j]==0):
                p=1
            if(ai[i][j]==0):
                a=1
    if(p==1 and a==1):
        return True
    else:
        return False

def player_move(x):
    c = input()
    i = 0
    if(c=='K'):
        i=0
    elif(c=='E'):
        i=1
    elif(c=='X'):
        i=2
    else:
        print(c,' line does not exist,please input again:')
        player_move(x)
        return
    flag=False
    for j in range(0,3):
        if(player[i][j]==0):
            flag=True
            player[i][j]=x
            for l in range(0,3):
                if(ai[i][l]==x):
                    ai[i][l]=0
            break
    if(flag==False):
        print(c,' line is full,please input again:')
        player_move(x)
        return


def ai_move(y):
    i=random.randint(0, 2)
    flag = False
    for j in range(0,3):
        if(ai[i][j]==0):
            flag = True
            ai[i][j]=y
            for l in range(0,3):
                if(player[i][l]==y):
                    player[i][l]=0
            break
    if (flag == False):
        ai_move(y)
        return
    if (i == 1):
        print("the computer moves in K line")
    elif (i == 2):
        print("the computer moves in E line")
    elif (i == 2):
        print("the computer moves in X line")



def win():
    ai_score = 0
    player_score = 0
    cnt = []
    fg = []
    for i in range(0,3):
        cnt.append([0, 0, 0, 0, 0, 0, 0])
        cnt.append([0, 0, 0, 0, 0, 0, 0])
        fg.append([0, 0, 0, 0, 0, 0, 0])
        fg.append([0, 0, 0, 0, 0, 0, 0])
        for j in range(0,3):
            if(player[i][j]!=0):
                cnt[0][player[i][j]]+=1
            if(ai[i][j]!=0):
                cnt[1][ai[i][j]]+=1
        for j in range(0,3):
            if(player[i][j]!=0):
                if(fg[0][player[i][j]]==0):
                    fg[0][player[i][j]]=1
                    player_score+=player[i][j]*cnt[0][player[i][j]]*cnt[0][player[i][j]]
            if(ai[i][j]!=0):
                if(fg[1][ai[i][j]]==0):
                    fg[1][ai[i][j]]=1
                    ai_score+=ai[i][j]*cnt[1][ai[i][j]]*cnt[1][ai[i][j]]
        cnt = []
        fg = []
    print("your score is:",player_score)
    print("computer score is:",ai_score)
    if(player_score>ai_score):
        return True
    else:
        return False

def show():
    print("player:")
    for i in range(0,3):
        for j in range(0,3):
            print("    ",player[i][j],end='')
        print("")
    print("computer:")
    for i in range(0,3):
        for j in range(0,3):
            print("    ",ai[i][j],end='')
        print("")

def easy_num():
    a=random.randint(3, 5)
    b=random.randint(0, 1)
    x=a+b
    return x

def normal_num():
    x=random.randint(1, 6)
    return x

def hard_num():
    a=random.randint(1, 2)
    b=random.randint(0, 1)
    c=random.randint(0, 1)
    d=random.randint(0, 1)
    x=a+b+c+d
    return x

def easy_mode():
    cnt=0
    while(check()):
        cnt+=1
        if(cnt&1):
            x=0
            if(cnt%3==0):
                x=normal_num()
            else:
                x=easy_num()
            print("the score you get is:",x)
            print("please input the line you want to move:")
            player_move(x)
        else:
            y=0
            if(cnt%4==0):
                y=normal_num()
            else:
                y=hard_num()
            print("the score computer get is:",y)
            ai_move(y)
        show()

def normal_mode():
    cnt=0
    while(check()):
        cnt+=1
        if(cnt&1):
            x=normal_num()
            print("the score you get is:",x)
            print("please input the line you want to move:")
        else:
            y=normal_num()
            print("the score computer get is:",y)
            ai_move(y)
        show()

def hard_mode():
    cnt=0
    while(check()):
        cnt+=1
        if(cnt&1):
            x=0
            if(cnt%3==0):
                x=normal_num()
            else:
                x=hard_num()
            print("the score you get is:",x)
            print("please input the line you want to move:")
            player_move(x)
        else:
            y=0
            if(cnt%4==0):
                y=normal_num()
            else:
                y=hard_num()
            print("the score computer get is:")
            ai_move(y)
        show()

def work():
    init()
    print("easy:1")
    print("normal:2")
    print("hard:3")
    print("please choose how hard you want to play:")
    opt=input()
    if(opt=='1'):
        easy_mode()
    elif(opt=='2'):
        normal_mode()
    else:
        hard_mode()
    if(win()):
        print("Congratulations!You win!!!")
    else:
        print("Sorry,You lose.")


if __name__ == '__main__':
    work()
