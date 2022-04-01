"""
Jason Lee
A15879338
Homework 01
This is the hw01 file. It contains the code of the 10 given functions and 3
doctests for each function.

TODO: This will be the module docstring; please put the description
of this module, or file, here as how it is done with the method
docstrings
"""

# Question 1
def sum_two(x,y):
    """Return the result sum of x and y
    >>> sum_two(2,-2)
    0
    >>> sum_two(-100,150)
    50
    >>> sum_two(-10, -10)
    -20
    >>> sum_two(-100,100)
    0
    >>> sum_two(20000,0)
    20000
    >>> sum_two(0.5,1.3)
    1.8
    """
    total = x + y
    return total

# Question 2
def distance(x1, y1, x2, y2):
    """Return the distance between the points (float)
    between (x1,y1) and (x2,y2)
    >>> distance(0, 0, 3, 4)
    5.0
    >>> distance(-3, -4, 3, 4)
    10.0
    >>> distance (100, 100, 100.5, 100)
    0.5
    >>> distance(0,1,0,1)
    0.0
    >>> distance(1,2,8,2)
    7.0
    >>> distance(2,100,100,100)
    98.0
    """
    half = 0.5
    squared = 2
    total_distance = (((x2-x1)**squared) + ((y2-y1)**squared))**half
    return total_distance

# Question 3
def find_slope(x1, y1, x2, y2):
    """Return the slope of the line (float) between
    points (x1,y1) and (x2,y2)
    >>> find_slope(0,0,5,5)
    1.0
    >>> find_slope(0, 0, 1 , 0.5)
    0.5
    >>> find_slope(1, 1, -1, -1)
    1.0
    >>> find_slope(0, 0, 1, 2)
    2.0
    >>> find_slope(3, 0, 6, 0)
    0.0
    >>> find_slope(1, 3, 3, 9)
    3.0
    >>> find_slope(6, 6, 12, 9)
    0.5
    """
    if x1 == x2 and y1 == y2:
        return 0.0
    else:
        slope = (y2-y1)/(x2-x1)
        return slope

# Question 4
def find_intercept(x1, y1, x2, y2):
    """Return y intercept of the line (float) between
    points (x1,y1) and (x2,y2)
    >>> find_intercept(0, 0, 123, 123)
    0.0
    >>> find_intercept(-22, -55, 55, 22)
    -33.0
    >>> find_intercept(-20, 20, 30, 40)
    28.0
    >>> find_intercept(6, 0, 6, 0)
    0.0
    >>> find_intercept(3, -60, 1, -180)
    -240.0
    >>> find_intercept(2, 10, -3, 40)
    22.0
    """
    slope = find_slope(x1, y1, x2, y2)
    intercept = y1 - (slope * x1)
    no_slope = 0.0
    if find_slope == 0.0:
        return y1
    else:
        return intercept

# Question 5
def is_triangle (x1, y1, x2, y2, x3, y3):
    """Return True if points (x1,y1), (x2,y2) and (x3,y3) form a
    triangle. Returns False otherwise.
    >>> is_triangle(0, 0, 3, 0, 3, 4)
    True
    >>> is_triangle(-3, -3, 0, 0, 3, 3)
    False
    >>> is_triangle(-5, -5, 1, 2, -10, 15)
    True
    >>> is_triangle(0, 1, 3, 10, 8, 2)
    True
    >>> is_triangle(2, 6, 2, 10, 3, -2)
    True
    >>> is_triangle(1, 4, 1, 4, 2, 5)
    False
    """
    first_distance = distance(x1,y1,x2,y2)
    second_distance = distance(x1,y1,x3,y3)
    third_distance = distance(x2,y2,x3,y3)
    if first_distance + second_distance > third_distance:
        if first_distance + third_distance > second_distance:
            if second_distance + third_distance > first_distance:
                return True
            else:
                return False
        else:
            return False
    else:
        return False

# Question 6
def is_right_triangle(x1, y1, x2, y2, x3, y3):
    """Return True if points (x1,y1), (x2,y2) and (x3,y3)
    form a right triangle. Returns False otherwise.
    >>> is_right_triangle(0, 0, 0, 3, 4, 0)
    True
    >>> is_right_triangle(0, 0, 0, 12, 5, 0)
    True
    >>> is_right_triangle(-3, -3, 0, 0, 3, 3)
    False
    >>> is_right_triangle(0, 0, 5, 5, 10, 10)
    False
    >>> is_right_triangle(3, 0, 6, 0, 3, 1)
    False
    >>> is_right_triangle(2, 1, 5, 7, 4, 0)
    True
    """
    d1 = distance(x1, y1, x2, y2)
    d2 = distance(x3, y3, x2, y2)
    d3 = distance(x3, y3, x1, y1)
    hypotenuse = max(d1,d2,d3)
    check_triangle = is_triangle(x1, y1, x2, y2, x3, y3)
    if check_triangle == True:
        if hypotenuse == d1:
            if d2**2 + d3**2 == d1**2:
                return True
            else:
                return False
        elif hypotenuse == d2:
            if d1**2 + d3**2 == d2**2:
                return True
            else:
                return False
        elif hypotenuse == d3:
            if d2**2 + d1**2 == d3**2:
                return True
            else:
                return False
    else:
        return False

# Question 7
def is_equilateral_triangle(x1, y1, x2, y2, x3, y3):
    """Return True if points (x1,y1), (x2,y2) and (x3,y3) form a
    equilateral triangle. Returns False otherwise.
    >>> is_equilateral_triangle(2,1, 7,1 ,4.5, 5.33)
    True
    >>> is_equilateral_triangle(0, 0, 10, 0, 3, 4)
    False
    >>> is_equilateral_triangle(-5, -4, -2, -4, -3.5, -1.402)
    True
    >>> is_equilateral_triangle(0, 0, 3, 0, 0, -2)
    False
    >>> is_equilateral_triangle(-3, 3, 0, -3, 3, 3)
    False
    >>> is_equilateral_triangle(-1, 2, 4, 2, 1.5, 6.33)
    True
    """
    d1 = round(distance(x1, y1, x2, y2), 3)
    d2 = round(distance(x3, y3, x2, y2), 3)
    d3 = round(distance(x3, y3, x1, y1), 3)
    check_triangle = is_triangle(x1, y1, x2, y2, x3, y3)
    if check_triangle == True:
        if d1 == d2 == d3:
            return True
        else:
            return False
    else:
        return False

# Question 8
def type_of_triangle(x1, y1, x2, y2, x3, y3):
    """Return the type of triangle formed by
    points (x1,y1), (x2,y2)  and (x3,y3).
    >>> type_of_triangle(-5, -4, -2, -4, -3.5, -1.402)
    'Equilateral triangle'
    >>> type_of_triangle(0, 0, 0, 3, 4, 0)
    'Right triangle'
    >>> type_of_triangle(0, 0, 0, 12, 5, 0)
    'Right triangle'
    >>> type_of_triangle( 1, 2, 3, 4, -2, 6)
    'Simple triangle'
    >>> type_of_triangle( -3, -3, 0, 0, 3, 3)
    'Not a triangle'
    >>> type_of_triangle(2, 1, 2, 6, 5, 8)
    'Simple triangle'
    >>> type_of_triangle(0, 5, 5, 8, 0, 5)
    'Not a triangle'
    >>> type_of_triangle(2, -1, 2, 3, -3, -1)
    'Right triangle'
    """
    triangle_check = is_triangle(x1, y1, x2, y2, x3, y3)
    right_triangle_check = is_right_triangle(x1,y1,x2,y2,x3,y3)
    equilateral_triangle_check = is_equilateral_triangle(x1,y1,x2,y2,x3,y3)
    if triangle_check == True:
        if right_triangle_check == True:
            return 'Right triangle'
        elif equilateral_triangle_check == True:
            return 'Equilateral triangle'
        else:
            return 'Simple triangle'
    else:
        return 'Not a triangle'

# Question 9:
def even_odd_list(lst1):
    """Return a new list indicating which replaces each
    element of lst1 with "Even" or "Odd". See the doctest
    examples for reference.
    >>> even_odd_list([1, 2, 3])
    ['Odd', 'Even', 'Odd']
    >>> even_odd_list([5, 8, 9, 10, 12])
    ['Odd', 'Even', 'Odd', 'Even', 'Even']
    >>> even_odd_list([-5, -1, -3])
    ['Odd', 'Odd', 'Odd']
    >>> even_odd_list([-2, 3, 11])
    ['Even', 'Odd', 'Odd']
    >>> even_odd_list([0,-100,61])
    ['Even', 'Even', 'Odd']
    >>> even_odd_list([-1, 0, 5, -1000, 49/2])
    ['Odd', 'Even', 'Odd', 'Even', 'Odd']
    >>> even_odd_list([2**2, 3*9, 6**(3/2)])
    ['Even', 'Odd', 'Odd']
    """
    divisible_by_2 = 2
    new_list = []
    for i in range(len(lst1)):
        if lst1[i] % divisible_by_2 == 0:
            new_list.append('Even')
        else:
            new_list.append('Odd')
    return new_list

# Question 10
def party (guests):
    """Scans the guests of the event. If the # of people who
    want to party (42's) is equal to or above 50%,
    returns "There is a party!". Otherwise returns
    "No party this time".

    >>> party([0,1,42,42,42,13,6,5])
    'No party this time'
    >>> party([0,1,42,42,42,42,6,7])
    'There is a party!'
    >>> party([0,42,6,42,42,7,66,12,13,42,42,42])
    'There is a party!'
    >>> party([0,1,42,5,6,42,42,42,5])
    'No party this time'
    >>> party([2,6,31,42])
    'No party this time'
    >>> party([21*2, 84/2, 42, 0])
    'There is a party!'
    >>> party([0.5, 42, 42, 1])
    'There is a party!'
    """
    over_half = 0.5
    party_number = 42
    guests_42_count = guests.count(party_number)
    total_guests = len(guests)
    if guests_42_count/total_guests >= over_half:
        return 'There is a party!'
    else:
        return 'No party this time'
