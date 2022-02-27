<<<<<<< HEAD
import random
name = input("Hello! What is your name?\n")
print("Well, {}, I am thinking of a number between 1 and 20.".format(name))
print("Take a guess.")
true_number = random.randint(1, 20)
cnt = 0
while(1):
    cnt += 1
    guess_number = int(input())
    if guess_number == true_number:
        print("Good job, {}! You guessed my number in {} guesses!".format(name, cnt))
        break
    elif true_number > guess_number:
        print("Your guess is too low.", "Take a guess.", sep="\n")
    else:
        print("Your guess is too high.", "Take a guess.", sep="\n")
=======
import random
name = input("Hello! What is your name?\n")
print("Well, {}, I am thinking of a number between 1 and 20.".format(name))
print("Take a guess.")
true_number = random.randint(1, 20)
cnt = 0
while(1):
    cnt += 1
    guess_number = int(input())
    if guess_number == true_number:
        print("Good job, {}! You guessed my number in {} guesses!".format(name, cnt))
        break
    elif true_number > guess_number:
        print("Your guess is too low.", "Take a guess.", sep="\n")
    else:
        print("Your guess is too high.", "Take a guess.", sep="\n")
>>>>>>> 68ee922863d7bbad933d1b77aaeeaf5cf621a9da
