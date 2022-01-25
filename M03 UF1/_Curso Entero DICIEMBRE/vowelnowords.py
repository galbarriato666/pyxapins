"""Scenario
The continue statement is used to skip the current block and move ahead to the next iteration, without executing the statements inside the loop.

It can be used with both the while and for loops.

Your task here is very special: you must design a vowel eater! Write a program that uses:

a for loop;
the concept of conditional execution (if-elif-else)
the continue statement.
Your program must:

ask the user to enter a word;
use user_word = user_word.upper() to convert the word entered by the user to upper case;
 we'll talk about the so-called string methods and the upper() method very soon - don't worry;
use conditional execution and the continue statement to "eat" the following vowels A, E, I, O, U from the inputted word;
print the uneaten letters to the screen, each one of them on a separate line.
Test your program with the data we've provided for you."""

word = input("Enter a word ")
word = word.upper()
word_without_vowels = ""

for a in word:
    if a == "A":
        continue
    elif a == "E":
        continue
    elif a == "I":
        continue
    elif a == "O":
        continue
    elif a == "U":
        continue    
    else:
        word_without_vowels = word_without_vowels+a # Importantisimo! De esta manera variable + iteración se van añadiendo una tras otra en la variable vacia del principio

print(word_without_vowels)

#alternativas to locas:   
#  else:
#         print(letter,end=wordWithoutVovels)
# y tambien sin siquiera usar la variable:
#Print (letter, end ="")