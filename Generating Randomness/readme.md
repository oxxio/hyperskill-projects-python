Description
In the final stage, we will gather all our components to construct a game where you will try to beat the system created by your hands. Initially, the player has a virtual balance of $1000. Every time the computer guesses a symbol correctly, the player loses one dollar. Every time the system is wrong, the player gets one dollar.

Objectives
In this final stage, your program should:

Get and preprocess user input just like in stage 1.
Learn user patterns by collecting triad statistics like in stage 2.
Ask the user to enter test strings or type enough to exit the game. Each test string must be preprocessed (in order to leave only "0" and "1" symbols). After that, you should launch the prediction algorithm and calculate the number of correctly guessed symbols. After each iteration, you should show the player's balance with the message Your balance is now $X, where X is the player's virtual balance.
It would be great if you kept updating the system by allowing it to learn from the test data as well. However, this update should happen only after the prediction and the verification stages are done: let's be honest with the user.
Finish the game with the words Game over!.
Example
The greater-than symbol followed by a space (> ) represents the user input. Note that it's not part of the input.

Please give AI some data to learn...
The current data length is 0, 100 symbols left
Print a random string containing 0 or 1:

> 010100100101010101000010001010101010100100100101001
The current data length is 63, 37 symbols left
Print a random string containing 0 or 1:

> 011010001011111100101010100011001010101010010001001010010011

Final data string:
010100100101010101000010001010101010100100100101001011010001011111100101010100011001010101010010001001010010011

You have $1000. Every time the system successfully predicts your next press, you lose $1.
Otherwise, you earn $1. Print "enough" to leave the game. Let's go!

Print a random string containing 0 or 1:
> 0111001001
prediction:
1000101011

Computer guessed right 4 out of 7 symbols (57.14 %)
Your balance is now $999

Print a random string containing 0 or 1:
> some wrong input

Print a random string containing 0 or 1:
> 0101001001
prediction:
0001011011

Computer guessed right 5 out of 7 symbols (71.43 %)
Your balance is now $996

Print a random string containing 0 or 1:
> enough
Game over!
