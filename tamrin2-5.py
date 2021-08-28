game=[['_','_','_'],
      ['_','_','_'],
      ['_','_','_']]
f=0
import random
def underline():
    for i in range(3):
        for j in range(3):
            print(game[i][j], end=' ')
        print()
def wininig_condition():
    for k in range(3):
        l = 0
        for m in range(3):
            if game[k][m]=='X':
                l+=1
                if l==3:
                    print("player one wins")
                    exit()
    for k in range(3):
        l = 0
        for m in range(3):
            if game[k][m] == 'O':
                l += 1
                if l == 3:
                    print("player two wins")
                    exit()
    for m in range(3):
        l = 0
        for k in range(3):
            if game[k][m] == 'X':
                l += 1
                if l == 3:
                    print("player one wins")
                    exit()
    for m in range(3):
        l = 0
        for k in range(3):
            if game[k][m] == 'O':
                l += 1
                if l == 3:
                    print("player two wins")
                    exit()
    if game[0][0]=='X'and game[1][1]=='X'and game[2][2]=='X':
        print("player one wins")
        exit()
    elif game[0][0]=='O' and game[1][1]=='O'and game[2][2]=='O':
        print("player two wins")
        exit()
    elif game[0][2]=='X'and game[1][1]=='X'and game[2][0]=='X':
        print("player one wins")
        exit()
    elif game[2][0]=='O' and game[1][1]=='O'and game[0][2]=='O':
        print("player two wins")
        exit()



def twoplayer():
    global f
    while True:

        row = int(input("Please enter your row:"))
        col = int(input("please enter your column:"))
        if f%2==0 and 0<=row<3 and 0<=col<3:
            if game[row][col]== '_':
                game[row][col] = 'X'
                f+=1
            else:
                print("That is not empty")
            underline()
            wininig_condition()

        elif f%2==1 and 0<=row<3 and 0<=col<3 :
            if game[row][col]== '_':
                game[row][col] = 'O'
                f+=1
            else:
                print("That is not empty")
            underline()
            wininig_condition()
        else:
            print("Enter row and columns between 0=< and <2")

def single_player():
    global f
    while True:

        if f % 2 == 0 :
            row = int(input("Please enter your row:"))
            col = int(input("please enter your column:"))
            if 0 <= row < 3 and 0 <= col < 3:
                if game[row][col] == '_':
                    game[row][col] = 'X'
                    f += 1
                else:
                    print("Enter row and columns between 0=< and <2")


        wininig_condition()
        if   f%2==1:
            row = random.randint(0, 2)
            col = random.randint(0, 2)
            if 0<=row<3 and 0<=col<3:
                if game[row][col]== '_':
                    game[row][col] = 'O'
                    f+=1
                else:
                    pass
        underline()
        wininig_condition()


n= int (input("Welcome to tic toc toe game \nfor single play Please enter one and for two players please enter 2:"))
if n == 1 :
    single_player()
elif n== 2 :
    twoplayer()
else:
    print("You have to choose between 1 and 2")