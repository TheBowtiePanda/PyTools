import random

class arthurs_pytools:
    def bare_input(name):
        user_input = input(f'{name}: ')
        user_input = user_input.lower().replace("!", "").replace(".", "").replace("?", "").replace(",", "").replace("'", "").replace(" ", "")
        return user_input



    def random_list(length, min_value, max_value):
        ran_list = []
        while length > 0:
            random_int = random.randint(min_value, max_value)
            ran_list.append(random_int)
            length -= 1
        return ran_list



    def dice_roll(sides, times_rolled=1):
        rolls = []
        while 0 < times_rolled:
            side = random.choice(sides)
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






