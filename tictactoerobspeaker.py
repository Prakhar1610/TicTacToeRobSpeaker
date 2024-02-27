import random as rd
import gtts as g
import playsound as ps

# function for printing board
def board(P1x , P2o) :
    # to check values of both player at a particular location according to what what position they have entered
    one = choice_1 if P1x[0] else (choice_2 if P2o[0] else 1)
    two = choice_1 if P1x[1] else (choice_2 if P2o[1] else 2)
    three = choice_1 if P1x[2] else (choice_2 if P2o[2] else 3)
    four = choice_1 if P1x[3] else (choice_2 if P2o[3] else 4)
    five = choice_1 if P1x[4] else (choice_2 if P2o[4] else 5)
    six = choice_1 if P1x[5] else (choice_2 if P2o[5] else 6)
    seven = choice_1 if P1x[6] else (choice_2 if P2o[6] else 7)
    eight = choice_1 if P1x[7] else (choice_2 if P2o[7] else 8)
    nine = choice_1 if P1x[8] else (choice_2 if P2o[8] else 9)
    print(f" {one} | {two} | {three} ")
    print("---|---|---")
    print(f" {four} | {five} | {six} ")
    print("---|---|---")
    print(f" {seven} | {eight} | {nine} ")

# function to decide winnner
def winner(P1x , P2o , check_win) :
    # checking all possible ways in which P1 can win
    if ((P1x[0] == choice_1 and P1x[1] == choice_1 and P1x[2] == choice_1) or 
    (P1x[0] == choice_1 and P1x[3] == choice_1 and P1x[6] == choice_1) or 
    (P1x[6] == choice_1 and P1x[7] == choice_1 and P1x[8] == choice_1) or 
    (P1x[2] == choice_1 and P1x[5] == choice_1 and P1x[8] == choice_1) or 
    (P1x[1] == choice_1 and P1x[4] == choice_1 and P1x[7] == choice_1) or 
    (P1x[3] == choice_1 and P1x[4] == choice_1 and P1x[5] == choice_1) or
    (P1x[0] == choice_1 and P1x[4] == choice_1 and P1x[8] == choice_1) or 
    (P1x[2] == choice_1 and P1x[4] == choice_1 and P1x[6] == choice_1)) :
        check_win = check_win + 1
        return check_win

    # checking all possible ways in which P2 can win
    elif ((P2o[0] == choice_2 and P2o[1] == choice_2 and P2o[2] == choice_2) or 
    (P2o[0] == choice_2 and P2o[3] == choice_2 and P2o[6] == choice_2) or 
    (P2o[6] == choice_2 and P2o[7] == choice_2 and P2o[8] == choice_2) or 
    (P2o[2] == choice_2 and P2o[5] == choice_2 and P2o[8] == choice_2) or 
    (P2o[1] == choice_2 and P2o[4] == choice_2 and P2o[7] == choice_2) or
    (P2o[3] == choice_2 and P2o[4] == choice_2 and P2o[5] == choice_2) or 
    (P2o[0] == choice_2 and P2o[4] == choice_2 and P2o[8] == choice_2) or 
    (P2o[2] == choice_2 and P2o[4] == choice_2 and P2o[6] == choice_2)) :
        check_win = check_win - 1
        return check_win

# funtion for toss
def toss(P1_toss , P2_toss) :
    h_and_t  = rd.choice(["H" , "h" , "T" , "t"])
    if(h_and_t == P1_toss) :
        return P1
    if(h_and_t == P2_toss) :
        return P2

if __name__ == "__main__":

    text1 = "Welcome to Tic Tac Toe"
    sound1 = g.gTTS(text1 , lang = "en")
    sound1.save("sound1.mp3")
    print("Welcome to Tic Tac Toe")
    ps.playsound("sound1.mp3")

    g.gTTS("Enter your name Player1" , lang = "en").save("sound2.mp3")
    ps.playsound("sound2.mp3")
    P1 = input("Enter your name Player1:\n")

    
    g.gTTS("Enter your name Player2" , lang = "en").save("sound3.mp3")
    ps.playsound("sound3.mp3")
    P2 = input("Enter your name Player2:\n")

    P1x = [0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0] # list to store choice of P1(x or o)
    P2o = [0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0] # list to store choice of P2(x or o)

    print("Rules-")
    g.gTTS("Rules" , lang = "en").save("sound4.mp3")
    ps.playsound("sound4.mp3")

    print("Players you will use the number keys to fill the box you want")
    g.gTTS("Players you will use the number keys to fill the box you want" , lang = "en").save("sound5.mp3")
    ps.playsound("sound5.mp3")

    turn = 0 # this will help to switch chances between players
    check_win = 0
    limit_P1 = 0 # to store total number of moves P1 can make which is 5
    limit_P2 = 0 # to store total number of moves P2 can make which is 4
   
    print("Enter your between H(Head) and T(Tail) for toss")
    g.gTTS("Enter your between H(Head) and T(Tail) for toss" , lang = "en").save("sound6.mp3")
    ps.playsound("sound6.mp3")

    g.gTTS(f"{P1} Enter H or T" , lang = "en").save("sound7.mp3")
    ps.playsound("sound7.mp3")
    P1_toss = input(P1+" Enter H or T:\n")

    g.gTTS(f"{P2} Enter H or T" , lang = "en").save("sound8.mp3")
    ps.playsound("sound8.mp3")
    P2_toss = input(P2+" Enter H or T:\n")

    wintoss = toss(P1_toss , P2_toss)

    if wintoss == P1 :
        print(P1 + " won the toss")
        g.gTTS(f"{P1} won the toss" , lang = "en").save("sound9.mp3")
        ps.playsound("sound9.mp3")
        
        print("Winner will get to chose first")
        g.gTTS("Winner will get to chose first" , lang = "en").save("sound11.mp3")
        ps.playsound("sound11.mp3")


        print(P1 + " Enter your choice between x and o")
        g.gTTS(f"{P1} Enter your choice between x and o" , lang = "en").save("sound13.mp3")
        ps.playsound("sound13.mp3")

        choice_1  = input(P1+" Enter your choice- ") # choice of P1
        choice_2  = input(P2+" Enter your choice- ") # choice of P2

        while(True):
            board(P1x , P2o)
            if turn == 0 :
                n = int(input(P1+" Enter the position at which you want to make "+choice_1+"- "))
                P1x[n-1] = choice_1
                turn = turn + 1
                limit_P1 = limit_P1 + 1
            else :
               n = int(input(P2+" Enter the position at which you want to make "+choice_2+"- ")) 
               P2o[n-1] = choice_2
               turn = turn - 1
               limit_P2 = limit_P2 + 1
            
            win = winner(P1x , P2o , check_win)
    
            if win == 1 :
                board(P1x , P2o)
                print(P1+" wins")
                break
            elif win == -1 :
                board(P1x , P2o)
                print(P2+" wins")
                break
            # for checking whether the match is draw or not
            if (limit_P1 == 5) and (limit_P2 == 4) :
                board(P1x , P2o)
                print("Draw")
                break

    elif(wintoss == P2) :
        print(P2 + " won the toss")
        g.gTTS(f"{P2} won the toss" , lang = "en").save("sound10.mp3")
        ps.playsound("sound10.mp3")

        print("Winner will get to chose first")
        g.gTTS("Winner will get to chose first" , lang = "en").save("sound12.mp3")
        ps.playsound("sound12.mp3")

        print(P2 + " Enter your choice between x and o")
        g.gTTS(f"{P2} Enter your choice between x and o" , lang = "en").save("sound14.mp3")
        ps.playsound("sound14.mp3")

        choice_2  = input(P2+" Enter your choice- ") # choice of P2
        choice_1  = input(P1+" Enter your choice- ") # choice of P1

        while(True):
            board(P1x , P2o)
            if turn == 0 :
                n = int(input(P2+" Enter the position at which you want to make "+choice_2+"- ")) 
                P2o[n-1] = choice_2
                turn = turn - 1
                limit_P2 = limit_P2 + 1
               
            else :
                n = int(input(P1+" Enter the position at which you want to make "+choice_1+"- "))
                P1x[n-1] = choice_1
                turn = turn + 1
                limit_P1 = limit_P1 + 1
            
            win = winner(P1x , P2o , check_win)
    
            if win == 1 :
                board(P1x , P2o)
                print(P1+" wins")
                g.gTTS(f"{P1} wins" , lang = "en").save("sound15.mp3")
                ps.playsound("sound15.mp3")
                break
            elif win == -1 :
                board(P1x , P2o)
                print(P2+" wins")
                g.gTTS(f"{P2} wins" , lang = "en").save("sound16.mp3")
                ps.playsound("sound16.mp3")
                break
            # for checking whether the match is draw or not
            if (limit_P1 == 5) and (limit_P2 == 4) :
                board(P1x , P2o)
                print("Draw")
                g.gTTS("Draw" , lang = "en").save("sound17.mp3")
                ps.playsound("sound17.mp3")
                break