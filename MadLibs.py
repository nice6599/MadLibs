#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Program:MadLibs
# Author: nice6599
# License: GPL-3.0
# Date: Feb 2019 
# https://github.com/nice6599/MadLibs 



welcomeMessage = """
 _       __     __                             ______    
| |     / /__  / /________  ____ ___  ___     /_  __/___ 
| | /| / / _ \/ / ___/ __ \/ __ `__ \/ _ \     / / / __ \  
| |/ |/ /  __/ / /__/ /_/ / / / / / /  __/    / / / /_/ /
|__/|__/\___/_/\___/\____/_/ /_/ /_/\___/    /_/  \____/ 
                                                         
""" +"""
███╗   ███╗ █████╗ ██████╗     ██╗     ██╗██████╗ ███████╗
████╗ ████║██╔══██╗██╔══██╗    ██║     ██║██╔══██╗██╔════╝
██╔████╔██║███████║██║  ██║    ██║     ██║██████╔╝███████╗
██║╚██╔╝██║██╔══██║██║  ██║    ██║     ██║██╔══██╗╚════██║
██║ ╚═╝ ██║██║  ██║██████╔╝    ███████╗██║██████╔╝███████║
╚═╝     ╚═╝╚═╝  ╚═╝╚═════╝     ╚══════╝╚═╝╚═════╝ ╚══════╝
                                                          
""" 
# the reason for having a variable is so i can have the multi line text

print welcomeMessage
 # this prints the welcome message
raw_input("Press Enter to Start...")
# I am using raw input to have a press enter to start because 
# it is the easiest way to implement a press enter to start


while True: 

    # This is the loop that allows for the user to repeat and play again. 
    # At the end if the user types "n" to not play again the loop breaks.

    
    mad_text="" 
    # this defines a variable that holds the entire madlib
        
    madlib="" 
    # defines a variable that represents the madlib that should be used.
    #It is set to blank and gets set later.
    
    choice=0 
    # defines variable that represents user choice 
    
    play_again = '' 
    # defines play_agian which is what the user inputs at the very end
    
    replace = [] 
    # defines the variable that will hold the list of user entires
    # resets the users entries if they are playing again
    
    libs=[]
    # Defines the variable that will hold the prompts

    
    while True: 
        # this creates an infinite loop
        # it is used to make sure that the user chooses an avaliable choice 

        print "Type a number to select a Mad Lib \n \n","Choices: \n \n", "1. War\n","2. Television\n","3. Very Simple Test \n"
        # Prints intstructions on how to choose a madlib and lists the madlibs avaliable

        choice = int(raw_input("Choice: "))
         # asks user to input a choice
        
       
        if choice == 1:
            madlib = "War.txt"
            break
        if choice == 2:
            madlib= "Television.txt"
            break
        if choice == 3:
            madlib = "Very Simple Test.txt" 
            break
        # Depending on which number is entered the variable madlib will be set
        # and the loop will be broken. 
        # I don't think i have to explain this in more depth       


        print "Please enter one of the choices."
        # If the user puts in a number say 0
        # which is not a choice this line will print 
        
    mad_file = open(madlib, 'r')
    # this uses the file function to open a file which is specified by a variable 
    # that was defined previously. 
    # it set mad_file to be the file code and sets it to read only. 

    
    varAmnt = int(mad_file.readline())
    # this reads the first line of the file and gets the number which is there


    while varAmnt != 0:
        libs.append(mad_file.readline())
        varAmnt += -1
    # this loop runs varAmnt times and gets the next line each time
    # on the first run it gets the second line on the second run it gets the third
    # on the third run it gets the 4th and so forth
    # how the files are formatted is explained in the README.md file 
    # after this loop is finished running it will have created a list of all the prompts


    while len(replace) != len(libs):
        replace.append(raw_input(libs[len(replace)]))
    # this loop runs for the lenthg of libs which means it runs once for each prompt
    # i could have used a for function but I didnt
    # this loop does a raw_input with the propmt in raw_input being the prompt from before
    # when this loop is done running it will have created a list of the users inputs

    for line in mad_file :
        mad_text += line
    # this gets the remaining lines in the file which should be where the mad lib is
    # and adds them to a single string which makes the text easier to work with. 
        
    for i in range(len(libs)):
            mad_text = mad_text.replace('{'+str(i)+'}', replace[i])
    # this for loop is where the magic happens. 
    # it uses the str.replace function to replace the "fields" with the user inputs
    # it uses the for loop and the range function to iterate through the index of the user inputs
    # There is an example of this in the README.md file
    # originally i was thinking of using the str.format fucntion
    # but it wants to format the entire string at once and it didnt want to take my list of user inputs.
    
    
    print mad_text
    # this prints the final text with all the users inputs 


    while True: # this creates an infinite loop
        play_again = raw_input("Would you like to play again? (y/n): ")
    
        if play_again == "y" or play_again == "Y" or play_again == "n" or play_again =="N":
            break 
    # this while loop asks the user if they want to play again
    # when the user inputs any of the acceptable answers this loop breaks
    # the large loop is not broken here
    
    if play_again == "n" or play_again =="N":
        break
    # if the user entered "n" when they were asked if they wanted to play again 
    # this breaks the large loop which has most of the program inside of it.
