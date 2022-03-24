# Two squares game.
# Two player each one of them have a ratangle use it to hide two
# number from the same column or row .  
# Author:Tawfik Mohamed Khalil.
# Date:24-2-2022
# version:1.0
matrix=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]] 
# def check numbers is aleardy chosen .
def check(p):
      for row in matrix:                        
            for i in row :
                  if i==p:
                     return True    
# def check_the_winner form player1 or player2.                                           
def check_the_winner():
    list=[]
    isWin = True
    for row in matrix: 
        for i in row:
                if i !="   X":
                    list.append(i)     
#loop on the list  we made to add the remainder of numbers to check
# if they available to or not.    
    for i in range (len(list)):
            for j in range (i+1,len(list)):

                  if  (list[i]+1 == list[j] and (list[i]!=4 and list[j]!=5)and 
                       (list[i]!=8 and list[j]!=9)and (list[i]!=12 and list[j]!=13))or list[i]+4 == list[j]:
                              isWin = False
    return isWin
check_the_winner() 

#def check_the_tie if all matrix element replaced by "x".
def check_the_tie():
    list=[]
    isWin = False
    for row in matrix: 
        for i in row:
                if i !="   X":
                    list.append(i)
# if all the board full of  "x"                    
    if len(list)==0:
        isWin=True    
    return isWin 

check_the_tie() 

# def play 
def play():
      player = 1

      while True :
            # print the board to start play.
            x = '\n'.join([''.join(['{:4}'.format(i) for i in row]) for row in matrix])
            print(x)
            # input should be like that 4,3 between every number comma.     
            theplayer=list(map(int,input(f"player{player},enter only two number from 1 to 16 : ").strip().split(",")))[:2]
            #check if the two number is exist or not.
            wrong=False
            while not wrong:
                  if (theplayer[0]+1==theplayer[1] and theplayer[0]!=4 and theplayer[1]!=5 and theplayer[0]!=8 and theplayer[1]!=9 and theplayer[0]!=12 
                  and theplayer[1]!=13) or(theplayer[0]+4==theplayer[1])or(theplayer[0]==theplayer[1]+4)or(theplayer[0]==theplayer[1]-1 
                  and theplayer[0]!=4 and theplayer[1]!=5 and theplayer[0]!=8 and theplayer[1]!=9 and theplayer[0]!=12 and theplayer[1]!=13):
                        wrong=True
                  else:
                        print("wrong play\n")
                        theplayer=list(map(int,input(f"please enter another two number : ").strip().split(",")))[:2] 
            #check if he number is exist or hidden by "x".
            valiad=False     
            while not valiad:
                  if check(theplayer[0]) and check(theplayer[1]):
                        valiad=True
                  else:
                        print("number is aleardy chosen  \n")
                        theplayer=list(map(int,input("please enter another two number : ").strip().split(",")))[:2]  
                        continue 

                  for row in matrix:
                  # replace the play of the player1 with "x". 
                        if theplayer[0] in row:
                              row[row.index(theplayer[0])]=str("   X")
                        if theplayer[1] in row:
                              row[row.index(theplayer[1])]=str("   X")   
     
                  x = '\n'.join([''.join(['{:4}'.format(i) for i in row]) for row in matrix])
                  print(x)
            if check_the_tie():
                  print("No one win")            
                  break                        
            if check_the_winner():
                  print(f"player {player} win ")            
                  break
            print("*"*20)  
            # switch between player 1 & 2. 
            if player == 1:
                  player = 2
            else:
                  player = 1
                
play()


 

