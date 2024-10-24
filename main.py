# Programmer:  Theresa DeJacimo
# Course:  CS151, Dr. Zaleem
# Due Date: 10/23/24
# Programming Assignment:  2
# Problem Statement: There is a pile of sticks on the table, and players alternate turns taking 1-3 sticks.
# The player to take the last stick loses.
# Data In: Player names and sticks taken
# Data Out: Number of times each player loses the game
# Credits: In Class and YouTube video



#Welcome to the Stick Game!


print('Welcome to the stick game.The rules are as follows: \n'
      '1.The game starts with some number of sticks on the table (between 10 and 100, chosen by the user) \n'
      '2.Three players take turns choosing how many sticks to take.Player 1 will always be the computer \n'
      '3.On each player’s turn they must take either 1, 2, or 3 sticks.\n'
      '4.The player to take the last stick loses.  Please enter your names in the player 2 and player 3 spaces')

import random
def main():
    game = str(input('Type "stop" to end game'))
#Assigning players of the game
    player_one = 'Computer'
    player_two = str(input('Enter player two name:'))
    player_three = str(input('Enter player three name:'))
    print('Player 1:', player_one, 'Player 2:', player_two, 'Player 3:', player_three)
    player_one_losses = 0
    player_two_losses = 0
    player_three_losses = 0
#Asking for number of sticks that current game is going to be played with
    while game != 'stop':
        number_of_sticks = input('Player 1 or Player 2, pick a number 10-100:')

#Making sure number of sticks is a number 10-100
        while not number_of_sticks.isdigit():
            print('Not a valid input, please enter a number 10-100')
            number_of_sticks = input('Player 1 or Player 2, pick a number 10-100:')

        number_of_sticks=int(number_of_sticks)

        while 100 < number_of_sticks or number_of_sticks < 10:
            print('Number or string is not allowed. Please choose a number 10-100')
            number_of_sticks = int(input('Player 1 or Player 2, pick a number 10-100:'))
        print(number_of_sticks)
#Computers' turn
        while number_of_sticks > 0:
            player_one_turn = random.randint(1,3)
            print(player_one_turn)
            number_of_sticks = number_of_sticks - player_one_turn
            if number_of_sticks <= 0:
                print('Computer lost')
                player_one_losses += 1
                break
#Player 2 turn
            player_two_turn = int(input('Pick up 1,2, or 3 sticks:'))
            while player_two_turn != 1 and player_two_turn != 2 and player_two_turn != 3:
                print('Not an acceptable turn value, please input 1, 2, or 3.')
                player_two_turn = int(input('Pick up 1,2, or 3 sticks:'))
            number_of_sticks = number_of_sticks - player_two_turn
            if number_of_sticks <= 0:
                print('Player two lost')
                player_two_losses += 1
                break
#Player 3 turn
            player_three_turn = int(input('Pick up 1,2, or 3 sticks:'))
            number_of_sticks = number_of_sticks - player_three_turn
            if number_of_sticks <= 0:
                    print('Player three lost')
                    player_three_losses += 1
                    break
#End of game
        game = str(input('Type "stop" to end game'))
    print('Computer losses:', player_one_losses,'Player two losses:', player_two_losses, 'Player three losses:', player_three_losses)

    print('Thank you for playing our game!')
main()








