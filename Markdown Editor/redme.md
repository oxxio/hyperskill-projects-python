Description
By this moment, our program can recognize some of the formatters and special commands, it can also print the results and exit. We need to implement yet another very useful feature — the ability to save the text to a file.

Objectives
Modify your done function that was implemented in the second stage. Apart from exiting the program, it should save the final result of a session to a file, let's call it output.md. Create this file in the program directory. If it already exists, overwrite this file. The file should include the result of the last session.

Examples
The greater-than symbol followed by a space (> ) represents the user input. Note that it's not part of the input.

Example 1:

	
Choose a formatter: > header
Level: > 1
Text: > Hello World!
# Hello World!

Choose a formatter: > plain
Text: > Lorem ipsum dolor sit amet, consectetur adipiscing elit
# Hello World!
Lorem ipsum dolor sit amet, consectetur adipiscing elit
Choose a formatter: > line-break
# Hello World!
Lorem ipsum dolor sit amet, consectetur adipiscing elit

Choose a formatter: > ordered-list
Number of rows: > 3
Row #1: > dolor
Row #2: > sit
Row #3: > amet
# Hello World!
Lorem ipsum dolor sit amet, consectetur adipiscing elit
1. dolor
2. sit
3. amet

Choose a formatter: > !done
