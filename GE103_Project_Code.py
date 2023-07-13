from playsound import playsound #This library is used to play mp3 files in python code.
#playsound('welcome.mp3')  #playsound is function used to run mp3 files
print('Welcome to Tic Tac Toe')
import random

'''Logic for tic tac toe:- We are using two lists initialised as a=[0,1,2,3,4,5,6,7,8]  b=[0,0,0,0,0,0,0,0,0].
As any position in list "a" is replaced by by 'O' or x , the corresponding position in list 'b' is replaced by -1 or 1 respectively.'''

'''This function is used to print 3*3 Tic Tac Toe board according to the input list "a" using print function. '''
def boxprint(a):
            print(f" {a[0]} | {a[1]} | {a[2]}") #here the f-string used to store variable inside a string for Row 1.
            print(f" --|---|--") # these are the divider lines between two rows that is row 1 and row 2
            print(f" {a[3]} | {a[4]} | {a[5]}") #similarly as above this is used for row 2.
            print(f" --|---|--") #divider to row 2 and row 3
            print(f" {a[6]} | {a[7]} | {a[8]}") # to print row 3

'''How to decide a winning or draw state:- When the list 'b' containing -1 or 1 or 0 is written in sequence of 3*3 matrix, if the first
three elements of the list 'a' are 'x' ,so the sum of the first three elements of list b is 3. 

This funtion is used to return an integer value 1,-1 or 0 if the current state of the Tic Tac Toe board is giving a result of win, loss,
or draw otherwise return none.'''
def check_result(b):
            if b[0]+b[1]+b[2]==3 or b[3]+b[4]+b[5]==3 or b[6]+b[7]+b[8]==3:
                return 1
            elif b[0]+b[1]+b[2]==-3 or b[3]+b[4]+b[5]==-3 or b[6]+b[7]+b[8]==-3:
                return -1
            elif b[0]+b[3]+b[6]==3 or b[1]+b[4]+b[7]==3 or b[2]+b[5]+b[8]==3:
                return 1
            elif b[0]+b[3]+b[6]==-3 or b[1]+b[4]+b[7]==-3 or b[2]+b[5]+b[8]==-3:
                return -1
            elif b[0]+b[4]+b[8]==3 or b[2]+b[4]+b[6]==3:
                return 1
            elif b[0]+b[4]+b[8]==-3 or b[2]+b[4]+b[6]==-3:
                return -1
            '''Even if all the elements of the list b are replaced by 1 or -1 still if above conditions of win or loss of 
            any of the player is not satisfied , it is obviously a draw. For which below loop is applied.'''
            count=0  
            for i in b:
                if i!=0:
                    count+=1
            if count==9:
                return 0
            '''return none if its neither a win or a loss or a draw'''
            return None



'''This is a recursive function which applies minimax algorithm in python code. It takes list "b" and turn(1 for cross's chance and -1 for 
nought's chance) as input, and return a score of input state of tic tac toe board as  0, -1 or 1 by backtracking , using recursion. '''

def getscore(b,turn):
            '''The base case of recursion is when it is a win, loss or draw state and return 1, -1 or 0 respectively'''
            if check_result(b)==1 :
            
                return 1
            if check_result(b)==-1 :

                return -1
            if check_result(b)==0 :
            
                return 0
            
            '''Turn is 1 when it is cross's chance and is assumed as maximiser'''
            if turn==1:
                '''We initialised the score to large negative number as it is maximizer's turn'''
                score=-1000
                '''This loop will run for all indexes of list b and insert 1 in a temporary copy of list 'b' ,if it is zero now ,
                one by one, to check score for all the possibilities'''
                for i in range(9):
                    
                    temp=b[:]
                    if temp[i]==0:
                        temp[i]=1
                        '''After inserting 1 at the empty place again pass it to self function and change the turn from maximiser to 
                        minimiser. This will go untill the base case is reached.'''
                        tempscore=getscore(temp,turn*(-1))
                        
                        '''As we have initialised score to a large negative number, so if the function returns any larger score than
                        that it will be updated. Eventually it will return the maximum of all the scores'''
                        if tempscore>score :
                            score=tempscore
            
            '''similar is the case of for the turn of nought that is turn is -1'''                
            if turn==-1:
                score=1000
                for i in range(9):
                
                    temp=b[:]
                    if temp[i]==0:
                        
                        temp[i]=-1
                
                        tempscore=getscore(temp,turn*(-1))
                        if tempscore<score :
                            score=tempscore
            '''Finally the score of the input state of a tic tac toe board is returned'''
            return score


'''This function will take  current state of a tic tac toe borad as input and return an index which is the best move for 
computer (computer is given nought and is assumed as maximiser)'''
def bestmove(b):
            '''The maximum score and the index for maximum score is initialised to minimum possible integer'''
            i_for_maxscore=0  
            maxscore=-1
            '''This loop run for all the indexes of a copy of list b , and insert 1 at zero positions one by one.
            Check score for them and keep updating the maximum score and the index for it '''
            for i in range(9):
                temp=b[:]
                if temp[i]==0:
                    temp[i]=1
                    '''maximum score and index for it is updated'''
                    if getscore(temp,-1)>maxscore:
                        maxscore=getscore(temp,-1)
                        
                        i_for_maxscore=i
            '''Finally return the index corresponding to the maximum score, that is the position at which computer will 
            move so that it will be the most optimal move for it'''
            return i_for_maxscore  

#This loop will run again if the player wants to play once more and will break otherwise'''
while True:
    #This loop will run again if the user has given an invaid choice , otherwise break by running once'''
    while True:
        
        #playsound('mode1.mp3')
        print('Press 1 and Enter for Player versus Player mode')
        #playsound('mode2.mp3')
        print('Press 2 and Enter for Player versus Computer mode')
        #playsound('mode3.mp3')
        print("Press 3 and Enter, if you think you can defeat computer. I bet, You can't ")
        
        #Player is asked for three choices, 
        #1 for a human vs human game
        #2 for a human vs computer game 
        #3 for the human vs computer game with undefeatable computer(where we have used minimax algorithm)'''
        choice=int(input())
        if choice==1 or choice==2 or choice==3:

            
            # choice=1 for a human vs human game
            if choice==1:
                a=[0,1,2,3,4,5,6,7,8]
                b=[0,0,0,0,0,0,0,0,0]
                
                #Turn is being varied between 1 and -1 , 1 for cross's chance and -1 for nought's chance
                turn=1   #Initial turn is given to crosss
                print('Player 1 has X and Player 2 has O')
                
                #This loop will run untill a game reaches its end
                while True:
                    boxprint(a)  #list a is send to boxprint function for printing tic tac toe board
                    if check_result(b)==1:
                        #playsound('P1won.mp3')
                        print('game over,P1 won')
                        
                        break  #loop will break if p1 wins
                    elif check_result(b)==-1:
                        #playsound('P2won.mp3')
                        print('game over,P2 won')
                        
                        break #loop will break if p2 wins
                    elif check_result(b)==0:
                        #playsound('P1p2draw.mp3')
                        print('game over, match draw better luck next time, both of you')
                        
                        break #loop will break if it is draw
                    
                    #Insert 1 in list b and x in list a , according to player's input
                    if turn ==1:
                        print('x"s chance')
                        value=int(input())
                        if value>-1 and value<9:
                            if b[value]==0:
                                a[value]='x'
                                b[value]=1
                            else:
                                #playsound('invalid.mp3')
                                print('you choose already filled position , try again')
                                turn=(-1)*turn
                        else :
                            #playsound('invalidinput.mp3')
                            print('invalid position please do again')
                            turn=turn*(-1)
                            
                    #Insert 1 in list b and x in list a , according to player's input
                    else:
                        print('0"s chance')
                        value=int(input())
                        if value>-1 and value<9:
                            if b[value]==0:
                                a[value]='O'
                                b[value]=-1
                            else:
                                #playsound('invalid.mp3')
                                print('you choose already filled position , try again')
                                turn=(-1)*turn
                        else :
                            #playsound('invalidinput.mp3')
                            print('invalid position please do again')
                            turn=turn*(-1)
                    
                    #turn is exchanged between -1 and 1 for p1 and p2 chance to alternate   
                    turn=(-1)*turn
            
            
            # choice=2 for a human vs computer game
            if choice==2:
                a=[0,1,2,3,4,5,6,7,8]  #list whose elements will be replaced by o or x as the game proceeeds and is used to print box
                b=[0,0,0,0,0,0,0,0,0]  #list whose elements will be replaced by 1 if 
                print('computer has "X" and you have "O"')
                z=[-1,1]
                turn =z[random.randint(0,1)]  #in this case we randomly give turn to computer or human

                #This loop will run untill  game reaches its end
                while True:
                    boxprint(a) #list a is send to boxprint function for printing tic tac toe board
                    if check_result(b)==1:
                        #playsound('lost.mp3')
                        print('game over, You lost')
                        
                        break #loop will break if computer wins
                    elif check_result(b)==-1:
                        #playsound('won.mp3')
                        print('game over, You won')
                        
                        break #loop will break if player wins
                    elif check_result(b)==0:
                        #playsound('draw.mp3')
                        print('game over, match draw')
                        
                        break   #loop will break if it is draw
                    
                    #if its  computer's chance
                    if turn ==1:
                        print('computer"s chance')
                        x=0
                        #This loop will run again if the user has choosen already filled position , otherwise break by running once'''
                        while x==0:
                            value=0  #positional input is initialised to zero , will be updated 
                            
                            #following conditions check if there is a winning move for computer 
                            # These are the conditions for attacking move for the computer like the case of two x at 
                            # ...two positions of a row then the computer will move at the unfilled position
                            #Similarly if two positions of a column is filled by x then the computer will move at the unfilled position
                            
                            if (b[0]+b[1]==2 or b[5]+b[8]==2 or b[4]+b[6]==2) and b[2]==0:
                                value=2
                            elif (b[1]+b[2]==2 or b[4]+b[8]==2 or b[3]+b[6]==2) and b[0]==0:
                                value=0
                            elif (b[0]+b[2]==2 or b[4]+b[7]==2) and b[1]==0:
                                value=1
                            elif (b[0]+b[6]==2 or b[4]+b[5]==2) and b[3]==0:
                                value=3
                            elif (b[0]+b[8]==2 or b[2]+b[6]==2 or b[3]+b[5]==2 or b[1]+b[7]==2) and b[4]==0:
                                value=4
                            elif (b[3]+b[4]==2 or b[2]+b[8]==2) and b[5]==0:
                                value=5
                            elif (b[0]+b[3]==2 or b[4]+b[2]==2 or b[7]+b[8]==2) and b[6]==0:
                                value=6
                            elif( b[4]+b[1]==2 or b[8]+b[6]==2) and b[7]==0:
                                value=7
                            elif (b[0]+b[4]==2 or b[2]+b[5]==2 or b[6]+b[7]==2) and b[8]==0:
                                value=8
                                
                            #If not, it will check if it is going to loose in next chance , so defends it
                            #the case of two o at 
                            # ...two positions of a row then the computer will move at the unfilled position
                            #Similarly if two positions of a column is filled by x then the computer will move at the unfilled position
                            #
                            elif (b[0]+b[1]==-2 or b[4]+b[6]==-2 or b[5]+b[8]==-2) and b[2]==0:
                                value=2
                            elif (b[1]+b[2]==-2 or b[3]+b[6]==-2 or b[4]+b[8]==-2) and b[0]==0:
                                value=0
                            elif (b[0]+b[2]==-2 or b[4]+b[7]==-2) and b[1]==0:
                                value=1
                            elif (b[0]+b[6]==-2 or b[4]+b[5]==-2) and b[3]==0:
                                value=3 
                            elif (b[0]+b[8]==-2 or b[2]+b[6]==-2 or b[3]+b[5]==-2 or b[1]+b[7]==-2) and b[4]==0:
                                value=4
                            elif (b[3]+b[4]==-2 or b[2]+b[8]==-2) and b[5]==0:
                                value=5
                            elif (b[0]+b[3]==-2 or b[4]+b[2]==-2 or b[7]+b[8]==-2) and b[6]==0:
                                value=6
                            elif( b[4]+b[1]==-2 or b[8]+b[6]==-2) and b[7]==0:
                                value=7
                            elif (b[0]+b[4]==-2 or b[2]+b[5]==-2 or b[6]+b[7]==-2) and b[8]==0:
                                value=8
                            
                            #else it will run randomly
                            else:
                                value=random.randint(0,8)
                            if b[value]==0:
                                print('computer choose ',value)
                                a[value]='x'   #For players turn 'x' is inserted in list a and 1 in list b
                                b[value]=1
                                x=1
                    #For player's turn , it will ask for an unfilled position
                    elif turn==-1:
                        print('Your chance,enter the position number')
                        value=int(input())
                        if value>-1 and value<9:
                            if b[value]==0:
                                a[value]='o'  #For players turn 'o' is inserted in list a and -1 in list b
                                b[value]=-1
                            else:
                                print('you choose already filled place, please do again')
                                turn=turn*(-1)
                        else :
                            print('invalid position please do again')
                            turn=turn*(-1)
                    
                    #turn is exchanged between -1 and 1 for p1 and p2 chance to alternate 
                    turn=turn*(-1)
            #choice=3 for the human vs computer game with undefeatable computer(where we have used minimax algorithm)   
            if choice ==3:
                a=[0,1,2,3,4,5,6,7,8]  
                b=[0,0,0,0,0,0,0,0,0]  
                print('computer has "X" and you have "O"')
                z=[-1,1]
                turn =z[random.randint(0,1)]

                while True:
                    boxprint(a)
                    if check_result(b)==1:
                        #playsound('lostinomode3.mp3')
                        print('game over,You lost')
                        
                        break
                    elif check_result(b)==-1:
                        print('game over,You won')
                        
                        break
                    elif check_result(b)==0:
                        #playsound('drawinomode3.mp3')
                        print('game over, match draw')
                        
                        break

                    if turn ==1:
                        print('computer"s chance')
                        
                        x=0
                        #This loop will run again if the user has choosen already filled position , otherwise break by running once'''
                        while x==0:
                            value=0
                            # These are the conditions for attacking move for the computer like the case of two x at 
                            # ...two positions of a row then the computer will move at the unfilled position
                            #Similarly if two positions of a column is filled by x then the computer will move at the unfilled position
                            if (b[0]+b[1]==2 or b[5]+b[8]==2 or b[4]+b[6]==2) and b[2]==0:
                                value=2
                            elif (b[1]+b[2]==2 or b[4]+b[8]==2 or b[3]+b[6]==2) and b[0]==0:
                                value=0
                            elif (b[0]+b[2]==2 or b[4]+b[7]==2) and b[1]==0:
                                value=1
                            elif (b[0]+b[6]==2 or b[4]+b[5]==2) and b[3]==0:
                                value=3
                            elif (b[0]+b[8]==2 or b[2]+b[6]==2 or b[3]+b[5]==2 or b[1]+b[7]==2) and b[4]==0:
                                value=4
                            elif (b[3]+b[4]==2 or b[2]+b[8]==2) and b[5]==0:
                                value=5
                            elif (b[0]+b[3]==2 or b[4]+b[2]==2 or b[7]+b[8]==2) and b[6]==0:
                                value=6
                            elif( b[4]+b[1]==2 or b[8]+b[6]==2) and b[7]==0:
                                value=7
                            elif (b[0]+b[4]==2 or b[2]+b[5]==2 or b[6]+b[7]==2) and b[8]==0:
                                value=8
                            else:
                                value=bestmove(b)
                            if b[value]==0:
                                print('computer choose ',value)
                                a[value]='x' # x will be inserted in list a
                                b[value]=1   # 1 will be inserted in list b
                                x=1
                    elif turn==-1:
                        print('O"s chance')
                        value=int(input())
                        if value>-1 and value<9:
                            if b[value]==0:
                                
                                a[value]='O' # o will be inserted in list a
                                b[value]=-1  #-1 will be inserted in list b
                            else:
                                #playsound('invalid.mp3')
                                print('you choose already filled place, please do again')
                                turn=turn*(-1)## Turn is being transferred from player to computer and vice versa
                        else :
                            #playsound('invalidinput.mp3')
                            print('Invalid  please do again')
                            turn=turn*(-1) ## Turn is being transferred from player to computer and vice versa
                    
                    turn=turn*(-1)  # Turn is being transferred from player to computer and vice versa
            
            break  #Break the loop if a valid input is taken by the user or the player

        else :
            print('Invalid Input, Choose again') #in case the user is giving an invalid input he will be asked again
            
    #playsound('exit.mp3')
    print("press 0 to exit")
    
    #playsound('playagain.mp3')
    print("press 1 to play again")
    #We are asking user if he wants to play again
    playnext=int(input())
    if playnext==0:
        break  #if the user dont want to play again then the loop will break
    elif playnext==1:
        pass #if the user wants to play again then the loop will run again
    else :
        print('invalid input, please do again')# in case the user is giving an invalid input he will be asked again