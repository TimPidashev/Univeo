import fractions
import statistics
import random
import cmath
import decimal
import numbers
import time
from termcolor import colored
from pyfiglet import Figlet

#ASCII LOGO
cool_logo = Figlet(font="graffiti")
print(colored(cool_logo.renderText("Univeo"), "magenta"))
time.sleep(.2)

#dont know why i did this...
logo = [
    " T",
    " Th",
    " The",
    " The u",
    " The ul",
    " The ult",
    " The ulti",
    " The ultim",
    " The ultima",
    " The ultimat",
    " The ultimate",
    " The ultimate T",
    " The ultimate Ty",
    " The ultimate Typ",
    " The ultimate Typi",
    " The ultimate Typin",
    " The ultimate Typing",
    " The ultimate Typing.",
    " The ultimate Typing.c",
    " The ultimate Typing.co",
    " The ultimate Typing.com",
    " The ultimate Typing.com g",
    " The ultimate Typing.com gr",
    " The ultimate Typing.com gra",
    " The ultimate Typing.com grad",
    " The ultimate Typing.com gradi",
    " The ultimate Typing.com gradin",
    " The ultimate Typing.com grading",
    " The ultimate Typing.com grading c",
    " The ultimate Typing.com grading ca",
    " The ultimate Typing.com grading cal",
    " The ultimate Typing.com grading calc",
    " The ultimate Typing.com grading calcu",
    " The ultimate Typing.com grading calcul",
    " The ultimate Typing.com grading calcula",
    " The ultimate Typing.com grading calculat",
    " The ultimate Typing.com grading calculato",
    " The ultimate Typing.com grading calculator",
    " The ultimate Typing.com grading calculator!"
]
i = 0

while True:
    print(logo[i % len(logo)], end="\r")
    time.sleep(.1)
    i += 1
    if i == 39:
        break
