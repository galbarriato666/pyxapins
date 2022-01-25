"""Objectives
Familiarize the student with:

using the break statement in loops;
reflecting real-life situations in computer code.
Scenario
The break statement is used to exit/terminate a loop.

Design a program that uses a while loop and continuously asks the user to enter a word unless the user enters "chupacabra" as the secret exit word, in which case the message "You've successfully left the loop." should be printed to the screen, and the loop should terminate.

Don't print any of the words entered by the user. Use the concept of conditional execution and the break statement."""

secret="chupacabras"
word=input("Intro password ")

while True:    
    if word!=secret:
        word=input("Intro password ")
    else:
        break
print("Good job, you entered da systam")

#o más corto así, sin breaks ni nada: 

"""while word =! secret:
        word=input("Intro password ") 
print("Good job ...")"""