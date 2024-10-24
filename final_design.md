# Final Design Document


# Algorithm:
#### Output "Welcome to the stick game.The rules are as follows:
      1.The game starts with some number of sticks on the table between 10 and 100, chosen by the user
      2.Three players take turns choosing how many sticks to take.Player 1 will always be the computer
      3.On each player’s turn they must take either 1, 2, or 3 sticks
      4.The player to take the last stick loses.  Please enter your names in the player 2 and player 3 spaces
#### 1) import random
- Name: main
- Parameters: none
- Return: how many times each player lost 
#### 2) Make variable 'game' to continue or stop game 
#### 3) if game does not equal "stop":
1.  set player one variable equal to 'Computer'
2. create player two and player two variables
3. prompt players to enter their names in player one and player two variables
4. output player names
5. make a losses variable for each player and set equal to zero 
6. while game does not equal 'stop':
   7. prompt user to input a number of sticks between 10 and 100
   8. if number of sticks is not an integer and not between 10 and 100:
      9. output 'Number or string is not allowed. Please choose a number 10-100'
      10. prompt players to enter a number 10-10
   11. print number of sticks
   12. while number of sticks is greater than 0:
       13. computer picks up a random amount of sticks 1-3
       14. subtract computer turn from total number of sticks and make that the new total number of sticks
       14. player two turn
       15. while player two input is not 1-3:
           16. output 'Not an acceptable turn value, please input 1, 2, or 3.'
           17. prompt player two to enter a number 1-3
       15. subtract player two turn from total number of sticks and make that the new total number of sticks
       16. player three turn 
       17. while player three input is not 1-3:
           16. output 'Not an acceptable turn value, please input 1, 2, or 3.'
           17. prompt player three to enter a number 1-3
       18) subtract player three turn from total number of sticks and make that the new total number of sticks
   13) add one to players count who picks up the last stick
   14) store value in player's losses variables 
#### 15) output 'Computer losses:, player_one_losses,Player two losses:, player_two_losses, 'Player three losses:', player_three_losses)
#### 16) output 'Thank you for playing our game!'
#### 17) call main function


