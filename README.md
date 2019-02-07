# MadLibs
A phrasal template word game written in python. Based on the game Mad Libs


## How to play 
 1. Download all the packages
 2. make sure its all in the same directory 
 3. run the python file in whatever ide or command line you wish
 4. follow the rest of the instructions in the program 
 5. Have Fun!!
 
 ## How the MadLibs files work
 
 ## Prompts / Word Types 
 Prompts/Word types are the phrases the program prints when asking for user input. An example of this is *Proper Noun*. It is a prompt that prompts the user to input a proper noun.
 
 
 ### Rules about prompts
 1. The prompts should be listed in order they appear in the text.
 2. The total number of prompts must be put the top of the file. 
 3. There cannot be any lines between the start of the file, the number, or the induvidiual prompts.
 4. You can type whatever you want as long as each prompt is on a separate line.

 
 If these rules are not followed the program will not work correctly
 
 You can have, and it is reccomended that you have a few blank lines between the prompts and the text of the Mad Lib.
 
 
 
 __Correct:__
 ```
 4
 Noun
 Noun
 Proper Noun
 Adjective
 
 Text
 ```
 __Incorrect:__
 ```
 
 4
 Noun
 
 Noun
 
 Proper Noun
 
 Adjective  
 
 Text
 ```
 
 ## Mad Lib Text
 The Mad Lib text is quite simple. For each field you want populated, use `{i}`. where `i` is the index number of the feild.
 
 Example:
 ```
4
Name
Pronoun
Occupation
Noun

{0} is a {2} {1} uses GitHub for his {3}
```
This file in action looks like this:
```
Press Enter to Start...
Type a number to select a Mad Lib 
 
Choices: 
 
1. War
2. Television
3. Very Simple Test 

Choice: 3
Name
Sam
Pronoun
he
Occupation
software engineer
Noun
version control 

Sam is a software engineer he uses GitHub for his version control
Would you like to play again? (y/n): n
TerminalPrompt:~ user$ 
``` 

 
 
 
 
 
