"""
DSC 20 HW 04
NAME: Jason Lee
PID: A15879338
"""

from math import factorial
from math import floor

## Question 1 ##
maximum = 100000
def prime_number_generator(number_of_primes):
    """
    Generator for creating the first 'number_of_primes' prime numbers
    using the prime number formula based on Wilson's theorem

    Restrictions:
    You should use a generator in this question.

    Parameters:
    number_of_primes (int): Number of primes to be generated

    Returns:
    The required generator of the question.

    >>> prime_gen = prime_number_generator(2)
    >>> next(prime_gen)
    2
    >>> list(prime_number_generator(10))
    [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    >>> prime_gen = prime_number_generator(20)
    >>> list(prime_gen)[10:20]
    [31, 37, 41, 43, 47, 53, 59, 61, 67, 71]

    +++++++++++++++++++++++++
    >>> list(prime_number_generator(5))
    [2, 3, 5, 7, 11]
    >>> list(prime_number_generator(8))
    [2, 3, 5, 7, 11, 13, 17, 19]
    >>> list(prime_number_generator(12))
    [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]

    +++++++++++++++++++++++++

    """
    tally = 0
    total_number = list(range(1,maximum))
    for n in total_number:
        if ((factorial(n)%(n+1)) // n) == 1:
            yield n+1
            tally += 1
            if tally == number_of_primes:
                break

## Question 2.1 ##
def exp_gen(n, e):
    """A generator that yields the following exponentials
    (given n, e as inputs):
    n**e, (n*e)**e, (n*e*e)**e, (n*e*e*e)**e, ... (and so on)
    >>> gen = exp_gen(2,2)
    >>> next(gen)
    4
    >>> next(gen)
    16
    >>> next(gen)
    64
    >>> next(gen)
    256

    +++++++++++++++++++++++++
    >>> new_gen = exp_gen(2, 4)
    >>> next(new_gen)
    16
    >>> next(new_gen)
    4096
    >>> y = exp_gen('y', 2)
    >>> next(y)
    Traceback (most recent call last):
    ...
    AssertionError

    +++++++++++++++++++++++++

    """
    assert isinstance(n, int)
    assert isinstance(e, int)
    tally = 0
    while tally >- 1:
        number = (n*(e**tally))**e
        tally += 1
        yield number

## Question 2.2 ##
def luc_seq():
    """A generator that yields the Lucas Sequence
    >>> gen = luc_seq()
    >>> next(gen)
    2
    >>> next(gen)
    1
    >>> next(gen)
    3

    +++++++++++++++++++++++++
    >>> new_gen = luc_seq()
    >>> next(gen)
    4
    >>> next(gen)
    7
    >>> next(gen)
    11
    >>> next(gen)
    18
    >>> next(gen)
    29
    >>> next(gen)
    47
    >>> next(gen)
    76

    +++++++++++++++++++++++++

    """
    a1,b1 = 2,1
    while 1:
        yield a1
        a1,b1 = b1, a1+b1

## Question 2.3 ##
def alpha_gen(stars_count, word):
    """Return a function that creates a generator that yields a
    letter from a given string with a specified number of stars between
    each letter.

    >>> gen = alpha_gen(2, "marina")
    >>> next(gen)
    'm'
    >>> next(gen)
    '*'
    >>> next(gen)
    '*'
    >>> for i in gen:
    ... 	print(i, end='')
    a**r**i**n**a**

    +++++++++++++++++++++++++
    >>> example = alpha_gen(3, 'thomas')
    >>> next(example)
    't'
    >>> next(example)
    '*'
    >>> next(example)
    '*'
    >>> next(example)
    '*'
    >>> example_2 = alpha_gen(1, 'maria')
    >>> list(example_2)
    ['m', '*', 'a', '*', 'r', '*', 'i', '*', 'a', '*']
    >>> example_3 = alpha_gen(0, 'kyle')
    >>> list(example_3)
    ['k', 'y', 'l', 'e']

    +++++++++++++++++++++++++

    """
    assert isinstance(stars_count, int)
    assert isinstance(word, str)
    assert len(word) > 0
    spacing = stars_count + 1
    for i in range((len(word)*spacing)):
        if i % spacing == 0:
            yield word[int(i/spacing)]
        else:
            yield '*'

## Question 2.4 ##
def generate_generators():
    """
    Return a generator that yields the previous three generators.
    First Yield:  exp_gen
    Second Yield: luc_seq
    Third Yield:  alpha_gen

    >>> gen_list = generate_generators()
    >>> exp_gnr = next(gen_list)
    >>> lucas_gnr = next(gen_list)
    >>> alpha_func = next(gen_list)
    >>> func1 = exp_gnr(2,2)
    >>> next(func1)
    4
    >>> next(func1)
    16
    >>> next(func1)
    64
    >>> next(lucas_gnr)
    2
    >>> next(lucas_gnr)
    1
    >>> next(lucas_gnr)
    3
    >>> alpha_gen = alpha_func(2, "marina")
    >>> next(alpha_gen)
    'm'
    >>> next(alpha_gen)
    '*'
    >>> next(alpha_gen)
    '*'
    >>> for i in alpha_gen:
    ... 	print(i, end='')
    a**r**i**n**a**

    +++++++++++++++++++++++++
    >>> example_list = generate_generators()
    >>> new_exp = next(example_list)
    >>> new_lucas = next(example_list)
    >>> new_alpha = next(example_list)
    >>> new_func = new_exp(1,5)
    >>> next(new_func)
    1
    >>> next(new_func)
    3125
    >>> next(new_func)
    9765625
    >>> next(new_lucas)
    2
    >>> next(new_lucas)
    1
    >>> next(new_lucas)
    3
    >>> next(new_lucas)
    4

    +++++++++++++++++++++++++

    """
    yield exp_gen
    yield luc_seq()
    yield alpha_gen

## Question 3 ##
def get_negative_lists(super_list):
    """
    Return a map object containing the lists in the
    super list that contain negative numbers.

    Restrictions:
    No loops (Not even list comprehension!)

    Parameters:
    super_list (list): A list containing sublists of integers

    Returns:
    The map required by the question.

    >>> subLsts = [[1, 5, 2, 8, 4], [-900, -22, 33, -90, 529],\
[0, -2, 5, -199, 300]]
    >>> isinstance(type(get_negative_lists(subLsts)), type(map))
    True
    >>> list(get_negative_lists(subLsts))
    [[-900, -22, 33, -90, 529], [0, -2, 5, -199, 300]]
    >>> subLsts = [[7, 2, -1, -6, -100], [-1, 0, 5, 2, 3], [0, 0, 1, 0, 0]]
    >>> list(get_negative_lists(subLsts))
    [[7, 2, -1, -6, -100], [-1, 0, 5, 2, 3]]

    +++++++++++++++++++++++++
    >>> positive_list = [[1,2,3], [15,7,6], [2,5,8]]
    >>> list(get_negative_lists(positive_list))
    []
    >>> list(get_negative_lists([[-1],[0],[1]]))
    [[-1]]
    >>> new_list = []
    >>> list(get_negative_lists(new_list))
    Traceback (most recent call last):
    ...
    AssertionError

    +++++++++++++++++++++++++

    """
    assert len(super_list) > 0
    assert isinstance(super_list, list)
    def func(list):
        if min(list) < 0:
            return True
        else:
            return False

    total_list = filter(func, super_list)
    return total_list


## Question 4 ##
miles_conversion = 1.609344
two = 2
sq_root = 1/2

def get_distances():
    """
    Return a list of lambdas that help do bulk distance calculations on city
    coordinates.
    1: Define a function that converts miles to km, with miles as the input.
    2: Define a function that determines the distance between two points that
       use (x, y) coordinates as inputs
    3: Determine how many kilometers are between Point A(424.3601, 71.0589)
       and Point B (-3601.1128, 493.4276)
    4: Return a lambda that returns a map object of the distances between a
       list of tuple pairs of cities.


    >>> cities = [(424.3601, 71.0589), (-3601.1128, 493.4276), \
(158.1010, 8179.001), (-119.030, -117.334)]
    >>> lambda_functions = get_distances()
    >>> lambda_functions[0](1000)
    1609.344
    >>> lambda_functions[1](cities[0][0], cities[0][1],\
cities[1][0], cities[1][1])
    4047.5705537240606
    >>> lambda_functions[2]((cities[0], cities[1]))
    6513.933385212495
    >>> list(lambda_functions[3]([(cities[0], cities[1]),\
(cities[2], cities[3])]))
    [6513.933385212495, 13359.103960657963]

    +++++++++++++++++++++++++
    >>> cities_example = [(100, 100), (-3902.5, 0), \
(3124.65, 991.84), (-206.3, -68.9)]
    >>> example_lambda = get_distances()
    >>> example_lambda[0](10)
    16.09344
    >>> example_lambda[1](cities_example[0][0], cities_example[0][1],\
cities_example[1][0], cities_example[1][1])
    4003.749024352051
    >>> example_lambda[2]((cities_example[0], cities_example[1]))
    6443.409469846828
    >>> list(example_lambda[3]([(cities_example[0], cities_example[1]),\
(cities_example[2], cities_example[3])]))
    [6443.409469846828, 5625.8940250720825]

    +++++++++++++++++++++++++

    """
    miles_to_km = lambda x: x * miles_conversion
    distance = lambda x1,y1,x2,y2: ((x2 - x1)**two+(y2-y1)**two)**(sq_root)
    km_distance = lambda x1: miles_to_km(distance(x1[0][0], x1[0][1], x1[1][0],
    x1[1][1]))
    tuple = lambda x: map(lambda list: miles_to_km(distance(list[0][0],
    list[0][1], list[1][0], list[1][1])), x)

    return [miles_to_km, distance, km_distance, tuple]


## Question 5 ##
unpaid = 5
max_filepath = 4
increase_8 = 8
power_12 = 12
def calculate_wages(filepath):
    """
    Calculator for tutor wages. See question description for explanation.

    Restrictions:
    No loops (Not even list comprehension!)

    Parameters:
    filepath (str): Path to the input file

    Returns:
    dict: Dictionary of tutor names and their total wages

    >>> calculate_wages('data/input.txt')
    {'Judy': 8, 'Owen': 40, 'Xiang': 460}

    +++++++++++++++++++++++++
    WRITE YOUR DOCTESTS BELOW
    +++++++++++++++++++++++++

    """

    with open(filepath, 'r') as f:
        splitted_file = f.read().splitlines()
        dictionary_string = ','.join(splitted_file).split(',')

        tutors_list = dictionary_string[0:len(dictionary_string)+1:max_filepath]
        del dictionary_string[0:len(dictionary_string)+1:max_filepath]
        tutor_hours = [list(map(int, dictionary_string))]
        def conjugate(lst):
            totallist = []
            totallist.append(lst[0])
            totallist.append(lst[1])
            totallist.append(lst[2])
            return totallist

        tutor1 = list(map(conjugate, tutor_hours))[0]
        tutor_hours[0].pop(0)
        tutor_hours[0].pop(0)
        tutor_hours[0].pop(0)
        tutor2 = list(map(conjugate, tutor_hours))[0]
        tutor_hours[0].pop(0)
        tutor_hours[0].pop(0)
        tutor3 = list(map(conjugate, tutor_hours))[0]

        def calc_wage(sum_tutor):
            if sum_tutor < unpaid:
                return 0
            else:
                sum_tutor -= unpaid
                if sum_tutor <= unpaid:
                    sum_tutor = sum_tutor * increase_8
                    return sum_tutor
                else:
                    sum_tutor -= unpaid
                    sum_tutor = (sum_tutor*power_12)
                    return sum_tutor

        tutor1_paid = list(map(calc_wage, tutor1))
        tutor2_paid = list(map(calc_wage, tutor2))
        tutor3_paid = list(map(calc_wage, tutor3))
        all_paid = [sum(tutor1_paid), sum(tutor2_paid), sum(tutor3_paid)]
        final = dict(zip(tutors_list, all_paid))

        return final


## Question 6 ##
def calculate_best_scores(formulas, scores):
    """
    Calculates the maximum score achievable with the provided formulas.

    Restrictions:
    No loops (Not even list comprehension!)

    Parameters:
    formulas (list(lambda)) : List of lambda functions to be applied to scores
    scores (list(int)) : List of integers indicating the scores for students

    Returns:
    list : List of scores with the function that maximizes each score applied
    to it

    >>> calculate_best_scores([lambda x : x - 1], [3, 4, 5])
    [3, 4, 5]
    >>> calculate_best_scores([lambda x : x + 1], [3, 4, 5])
    [4, 5, 6]
    >>> calculate_best_scores([lambda x : x + 1, lambda x : x * 2,\
lambda x : x - 1], [3, 4, 5])
    [6, 8, 10]
    >>> calculate_best_scores([lambda x : x + 20, lambda x : x * 2,\
lambda x : x * 3], [3, 4, 20])
    [23, 24, 60]
    >>> calculate_best_scores([lambda x : x + 20], [3, 4, 5])
    [23, 24, 25]

    +++++++++++++++++++++++++
    >>> calculate_best_scores([lambda x : x + 1, lambda x:x* -1], [3, 4, 5])
    [4, 5, 6]
    >>> calculate_best_scores([lambda x : x**-1, lambda x:x* -1], [1, 2, 3])
    [1, 2, 3]
    >>> calculate_best_scores([lambda x : x**-1, lambda x:x* -1, \
lambda x: x**2], [2,4,8])
    [4, 16, 64]

    +++++++++++++++++++++++++

    """
    assert isinstance(formulas, list)
    assert isinstance(scores, list)
    assert callable(formulas[0])
    assert isinstance(scores[0], int)
    assert len(scores) == 3
    total_scores = list(map(lambda funcs: list(map(funcs, scores)),formulas))
    first_list = []
    second_list = []
    third_list = []

    max_1 = list(map(lambda x: first_list.append(x[0]), total_scores))
    max_2 = list(map(lambda x: second_list.append(x[1]), total_scores))
    max_3 = list(map(lambda x: third_list.append(x[2]), total_scores))

    max_list = [max(first_list),max(second_list),max(third_list)]

    if max_list == scores or sum(max_list) < sum(scores):
        return scores
    else:
        return max_list

## Question 7 ##
multiplier = 2
kill_multiplier = 4
trigger_multiplier = 10
def best_champ(champion_dict):
    """
    Returns a dictionary of champions and calculated scores.

    Restrictions:
    No loops (Not even list comprehension!)

    Parameters:
    champion_dict: a dictionary of champions and K/D/A slash lines

    Returns:
    dict: a dictionary of champions and scores

    >>> champ_dict = {'Lucian': '20/7/8', 'Caitlyn': '2/8/4', \
'Kha\\'Zix': '0/19/2'}
    >>> best_champ(champ_dict)
    {'Lucian': 77.0, 'Caitlyn': -2.0, "Kha'Zix": -8.5}

    +++++++++++++++++++++++++
    >>> best_champ({'Gnar': '2/5/3', 'Ornn': '10/3/6', \
'Camille': '2/2/2'})
    {'Gnar': 0.5, 'Ornn': 40.0, 'Camille': 3.0}
    >>> best_champ({'Ahri': '0/0/0', 'Lissandra': '10/2/3', \
'Vladimir': '1/5/10'})
    {'Ahri': 0.0, 'Lissandra': 39.5, 'Vladimir': 2.0}
    >>> best_champ({'Soraka': '0/1/21', 'Senna': '5/3/1', \
'Zyra': '10/10/3'})
    {'Soraka': 9.5, 'Senna': 7.5, 'Zyra': 36.5}

    +++++++++++++++++++++++++

    """
    assert isinstance(champion_dict, dict)
    assert len(champion_dict) > 0
    def kda(string):
        separated = string.split('/')
        kill = int(separated[0])
        death = int(separated[1])
        assist = int(separated[2])
        if kill >= trigger_multiplier:
            new_kill = kill*kill_multiplier
        else:
            new_kill = kill*multiplier
        if death >= trigger_multiplier:
            new_death = death/multiplier
        else:
            new_death = death
        new_assist = assist/multiplier

        return new_kill - new_death + new_assist
    names_list = list(champion_dict.keys())
    values_list = list(map(kda, list(champion_dict.values())))
    final_dict = dict(zip(champion_dict, values_list))

    return final_dict



## Question 8 ## (Extra Credit)
def find_positive_magic_integer(filepath):
    """
    Find any positive magic integers in the given file and output a dictionary
    whose keys are the string value of the found magic numbers and values
    are the line numbers where they were found.

    Parameters:
    filepath (str): A string containing the filepath.

    Returns:
    The dictionary described above.

    >>> find_positive_magic_integer('./data/magic_number_test1.py')
    {'2': [3, 11], '3': [4, 11], '4': [5, 11], '5': [6, 11], '6': [7, 11], \
'7': [8, 11], '8': [9, 11], '9': [10, 11]}
    >>> find_positive_magic_integer('./data/magic_number_test2.py')
    {'2': [4, 5], '3': [4, 6], '20': [7], '5': [8]}

    +++++++++++++++++++++++++
    WRITE YOUR DOCTESTS BELOW
    +++++++++++++++++++++++++

    """
