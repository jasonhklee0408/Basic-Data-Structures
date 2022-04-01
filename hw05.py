"""
DSC 20 HW 05
NAME: Jason Lee
PID: A15879338
"""

from functools import reduce

# Question 1.1:
def question1_1():
    """Return a list with answers to the True/False questions.
    >>> out = question1_1()
    >>> type(out) == list
    True
    >>> len(out)
    10
    >>> all([isinstance(i, bool) for i in out])
    True
    """
    return [True, False, True, False, False, False, True, True, True, False]

# Question 1.2:
def question1_2():
    """Return a list with answers to the code complexity questions.
    >>> out = question1_2()
    >>> type(out) == list
    True
    >>> len(out)
    15
    >>> all([isinstance(i, int) and i<=7 and i>=1 for i in out])
    True
    """
    return [3,6,2,2,5,5,6,6,4,4,1,3,3,4,5]

# Question 2.1:
def make_id(name, suffix):
    """Returns a netid for name with suffix n.
    >>> make_id('Marina Aleksandrovna Langlois', 17)
    'mal17'
    >>> make_id('Donald Trump', "boss")
    'dtboss'

    +++++++++++++++++++++++++
    >>> make_id('alex lee', 'alex lee')
    'alalex lee'
    >>> make_id('JASON LEE', 'dsc20')
    'jldsc20'
    >>> make_id('tom brAdy', '2019')
    'tb2019'

    +++++++++++++++++++++++++

    """
    name_list = name.split(' ')
    netid = ''
    for i in name_list:
        netid += i[0].lower()
    netid += str(suffix)
    return netid

# Question 2.2:
def do_you_have_me(dic, item):
    """Returns a key for which item exists
    otherwise returns "Not there"
    >>> do_you_have_me({"key1":[1,2,3,4], "key2": [5,4,7,8]}, 9)
    'Not there'
    >>> do_you_have_me({"key1":[1,2,3,4], "key2": [5,4,7,8]}, 1)
    'key1'
    >>> do_you_have_me({"key1":[1,2,3,4], "key2": [5,4,7,8]}, 4)
    'key1'

    +++++++++++++++++++++++++
    >>> do_you_have_me({"key1":[0,1,2,3], "key2": [4,5,6,7]}, 1-0)
    'key1'
    >>> do_you_have_me({"key1":[0,1,2,3], "key2": [4,5,6,7]}, 'mal')
    'Not there'
    >>> do_you_have_me({"key1":[0,1,2,3], "key2": [4,5,6,7]}, 1.5)
    'Not there'

    +++++++++++++++++++++++++

    """
    for i in dic.items():
        if item in i[1]:
            return i[0]
        else:
            return 'Not there'

# Question 2.3:
def read_menus(food_cat, *menus):
    """Return a string that summarized amount of items from the same category
    in the menus.
    >>> read_menus("food_cat.txt", "menu1.txt", "menu2.txt")
    'There are 7 burgers, 4 salads and 5 desserts'

    +++++++++++++++++++++++++
    >>> read_menus("food_cat.txt", "example.txt")
    'There are 5 burgers, 0 salads and 0 desserts'
    >>> read_menus("food_cat.txt", "example2.txt")
    'There are 8 burgers, 4 salads and 6 desserts'
    >>> read_menus("food_cat.txt", "example3.txt", "example4.txt")
    'There are 8 burgers, 4 salads and 6 desserts'

    +++++++++++++++++++++++++

    """
    dict = {}
    burger_tally = 0
    salad_tally = 0
    dessert_tally = 0
    final = ''
    with open(food_cat, 'r') as f:
        for line in f:
            new_line = line.split(':')
            replaced = new_line[1].replace('\n','')
            if replaced not in dict:
                dict[replaced] = [new_line[0]]
            else:
                dict[replaced].append(new_line[0])

    dict_list = list(dict.items())

    for menu in menus:
        with open(menu, 'r') as m:
            for line in m:
                menu_line = line.split(':')[0]
                for item in range(len(dict_list)):
                    for dishes in range(len(dict_list[item][1])):
                        set = dict_list[item][1][dishes]
                        if menu_line == set:
                            if dict_list[item][0] ==  ' Burger':
                                burger_tally += 1
                            elif dict_list[item][0] == ' Salad':
                                salad_tally += 1
                            elif dict_list[item][0] == ' Dessert':
                                dessert_tally += 1

    final += 'There are ' + str(burger_tally) + ' burgers, ' + str(salad_tally) + ' salads \
and ' + str(dessert_tally) + ' desserts'

    return final



# Question 2.4
def cuboid_coordinates(x, y, z, n):
    """
    Return a list of all possible coordinates (i, j, k)
    such that i + j + k is not equal to n.

    Restrictions: Your solution must be one line.

    >>> cuboid_coordinates(1, 1, 1, 2)
    [(0, 0, 0), (0, 0, 1), (0, 1, 0), (1, 0, 0), (1, 1, 1)]

    +++++++++++++++++++++++++
    >>> cuboid_coordinates(0, 0, 0, 1)
    [(0, 0, 0)]
    >>> cuboid_coordinates(1, 1, 1, 3)
    [(0, 0, 0), (0, 0, 1), (0, 1, 0), (0, 1, 1), (1, 0, 0), (1, 0, 1), (1, 1, 0)]
    >>> cuboid_coordinates(1, 2, 0, 1)
    [(0, 0, 0), (0, 2, 0), (1, 1, 0), (1, 2, 0)]

    +++++++++++++++++++++++++

    """
    return [(a,b,c) for a in range(x+1) for b in range(y+1) for c in range(z+1) if a+b+c != n]

# Question 2.5
def k_mapping(inp, k):
    """
    Maps each element in the circular list to the
    element k spaces in front of it.

    >>> k_mapping([1, 2, 3, 4, 5], 2)
    '1 -> 3, 3 -> 5, 5 -> 2, 2 -> 4, 4 -> 1'
    >>> k_mapping([1, 2, 3], 3)
    '1 -> 1, 2 -> 2, 3 -> 3'

    +++++++++++++++++++++++++
    >>> k_mapping([0, 1, 2, 3], 1)
    '0 -> 1, 1 -> 2, 2 -> 3, 3 -> 0'
    >>> k_mapping([1, 2, 3, 4], 5)
    '1 -> 2, 2 -> 3, 3 -> 4, 4 -> 1'
    >>> k_mapping([1, 2, 3, 4, 5, 6], 3)
    '1 -> 4, 4 -> 1, 1 -> 4, 4 -> 1, 1 -> 4, 4 -> 1'

    +++++++++++++++++++++++++

    """
    final_str = ''
    bigger_list = inp*(k+1)

    final_lst = bigger_list[k:len(bigger_list)-len(inp)+1:k]
    if final_lst[0] == inp[0]:
        bigger_list = inp * k
        for i in range(len(inp)):
            final_str += str(inp[i]) + ' -> ' + str(bigger_list[i+k])
            if i != len(inp)-1:
                final_str += ', '
        return final_str
    else:
        for i in range(len(inp)):
            final_str += str(final_lst[i-1]) + ' -> ' + str(final_lst[i])
            if i != len(inp)-1:
                final_str += ', '
        return final_str

# Question 2.6
def gcd_fraction(frac_lst):
    """
    Returns the reduced fraction made by multiplying
    fractions in frac_lst. The first element of each
    tuple represents the numerator and the second
    element represents the denominator.

    Restrictions: No loops or maps outside the gcd inner function.
    Must use reduce.

    >>> gcd_fraction([(1, 2), (3, 4), (10, 6)])
    (5, 8)

    +++++++++++++++++++++++++
    >>> gcd_fraction([(1, 2), (1, 3), (1, 4)])
    (1, 24)
    >>> gcd_fraction([(1, 1), (3, 4), (10, 6)])
    (5, 4)
    >>> gcd_fraction([(2, 4), (3, 6), (4, 8)])
    (1, 8)

    +++++++++++++++++++++++++

    """
    listed_map = list(map(lambda x: list(x), frac_lst))
    total = reduce(lambda x,y: [x[0]*y[0],y[1]*x[1]], listed_map)
    def gcd(x, y):
        """
        Find the greatest common divisor between x and y.
        """
        while y:
            t = y
            y = x % y
            x = t
        return x
    denominator = gcd(total[0], total[1])
    return (int(total[0]/denominator), int(total[1]/denominator))
