"""
Umar Mohammad Riaz & Emmanuel Manzanilla
04/05/2022
ASIXc 1B

Writes to Log file
"""

import os
import sys
from datetime import datetime


def currentDateTime():  # Gets the current datetime
    now = datetime.now()
    currentDateTime = now.strftime("%d/%m/%Y %H:%M:%S:%f")[:-3]
    return currentDateTime


def log(message):   # Writes the error messages
    if not os.path.exists("log"):
        os.mkdir("log")
    with open("log/error.log", "a") as log:
        log.write(f"{currentDateTime()} - {message}\n")


def personalizedException(exception):   # In case of other error it makes a short message
    exception_type, exception_object, exception_traceback = sys.exc_info()
    filename = os.path.split(exception_traceback.tb_frame.f_code.co_filename)[1]
    lineNumber = exception_traceback.tb_lineno
    error = f"{type(exception).__name__} at line {lineNumber} of {filename}: {exception}"
    return error

