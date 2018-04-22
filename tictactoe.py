#Framework combination of scratch, overflow,github, python.org
import random
import sys

user = '' #User value
comp = '' #Computer value
array = ['','','','','','','','','',''] #Array to hold the X/O value
null = '' #Null representing no input

def design(): #Table design with format 1-9
    print("1 | 2 | 3")         
    print("----------")
    print("4 | 5 | 6")           
    print("-----------")
    print("7 | 8 | 9")
    print("These are the number positions")
def start(): #Select whether to begin the game or exit
        ans = input("Ready to begin? Y or N:")
        if ans == 'y' or ans == 'Y': #Continues the game with a True value
            return 1
        elif ans == 'n' or ans == 'N': #Quits the game 
            quit()
        else:
            print("Invalid choice")
            
def side_select(user, comp): #Select X or O, then for the user and comp selection to uppercase letters
    user = input("What team you want to be? X or O: ")
    while user not in ('x','X','o','O'):
        print ("Invalid Choice!")
        user = input("What team you want to be? X or O: ")
    if user == 'x' or user == 'X':
        comp = 'o'
    else:
        comp = 'x'
    return user.upper(), comp.upper() #Shows values as uppercase on the board 

            
def table(a): #Draw the table (taken from overflow)
    
    print("\n\t",a[1],"|",a[2],"|",a[3])
    print("\t", "--------")
    print("\n\t",a[4],"|",a[5],"|",a[6])
    print("\t", "--------")
    print("\n\t",a[7],"|",a[8],"|",a[9], "\n")
    
def user_select(user, array): 
    a = input("Where do you want to move, 1-9: ") #Decide between 1-9 for a move
    while True:
        if a not in ('1','2','3','4','5','6','7','8','9'): #Checks for the number
            print("Invalid")
            a = input("Where do you want to move, 1-9:")
        elif array[int(a)] != null:
            a = input("Where do you want to move, 1-9: ") #If number already taken reask
        else:
            return int(a)
 
def comp_select(user, comp, array): #Computer selection
    tmp = [] #Empty array
    for i in range(0,9): #Computer can choose between 1-9
        if array[i] == null:
            tmp.append(i) #Adds value to table
    
    for i in tmp:
        array[i] = comp
        if process(user, comp, array) is 0: #If false i.e. number is taken or invalid return null and redo

            return i
        array[i] = null

    for i in tmp:
        array[i] = user
        if process(user, comp, array) is 1: #If true replace the number now the same as the user

            return i #Return such value to the table
        array[i] = null
    if len(tmp) !=0:
        
        return int(random.choice(tmp)) #Return random selection
    else:
        return None
def process(user, comp, array):
    combination = ((1,2,3),(4,5,6),(7,8,9),(1,4,7),(2,5,8),(3,6,9),(1,5,9),(3,5,7)) #Possible combinations to win (combinations  taken in parts from overflow)
    for i in combination:
        if array[i[0]] == array[i[1]] == array[i[2]] != null: #Checks every turn for combination on the table through the array
            winner = array[i[0]] #The winning value (process from github (determining a winner))
            if winner == user:
                return 1 #User win
            elif winner == comp:
                return 0 #Comp win
            if null not in array: 
                return ' ' #Returns empty string to relay a tie 
    if null not in array: 
        return ' '    #Returns the empty string
    return None


def play(user, comp, array): #Play the game
    while process(user, comp, array) is None: #While there are still no winning combinations allow selection
        select = user_select(user, array) #User selection of numbers from array
        array[int(select)] = user #Enter the X or O into the selected number
        table(array) #Reprint the table
        if process(user, comp, array) != None:
            break #Break for a computer turn when the selection is made
            
        else:
            pass
        comp_turn = comp_select(user, comp, array) #Computer operated random generation 
        array[int(comp_turn)] = comp
        table(array) #Reprint the table
    tmp = process(user, comp, array) #Deciding a winner via True and False values (idea from github)
    if tmp == 1:
        print("You won!") #True value is the user
    elif tmp == 0:
        print("Computer won!") #False value is the computer
    else:
        print("It's a tie") #Tie otherwise

def main(user, comp, array):
    design() #Calls for the tabe layout
    a = side_select(user, comp) #Selects the X and O value, stores the value in value a (the arrays)
    user = a[0] #Holds user combinations
    comp = a[1] #Holds computer combinations
    begin = start()
    if begin == 1: #If start is true via the Y or y draw the table and play
        table(array) #Draw table
        play(user, comp, array) #Play  
    else:
        pass

main(user,comp, array)
input("Press any key to exit") #input from overflow
quit()

if __name__ == "__main__": main() 