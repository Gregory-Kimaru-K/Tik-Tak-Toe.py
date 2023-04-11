game_list = [0, 1, 2]
def display_game(games_list):
    print('Here is the current list')
    print(games_list)

display_game(game_list)

def position_choice():
    global choice
    choice= 'Wrong'
      
    while choice not in ['0','1','2']:
        choice = input("Pick a position (0,1,2): ")
        
        if choice not in ['0','1','2']:
            print("sorry, invalid choice! ")
            
    return int(choice)
                        
position_choice()


def replacement_choice(game_list,position):
    user_placement= input('type a string to place in position: ')

    
    game_list[position]= user_placement
    
    return game_list

replacement_choice(game_list,1)


def gameon_choice():
    global choice
    choice= 'Wrong'
      
    while choice not in ['Y', 'N']:
        choice = input("Please pick the option of (Y or N): ")
        
        if choice not in ['Y','N']:
            print("sorry, I dont understand. Plese pick Y or N ")
            
        if choice== 'Y':
            return True
        else:
            return False
            
                        

gameon_choice()

GAME HEAD

game_on= True
game_list= [0,1,2]

while game_on: 
    display_game(game_list)
    
    position = position_choice()
    
    game_list = replacement_choice(game_list,position)
    
    game_on =gameon_choice()

    display_game(game_list)