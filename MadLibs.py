#!/usr/bin/env python
# -*- coding: utf-8 -*-
from termcolor import colored,cprint

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

while True: 

    # This is the loop that allows for the user to repeat and play again. 
    # At the end if the user types "n" to not play again the loop breaks.
    
    
    mad_text="" # this defines a variable that holds the entire madlib
        
    madlib="" # defines a variable that represents the madlib that should be used. It is set to blank and gets set later.
    
    choice=0 # defines variable that represents user choice is the choice 
    
    play_again = ''
    
    replace = [] # resets the users entries
    
    libs=[]

    
    while True: 
        print "Type a number to select a Mad Lib \n \n","Choices: \n \n", "1. War\n","2. Television\n","3. Very Simple Test \n"

        choice = int(raw_input("Choice: "))
        if choice == 1:
            madlib = "War.txt"
            break
        if choice == 2:
            madlib= "Television.txt"
            break
        if choice == 3:
            madlib = "Very Simple Test.txt" 
            break
        print "Please enter one of the choices."
        
    mad_file = open(madlib, 'r')
    
    varAmnt = int(mad_file.readline())
    while varAmnt != 0:
        libs.append(mad_file.readline())
        varAmnt += -1
        
    while len(replace) != len(libs):
        replace.append(raw_input(libs[len(replace)]))
            
    for line in mad_file :
        mad_text += line
        
    for i in range(len(libs)):
            mad_text = mad_text.replace('{'+str(i)+'}', replace[i])
    print mad_text
    
    while True:
        play_again = raw_input("Would you like to play again? (y/n): ")
    
        if play_again == "y" or play_again == "Y" or play_again == "n" or play_again =="N":
            break 
    
    
    if play_again == "n" or play_again =="N":
        break

    
    
    
    




