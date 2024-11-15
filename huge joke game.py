


valid_answers = ['k', 'ok', 'sure', 'why not', 'yes', 'y', 'yeah', 'yep', 'yup', 'ye']



answer = input("do you want to hear a joke?    ")

if answer in valid_answers:
    answer = input("Which joke do you want to hear first? (a/b/c/d)     ")

else:
    answer2 = input("want to hear a riddle?   ")
    
a = '''Do you know what has four legs and cant move?
            A chair!'''

b = '''He said ,"Aren't Can't Shouldn't wouldn't" use it to solve the problem '''


c = '''Why don't scientists trust atoms? Because they make up everything!'''


d = '''Why did the chicken cross the road?
            To get to the other side!'''


if answer == "a":
    print(a)
    input("Type anything to close the program   " )
    exit()

elif answer == "b":
    print(b)
    input("Type anything to close the program   " )
    exit()
elif answer == "c":
    print(c)
    input("Type anything to close the program   " )
    exit()
elif answer == "d":
    print(d)
    input("Type anything to close the program   " )
    exit()

    

if answer2 in valid_answers:
    answer2 = input("Which riddle do you want to hear? a/b/c     ")
    if answer2 == "a":
        a = "what is something that is yours and everyone uses it? Your name!"
        print(a)
        input("Type anything to close the program   " )

    elif answer2 == "b":
        b = "What is something that always gets wet and is in your to do list? A towel!"
        print(b)
        input("Type anything to close the program   " )\

    elif answer2 == "c":
        c = 'What is something that you can eat and drink but not live in? A water bottle!'
        print(c)
        input("Type anything to close the program   " )
else:
    input("GET OUT OF HERE  ")