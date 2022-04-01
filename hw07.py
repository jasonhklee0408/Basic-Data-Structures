"""
DSC 20 HW 07
NAME: Jason Lee
PID: A15879338
"""

## Question 1.1 ##
last_item_to_clear = 4

def populate_menu_schedule(menu_schedule, recipe_dict):
    """
    Populate the given menu_schedule with recipes based on recipe_dict

    Parameters:
    menu_schedule (tuple): A tuple with five dictionaries representing the menu
    recipe_dict (dict): A dictionary of food recipe

    Returns:
    (None)

    >>> menu_schedule = ( \
            {"Orange Chicken": [], "Broccoli Beef": []}, \
            {"Broccoli Beef": []}, \
            {"Orange Chicken": [], "Spring Roll": []}, \
            {"Fortune Cookie": []}, \
            {"Fortune Cookie": [], "Broccoli Beef": []} \
        )
    >>> recipe_dict = { \
	        "Orange Chicken": ["Orange", "Chicken"], \
	        "Fortune Cookie": ["Fortune", "Cookie", "Paper"], \
	        "Spring Roll": ["Egg"] \
        }
    >>> populate_menu_schedule(menu_schedule, recipe_dict)
    >>> menu_schedule
    ({'Orange Chicken': ['Orange', 'Chicken']}, {}, {'Orange Chicken': \
['Orange', 'Chicken'], 'Spring Roll': ['Egg']}, {'Fortune Cookie': \
['Fortune', 'Cookie', 'Paper']}, {'Orange Chicken': ['Orange', 'Chicken']})
    >>> menu_schedule[0]['Orange Chicken'].append("Hot Sauce")
    >>> menu_schedule[2]['Orange Chicken']
    ['Orange', 'Chicken', 'Hot Sauce']
    >>> menu_schedule[0]['Gyro Plate'] = ['Beef']
    >>> menu_schedule[0]
    {'Orange Chicken': ['Orange', 'Chicken', 'Hot Sauce'], 'Gyro Plate': \
['Beef']}
    >>> menu_schedule[4]
    {'Orange Chicken': ['Orange', 'Chicken', 'Hot Sauce']}

    +++++++++++++++++++++++++
    WRITE YOUR DOCTESTS BELOW
    +++++++++++++++++++++++++
    >>> menu_schedule = ( \
            {"KungPao Chicken": []}, \
            {"Walnut Shrimp": []}, \
            {"Orange Chicken": []}, \
            {"Walnut Shrimp": []}, \
            {"KungPao Chicken": [], "Walnut Shrimp": []} \
        )
    >>> recipe_dict = { \
	        "Orange Chicken": ["Orange", "Chicken"], \
	        "KungPao Chicken": ["Kung Pao Sauce", "Chicken"], \
	        "Walnut Shrimp": ["Walnut", "Shrimp"] \
        }
    >>> populate_menu_schedule(menu_schedule, recipe_dict)
    >>> menu_schedule
    ({'KungPao Chicken': ['Kung Pao Sauce', 'Chicken']}, {'Walnut Shrimp': \
['Walnut', 'Shrimp']}, {'Orange Chicken': ['Orange', 'Chicken']}, \
{'Walnut Shrimp': ['Walnut', 'Shrimp']}, {'KungPao Chicken': \
['Kung Pao Sauce', 'Chicken']})
    >>> menu_schedule[1]
    {'Walnut Shrimp': ['Walnut', 'Shrimp']}
    >>> menu_schedule[2]
    {'Orange Chicken': ['Orange', 'Chicken']}
    >>> menu_schedule[2]['Orange Chicken'].append('Orange Juice')
    >>> menu_schedule[2]
    {'Orange Chicken': ['Orange', 'Chicken', 'Orange Juice']}
    >>> menu_schedule[3]['Water'] = ['H20']
    >>> menu_schedule[3]
    {'Walnut Shrimp': ['Walnut', 'Shrimp'], 'Water': ['H20']}
    """
    # YOUR CODE STARTS HERE #
    assert isinstance(menu_schedule, tuple)
    assert isinstance(recipe_dict, dict)
    for i in menu_schedule:
        assert isinstance(i, dict)
    
    update_dict = recipe_dict
    menu_schedule[last_item_to_clear].clear()
    for i in list(menu_schedule[0].keys()):
        menu_schedule[last_item_to_clear][i] = []

    for key in list(update_dict.keys()):
        updated_key = update_dict[key]
        for dict_menu in menu_schedule:
            for n in list(dict_menu.keys()):
                if n == key:
                    dict_menu[n] = updated_key

    for dict_menu in menu_schedule:
        for n in list(dict_menu.keys()):
            if dict_menu[n] == []:
                del dict_menu[n]


## Question 1.2 ##

def dereference_recipes(menu_schedule):
    """
    Dereference all pairs of recipe that refers to the same recipe object

    Parameters:
    menu_schedule (tuple): A tuple with five dictionaries representing the menu
        whose recipes have been already populated

    Returns:
    (None)

    >>> menu_schedule = ( \
            {"Orange Chicken": [], "Broccoli Beef": []}, \
            {}, \
            {}, \
            {}, \
            {"Orange Chicken": [], "Broccoli Beef": []} \
        )
    >>> oc_recipe = ['Orange', 'Chicken']
    >>> bb_recipe = ['Love']
    >>> menu_schedule[0]["Orange Chicken"] = oc_recipe
    >>> menu_schedule[4]["Orange Chicken"] = oc_recipe
    >>> menu_schedule[0]["Broccoli Beef"] = bb_recipe
    >>> menu_schedule[4]["Broccoli Beef"] = bb_recipe
    >>> menu_schedule[4]["Broccoli Beef"].append('Peace')
    >>> dereference_recipes(menu_schedule)
    >>> menu_schedule[4]["Broccoli Beef"].remove('Peace')
    >>> menu_schedule[0]["Broccoli Beef"]
    ['Love', 'Peace']

    +++++++++++++++++++++++++
    WRITE YOUR DOCTESTS BELOW
    +++++++++++++++++++++++++
    >>> menu_schedule = ( \
            {"Orange Chicken": [], "Walnut Shrimp": []}, \
            {}, \
            {"Orange Chicken": [], "Walnut Shrimp": []}, \
            {}, \
            {} \
        )
    >>> oc_recipe = ['Orange', 'Chicken']
    >>> ws_recipe = ['Crab', 'Peanuts']
    >>> menu_schedule[0]["Orange Chicken"] = oc_recipe
    >>> menu_schedule[2]["Orange Chicken"] = oc_recipe
    >>> menu_schedule[0]["Walnut Shrimp"] = ws_recipe
    >>> menu_schedule[2]["Walnut Shrimp"] = ws_recipe
    >>> menu_schedule[2]["Walnut Shrimp"].append('Poison')
    >>> dereference_recipes(menu_schedule)
    >>> menu_schedule[2]["Walnut Shrimp"].remove('Poison')
    >>> menu_schedule[2]["Walnut Shrimp"]
    ['Crab', 'Peanuts']
    """
    # YOUR CODE STARTS HERE #
    assert isinstance(menu_schedule, tuple)
    for i in menu_schedule:
        assert isinstance(i, dict)

    key_lst = []
    for dict_menu in menu_schedule:
        for i in list(dict_menu.keys()):
            key_lst.append(i)

    duplicate_list = []
    for n in key_lst:
        if key_lst.count(n) > 1:
            duplicate_list.append(n)

    no_dup_lst = []
    for i in duplicate_list:
        if i not in no_dup_lst:
            no_dup_lst.append(i)

    for dict_menu in menu_schedule:
        for item in list(dict_menu.keys()):
            if item in no_dup_lst:
                increment_lst = []
                for increment in dict_menu[item]:
                    increment_lst.append(increment)
                dict_menu[item] = increment_lst


## Question 2 is in hw07_OOP.py ##

## Question 3.1 ##

def create_palindrome_v1(start, end):
    """
    Creates a palindrome of integers starting from start, ending at end
    (in the middle) All inputs are positive integers. No input validation
    required.
    Parameters: start, end (int), positive integers
    Returns: palindrome sequence (str)
    Restrictions. You should use recursion in this question.
    >>> create_palindrome_v1(1, 1)
    '1'
    >>> create_palindrome_v1(3, 5)
    '34543'
    >>> create_palindrome_v1(5, 2)
    '5432345'

    +++++++++++++++++++++++++
    WRITE YOUR DOCTESTS BELOW
    +++++++++++++++++++++++++
    >>> create_palindrome_v1(0, 1)
    '010'
    >>> create_palindrome_v1(0, 0)
    '0'
    >>> create_palindrome_v1(10, 0)
    '10987654321012345678910'
    """
    # YOUR CODE STARTS HERE #
    if start > end:
        return str(start) + create_palindrome_v1(start-1, end) + str(start)
    elif start < end:
        return str(start) + create_palindrome_v1(start+1, end) + str(start)
    elif start == end:
        return str(end)

## Question 3.2 ##

def create_palindrome_v2(start1, end1, start2, end2):
    """
    Creates a two level palindrome of integers. The first level (outer level)
    starts from start1 and ends at end1. The second level (inner level) starts
    from start2 and end2. No input validation is required.
    Parameters: start1, end1, start2, end2 (int), positive integers
    Returns: palindrome sequence (str)
    Restrictions. You should use recursion in this question.
    >>> create_palindrome_v2(1, 1, 1, 1)
    '1_1_1'
    >>> create_palindrome_v2(2, 5, 5, 4)
    '2345_545_5432'
    >>> create_palindrome_v2(3, 1, 5, 9)
    '321_567898765_123'

    +++++++++++++++++++++++++
    WRITE YOUR DOCTESTS BELOW
    +++++++++++++++++++++++++
    >>> create_palindrome_v2(1, 2, 3, 4)
    '12_343_21'
    >>> create_palindrome_v2(4, 3, 2, 1)
    '43_212_34'
    >>> create_palindrome_v2(6, 5, 2, 14)
    '65_2345678910111213141312111098765432_56'
    """
    # YOUR CODE STARTS HERE #
    if start1 > end1:
        return str(start1) + create_palindrome_v2(start1-1, end1, start2, end2) + str(start1)
    elif start1 < end1:
        return str(start1) + create_palindrome_v2(start1+1, end1, start2, end2) + str(start1)
    elif start1 == end1:
        return str(end1) + '_' + create_palindrome_v1(start2, end2) + '_' + str(end1)
