
theboard={"1":" ","2":" ","3":" ",
         "4":" ","5":" ","6":" ",
         "7":" ","8":" ","9":" "}
print("The Grid")
print("1"+"|"+"2"+"|"+"3")
print('-+-+-')
print("4"+"|"+"5"+"|"+"6")
print('-+-+-')
print("7"+"|"+"8"+"|"+"9")

def board():
    print("\n\nThe Board")
    #print(theboard)
    print(theboard['1']+"|"+theboard['2']+"|"+theboard['3'])
    print('-+-+-')
    print(theboard['4']+"|"+theboard['5']+"|"+theboard['6'])
    print('-+-+-')
    print(theboard['7']+"|"+theboard['8']+"|"+theboard['9'])


def checkwin():
    if theboard['1']==theboard['2']==theboard['3']!=' ':
        print(turn+" won the game!")
        return('true')
    
    elif theboard['4']==theboard['5']==theboard['6']!=' ':
        print(turn+" won the game!")
        return('true')
    elif theboard['7']==theboard['8']==theboard['9']!=' ':
        print(turn+" won the game!")
        return('true')
    elif theboard['1']==theboard['5']==theboard['9']!=' ':
        print(turn+" won the game!")
        return('true')
    elif theboard['3']==theboard['5']==theboard['7']!=' ':
        print(turn+" won the game!")
        return('true')
   
    else:
        for i in range(9):
            if theboard[i]==' ':
                return(false)
            else:
                print("Its a tie")
                return('true')
        break
            
    
turn = "x"


    
move = input("Do your turn "+turn+" specify your position on the grid")

print(move)
if theboard[move]==' ':
    theboard[move] = turn;
    board()

    if checkwin()=='true':
        break

    if turn=='x':
        turn='o'
    else: 
        turn='x'

        
        
