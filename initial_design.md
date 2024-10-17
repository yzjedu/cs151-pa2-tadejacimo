# Initial Design Document
#### 

# Algorithm:
#### 1) State the name of the game to the players and with the basic concept through comments
#### 2) Assign player 1 to be the computer
#### 3) Have other two users input their names next to variables player_2 and player_3
#### 4) Make a while loop asking each player to pick 1-3 sticks 
#### 5) If  any player inputs for number of sticks less than 1 or greater than 3: 
1.  output "input a number 1-3"
#### 6) Output the name of the player who picks up the last stick and assign it to the variable you_lose
#### 7) To keep track of number of times each player loses make a string integer that adds each time the game is played, 
##### (this could possibly be done with a function?)
#### 8) Once output of the player who loses the game, ask the users if they want to play again
#### 9) Create a variable for the response to the question 'Do you want to play again?' 
#### 10) if answer is equal to yes:
1. output 'Okay get ready to play again' and stay in loop
2. otherwise output 'Thanks for playing!' and the amount of games each player lost, and exit loop 
#### 10) Once players decide to end the game and not play again output each player with the amount of times they lost next to their name
