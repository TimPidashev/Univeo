import time
import os
import waste_of_time
from termcolor import colored
from pyfiglet import Figlet
os.system('color')

#ASCII LOGO
cool_logo = Figlet(font="graffiti")
print(colored(cool_logo.renderText("Univeo!"), "magenta"))
time.sleep(.2)

#loop variable
still_grading = True

#getting user input
while still_grading:
    stars_total = input(colored("Number of stars assignment has: ", "yellow"))
    stars_achieved = input(colored("Number of stars achieved: ", "yellow"))
    avg_acc = input(colored("AVG typing accuracy: ", "cyan"))

    #calulating percent
    stars_achieved = float(stars_achieved)
    stars_total = float(stars_total)
    stars_percentage = '{0:.2f}'.format((stars_achieved / stars_total * 100))

    #getting an avg between the stars grade and avg accuracy
    def average(stars_percentage, avg_acc):
        return (stars_percentage + avg_acc) / 2.0

    avg = average(float(stars_percentage), float(avg_acc))

    #literally just doing checks to get grade specific colors
    if avg > 90.0:
        print(colored(f"{avg}", "green"))
        print(colored("---------------------------------------", "magenta"))

    elif avg < 90.0 and avg > 50.0:
        print(colored(f"{avg}", "yellow"))
        print(colored("---------------------------------------", "magenta"))

    elif avg < 50.0:
        print(colored(f"{avg}", "red"))
        print(colored("---------------------------------------", "magenta"))

    else:
        print(colored("A user input error has occured, restart program to continue grading!", "red"))
        break
