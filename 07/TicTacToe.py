#!/usr/bin/env python

def evaluate(b) :
    for i in range(3) :
        if b[i][0]==b[i][1] and b[i][1]==b[i][2] :
            if b[i][0]=='x' :
                return 1
            elif b[i][0]=='o' :
                return -1
        if b[0][i]==b[1][i] and b[1][i]==b[2][i] :
            if b[0][i]=='x' :
                return 1
            elif b[0][i]=='o' :
                return -1
    if b[0][0]==b[1][1] and b[1][1]==b[2][2] :
        if b[0][0]=='x' :
            return 1
        elif b[0][0]=='o' :
            return -1
    if b[0][2]==b[1][1] and b[1][1]==b[2][0] :
        if b[0][2]=='x' :
            return 1
        elif b[0][2]=='o' :
            return -1
    return 0

def ismovesleft(b) :
    for i in range(3) :
        for j in range(3) :
            if b[i][j]!='x' and b[i][j]!='o' :
                return True
    return False

def displayboard(b,turn) :
    print("\tTic-Tac-Toe")
    print("Player 1 (x) , Player 2 (o)")
    print("Turn : Player ",turn)
    for i in range(3) :
        for j in range(3) :
            print(" ",b[i][j],end="")
        print()
    
def checkboard(b,c) :
    for i in range(3) :
        for j in range(3) :
            if c==b[i][j] :
                return c
    c=int(input("Invalid Choice , Enter Again (1-9) : "))
    return checkboard(b,c)

nextgame=True
while nextgame :
    board=[[1,2,3],[4,5,6],[7,8,9]]
    turn=1
    while True :
        displayboard(board,turn)
        choice=int(input("Enter number (1-9) : "))
        choice=checkboard(board,choice)
        board[(choice-1)//3][(choice-1)%3]='x' if turn==1 else 'o'
        result=evaluate(board)
        turn=2 if turn==1 else 1
        if result==1 :
            print("------ Player 1 wins ------")
            break
        elif result==-1 :
            print("------ Player 2 wins ------")
            break
        if not ismovesleft(board) :
            print("------ -----DRAW----- ------")
            break
    nextgame=int(input("Press 1 and enter for next game : "))