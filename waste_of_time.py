import time

#dont know why i did this...(And i felt like manually writing this out instead of string slicing for some reason...)
logo = [
    " T",
    " Th",
    " The",
    " The b",
    " The be",
    " The best",
    " The best T",
    " The best Ty",
    " The best Typ",
    " The best Typi",
    " The best Typin",
    " The best Typing",
    " The best Typing.",
    " The best Typing.c",
    " The best Typing.co",
    " The best Typing.com",
    " The best Typing.com g",
    " The best Typing.com gr",
    " The best Typing.com gra",
    " The best Typing.com grad",
    " The best Typing.com gradi",
    " The best Typing.com gradin",
    " The best Typing.com grading",
    " The best Typing.com grading c",
    " The best Typing.com grading ca",
    " The best Typing.com grading cal",
    " The best Typing.com grading calc",
    " The best Typing.com grading calcu",
    " The best Typing.com grading calcul",
    " The best Typing.com grading calcula",
    " The best Typing.com grading calculat",
    " The best Typing.com grading calculato",
    " The best Typing.com grading calculator"
]
i = 0

while True:
    print(logo[i % len(logo)], end="\r")
    time.sleep(.1)
    i += 1
    if i == 39:
        break
