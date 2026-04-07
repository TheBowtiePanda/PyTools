import random

class arthurs_pytools:
    # TheBowtiePanda
    def bare_input(name):
        # makes a user input
        user_input = input(f'{name}: ')
        #removes punctuation and spaces from the input
        user_input = user_input.lower().replace("!", "").replace(".", "").replace("?", "").replace(",", "").replace("'", "").replace(" ", "")
        #returns user input
        return user_input


    # TheBowtiePanda
    def random_list(length, min_value, max_value):
        ran_list = []
        #loops (length) times
        while length > 0:
            #make a random number
            random_int = random.randint(min_value, max_value)
            #add that number to a list
            ran_list.append(random_int)
            length -= 1
        return ran_list


    # TheBowtiePanda
    def dice_roll(sides, times_rolled=1):
        rolls = []
        #loops (times_rolled) times. default of 1
        while 0 < times_rolled:
            #pick a random side of the die
            side = random.choice(sides)
            #add that to a list
            rolls.append(side)
            times_rolled -= 1
        return rolls

    # checks to see if a given number is prime (returns True/False)
    def is_prime(num):
        i: int = 2
        while i<=math.sqrt(num):
            if num % i == 0:
                return False
            i=i+1
        return True






