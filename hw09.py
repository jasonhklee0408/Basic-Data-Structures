"""
DSC 20 HW 09
NAME: Jason Lee
PID: A15879338
"""

## Question 1 ##

def checkingInputs(input1, input2, input3):
    """
    You will be handling 3 basic checks
    - are all the input types correct
    - does input2 exist within input3
    - can you divide input1 by input3

    >>> checkingInputs(15, 'key1', {'key1': 5, 'key2': 10})
    3.0

    >>> checkingInputs(15, 'key1', {'key1': 0, 'key2': 10})
    Traceback (most recent call last):
    ...
    ZeroDivisionError: Cannot divide 15 by 0

    >>> checkingInputs(15, 'key1', {'key2': 10})
    Traceback (most recent call last):
    ...
    KeyError: 'Cannot find key1 in the dictionary'

    >>> checkingInputs("15", 2810, ['key2', 10])
    Traceback (most recent call last):
    ...
    TypeError: Inputs are not the correct type

    +++++++++++++++++++++++++
    WRITE YOUR DOCTESTS BELOW
    +++++++++++++++++++++++++
    >>> checkingInputs('5', 'key2', {'key1':10, 'key2': 3})
    Traceback (most recent call last):
    ...
    TypeError: Inputs are not the correct type
    >>> checkingInputs(5, 'key3', {'key1':10, 'key2': 3})
    Traceback (most recent call last):
    ...
    KeyError: 'Cannot find key3 in the dictionary'
    >>> checkingInputs(5, 'key2', {'key1':10, 'key2': 10})
    0.5
    """
    if (isinstance(input2, str) == False):
        raise TypeError('Inputs are not the correct type')
    if (isinstance(input1, int) == False):
        raise TypeError('Inputs are not the correct type')
    if input2 not in list(input3.keys()):
        raise KeyError('Cannot find {} in the dictionary'.format(input2))
    if input3[input2] == 0:
        raise ZeroDivisionError('Cannot divide {} by 0'.format(input1))
    return input1/input3[input2]


## Question 2 ##

def loadFile(filename):
    """
    >>> loadFile("file1.txt")
    'File loaded'

    >>> loadFile("file2.txt")
    Traceback (most recent call last):
        ...
    FileNotFoundError: file2.txt does not exist

    +++++++++++++++++++++++++
    WRITE YOUR DOCTESTS BELOW
    +++++++++++++++++++++++++
    >>> loadFile('yooo.txt')
    Traceback (most recent call last):
        ...
    FileNotFoundError: yooo.txt does not exist
    >>> loadFile('fil1.txt')
    Traceback (most recent call last):
        ...
    FileNotFoundError: fil1.txt does not exist
    >>> loadFile('12345.jpeg')
    Traceback (most recent call last):
        ...
    FileNotFoundError: 12345.jpeg does not exist
    """
    ## YOUR CODE HERE ##
    try:
        r = open(filename)
        return 'File loaded'
    except:
        raise FileNotFoundError('{} does not exist'.format(filename))


## Question 3.1 ##

def recursive_triangle(n):
    """
    Creates a triangle structure with * characters. The triangle has n
    levels, each level has one more element than the previous. n is a
    positive integer, no validation is required.
    Parameters: n (int), positive integer
    Returns: triangle string (str)
    Restrictions. This function should be recursive.
    >>> print(recursive_triangle(1))
    *
    >>> print(recursive_triangle(2))
    *
    **
    >>> print(recursive_triangle(3))
    *
    **
    ***

    +++++++++++++++++++++++++
    WRITE YOUR DOCTESTS BELOW
    +++++++++++++++++++++++++
    >>> print(recursive_triangle(0))
    <BLANKLINE>
    >>> print(recursive_triangle(4))
    *
    **
    ***
    ****
    >>> print(recursive_triangle(10))
    *
    **
    ***
    ****
    *****
    ******
    *******
    ********
    *********
    **********
    """
    ## YOUR CODE HERE ##
    if n == 0:
        return ""
    if n == 1:
        return "*"
    else:
        return recursive_triangle(n - 1)+"\n"+ "*"*n

## Question 3.2 ##

def triangle_patterns(n, pattern_count):
    """
    Creates a triangle pattern with * characters. Each triangle has n
    levels, there are pattern_count total triangles. All inputs are
    positive integers, no input validation required.
    Parameters: n, pattern count (int), positive integers
    Returns: triangle string (str)
    Restrictions. This function should be recursive.
    >>> print(triangle_patterns(3, 1))
    *
    **
    ***
    >>> print(triangle_patterns(3, 2))
    *
    **
    ***
    ***
    **
    *
    >>> triangle_patterns(3, 3)
    '*\\n**\\n***\\n***\\n**\\n*\\n*\\n**\\n***'
    >>> triangle_patterns(3, 4)
    '*\\n**\\n***\\n***\\n**\\n*\\n*\\n**\\n***\\n***\\n**\\n*'

    +++++++++++++++++++++++++
    WRITE YOUR DOCTESTS BELOW
    +++++++++++++++++++++++++
    >>> print(triangle_patterns(2, 0))
    None
    >>> print(triangle_patterns(2, 1))
    *
    **
    >>> print(triangle_patterns(2, 2))
    *
    **
    **
    *
    """
    ## YOUR CODE HERE ##
    if pattern_count == 1:
        return recursive_triangle(n)
    if pattern_count == -1:
        return recursive_triangle(n)[::-1]
    if pattern_count < 0:
        return  recursive_triangle(n)[::-1] +"\n"+triangle_patterns(n, -pattern_count-1)
    if pattern_count > 0:
        return  recursive_triangle(n) +"\n"+triangle_patterns(n, -pattern_count+1)


## Question 4 ##

## This question's implementation will be done in hw09_card.py

## Question 5.1 ##
double_dashes = 2
end_case = 2
def full_triangle(n, space_count = 0):
    """
    Creates a triangle structure as shown in the doctests. The triangles have
    n - 1 levels. space_count is a helper variable used to help with spacing
    of the triangle. Assume n >= 2, and space_count >= 0. All inputs are
    integers. No input validation is required.
    Parameters: n, space count (int), integers. n >= 1, space_count >= 0.
    Returns: triangle string (str)
    Restrictions. You should use recursion in this question.
    >>> print(full_triangle(2)) # The smallest value we can have
    OO
    >>> print(full_triangle(3))
    -OO-
    OOOO
    >>> print(full_triangle(5))
    ---OO---
    --OOOO--
    -OOOOOO-
    OOOOOOOO
    >>> full_triangle(6)
    '----OO----\\n---OOOO---\\n--OOOOOO--\\n-OOOOOOOO-\\nOOOOOOOOOO'

    +++++++++++++++++++++++++
    WRITE YOUR DOCTESTS BELOW
    +++++++++++++++++++++++++
    >>> print(full_triangle(4))
    --OO--
    -OOOO-
    OOOOOO
    >>> print(full_triangle(6))
    ----OO----
    ---OOOO---
    --OOOOOO--
    -OOOOOOOO-
    OOOOOOOOOO

    """
    ## YOUR CODE HERE ##
    space_count += 1
    if n == end_case:
        return 'O' * space_count * double_dashes
    else:
        return '-' * (n - double_dashes) + 'O' * space_count * \
        double_dashes + '-' * (n - double_dashes) + '\n' + \
        full_triangle(n-1, space_count)


## Question 5.2 ##

def diamond_patterns(n, pattern_count, space_count = 0):
    """
    Assume n >= 2, pattern_count >= 1 and space_count >= 0. All inputs are
    integers. No assertion required.
    >>> print(diamond_patterns(2,1))
    OO
    >>> print(diamond_patterns(2,2))
    OO
    OO
    >>> print(diamond_patterns(5,1))
    ---OO---
    --OOOO--
    -OOOOOO-
    OOOOOOOO
    >>> diamond_patterns(4,2)
    '--OO--\\n-OOOO-\\nOOOOOO\\nOOOOOO\\n-OOOO-\\n--OO--'

    +++++++++++++++++++++++++
    WRITE YOUR DOCTESTS BELOW
    +++++++++++++++++++++++++
    >>> print(diamond_patterns(2, 1, 1))
    OOOO
    >>> print(diamond_patterns(4, 1, 1))
    --OOOO--
    -OOOOOO-
    OOOOOOOO
    >>> print(diamond_patterns(3, 2))
    -OO-
    OOOO
    OOOO
    -OO-
    """
    ## YOUR CODE HERE ##
    if pattern_count == 1:
        return full_triangle(n,space_count)
    if pattern_count == -1:
        return full_triangle(n,space_count)[::-1]
    if pattern_count < 0:
        return  full_triangle(n, space_count)[::-1] +"\n" + \
        diamond_patterns(n, -pattern_count-1 ,space_count)
    if pattern_count > 0:
        return  full_triangle(n, space_count) + "\n" + \
        diamond_patterns(n, -pattern_count+1, space_count)
