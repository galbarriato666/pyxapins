"""
Umar Mohammad Riaz
04/05/2022
ASIXc 1B

Runs all functions and prints the result
"""
from crazyWords import *



try:
    getDataFromFiles('jojo')
except Exception as e:
    log(personalizedException(e))

