# Annie Kuo

import random as r

def point_gained(human_action, computer_action):
    """ (str, str) -> str
    
    The function takes two strings as arguments ('throw', 'dodge', or 'restock')
    and returns which player ('human' or 'computer') has gained a point.
    
    >>> point_gained('throw', 'dodge')
    ''
    >>> point_gained('throw', 'restock')
    'human'
    >>> point_gained('throw','throw')
    'human and computer'
    >>> point_gained('restock', 'restock')
    ''
    >>> point_gained('restock', 'throw')
    'computer'
    """
    # Determine and return who gets the point
    if human_action == 'throw' and computer_action == 'throw':
        return 'human and computer'
    
    elif human_action == 'throw' and computer_action == 'restock':
        return 'human'
    
    elif computer_action == 'throw' and human_action == 'restock':
        return 'computer'
    
    else:
        return ''
    

def get_computer_action(num_player_balls, num_opponent_balls):
    """ (int, int) -> str
    
    The function takes two integers as input
    each representing the number of balls in each player's possession
    Returns the string corresponding to the action ('throw', 'dodge', or 'restock')
    
    >>> r.seed(5)
    >>> get_computer_action(2, 0)
    'dodge'
    >>> get_computer_action(3, 2)
    'dodge'
    >>> get_computer_action(0,3) #random_int = 20
    'dodge'
    >>> get_computer_action(1,0) #random_int = 9
    'restock'
    >>> get_computer_action(1,1) #random_int = 24
    'restock'
    >>> get_computer_action(1,1) #random_int = 12
    'dodge'
    >>> get_computer_action(1,1) #random_int = 26
    'restock'
    """
    # Determine the computer's action based on the number of balls
    
    # If the human player has picked at least 2 balls, the computer dodges
    if num_player_balls >= 2:
        return 'dodge'    
    
    # If the human player has not picked 2 balls yet
    else:
        random_int= r.randint(1,30)
        
        if (num_opponent_balls == 0 or num_opponent_balls == 3) and random_int > 15:
            return 'dodge'
        elif (num_opponent_balls == 0 and random_int <= 15):
            return 'restock'
        elif (num_opponent_balls == 3 and random_int <= 15):
            return 'throw'
        elif (num_opponent_balls == 1 or num_opponent_balls == 2):
            if random_int <= 10:
                return 'throw'
            elif random_int <= 20:
                return 'dodge'
            else:
                return 'restock'
    
    
    
    
def get_human_action(num_player_balls, num_opponent_balls):
    """ (int, int) -> str
    
    The function takes two integers as input, each representing the number of balls in each player's possession
    The function asks and returns the user's input.
    If the user's input is invalid, the user is asked to enter another input
    
    >>> get_human_action(3,0)
    You now have 3 ball(s), and your opponent has 0 ball(s).
    Which action do you want to take (throw, dodge, or restock)? throw
    'throw'
    >>> get_human_action(2,3)
    You now have 2 ball(s), and your opponent has 3 ball(s).
    Which action do you want to take (throw, dodge, or restock)? dodge
    'dodge'
    >>> get_human_action(0,1)
    You now have 0 ball(s), and your opponent has 1 ball(s).
    Which action do you want to take (throw, dodge, or restock)? throw
    You do not have any ball to do so. Please choose again: dodge
    'dodge'
    >>> get_human_action(3,3)
    You now have 3 ball(s), and your opponent has 3 ball(s).
    Which action do you want to take (throw, dodge, or restock)? hello
    This is not a valid option. Please choose again: restock
    Sorry, you have reached the max number of balls. Please choose again: throw
    'throw'
    """
    # Display to the user the number of balls they and their opponent currently have
    print("You now have", num_player_balls, "ball(s), and your opponent has", num_opponent_balls, "ball(s).")
    
    # Retrieve the user's input
    human_action = input("Which action do you want to take (throw, dodge, or restock)? ")
    
    # Check for input validation
    is_an_option= (human_action != 'throw') and (human_action != 'dodge') and (human_action != 'restock')
    enough_balls= human_action == 'throw' and num_player_balls == 0
    max_balls= human_action == 'restock' and num_player_balls == 3
    
    # Ask for another user input as long as the input is invalid and display the according message
    while is_an_option or enough_balls or max_balls:
        if is_an_option:
            human_action = input("This is not a valid option. Please choose again: ")
            
        elif enough_balls:
            human_action = input("You do not have any ball to do so. Please choose again: ")
            
        elif max_balls:
            human_action = input("Sorry, you have reached the max number of balls. Please choose again: ")
            
        # Recheck the input validation
        is_an_option= (human_action != 'throw') and (human_action != 'dodge') and (human_action != 'restock')
        enough_balls= human_action == 'throw' and num_player_balls == 0
        max_balls= human_action == 'restock' and num_player_balls == 3
        
    return human_action



def play_game():
    """ () -> NoneType
    
    The function calls other functions as necessary to play a game of dodgeball
    until 5 points have been scored
    It prints the necessary messages following the game's development
    
    """
    # Welcome the user
    print("Welcome to this game of dodgeball. First to score 5 points wins! \n")
    
    # Initialize variables
    human_balls = 0
    computer_balls = 0
    human_points = 0
    computer_points = 0
    
    # Iterate until one of the players get 5 points
    
    while human_points <5 and computer_points <5:
        
        # Retrieve action from the human player
        human_action = get_human_action(human_balls, computer_balls)
        if human_action == 'restock':
            human_balls += 1
        elif human_action == 'throw':
            human_balls -= 1
        
        # Retrieve action from the computer
        computer_action = get_computer_action(human_balls, computer_balls)
        if computer_action == 'restock':
            computer_balls += 1
        elif computer_action == 'throw':
            computer_balls -= 1
            
        # Display both players' actions
        print("You've decided to " + human_action + ", and your opponent has decided to " + computer_action + ".")
        
        # Determine who gets the point
        point = point_gained(human_action, computer_action)
        
        # Display the scoreboard
        if 'human' in point:
            human_points += 1
            print("You got a point! You now have", human_points, "point(s).")
            
        if 'computer' in point:
            computer_points += 1
            print("Your opponent got a point. It now has", computer_points, "point(s).")
        
        if point == "":
            print("Neither of you got a point.")
        
        print("")
    
    # Announce winner
    if human_points == 5 and computer_points == 5:
        print("\n It's a tie!")
    elif human_points == 5:
        print("\nCongrats! You have won!")
    else:
        print("\nSorry! You have lost the game of dodgeball.")
    