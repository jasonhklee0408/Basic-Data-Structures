"""
DSC 20 HW 02
NAME: Jason Lee
PID: A15879338
"""

## Question 1 ##

def convert_1(path):
    """
    Read a file that contains pairs of name and company and convert these
    pairs to a list of tuples.

    >>> convert_1('tests/q1_test1.txt')
    [('Wesley', 'Microsoft'), ('Aaron', 'Microsoft'), ('Aaron', 'Apple'), \
('Judy', 'Microsoft'), ('Judy', 'Facebook')]
    >>> convert_1('tests/q1_test2.txt')
    [('Owen', 'TMobile'), ('Aaron', 'AT&T'), ('Wesley', 'SoftBank'), \
('Owen', 'Qualcomm'), ('Xiang', 'Qualcomm'), ('Wesley', 'AT&T'), \
('Xiang', 'SoftBank'), ('Aaron', 'TMobile')]
    >>> convert_1('tests/q1_test3.txt')
    [('David', 'Intel'), ('David', 'Amazon'), ('Judy', 'Intel'), \
('Judy', 'AMD'), ('Judy', 'Amazon'), ('Aaron', 'Amazon'), \
('Xiang', 'Amazon'), ('Wesley', 'Amazon')]
    >>> convert_1('tests/q1_test4.txt')
    [('Jason', 'Tmobile'), ('Nigel', 'Facebook'), ('Nigel', 'Twitter'), \
('Veronica', 'Verizon'), ('Veronica', 'Cricket'), ('Abby', 'Sprint'), \
('Abby', 'Verizon')]
    >>> convert_1('tests/q1_test5.txt')
    [('Tom', 'Sony'), ('Kathy', 'Sony'), ('Mike', 'Samsung'), ('Kyle', 'Boss')]
    >>> convert_1('tests/q1_test6.txt')
    [('Ethan', 'Dasani'), ('Robert', 'Nestle'), ('Ethan', 'Nestle'), \
('Aaron', 'Arrowhead'), ('Robert', 'Arrowhead')]
    """
    converted_list = []
    open_path = open(path)
    for line in open_path.read().splitlines():
        space = line.find(' ')
        converted_list.append((line[0:space], line[space+1:]))
    open_path.close()
    return converted_list

## Question 2 ##

def convert_2(lst):
    """
    Convert the given list of tuples that contain pairs of names and companies
    to a dictionary that has companies as keys and names that pairs with
    these companies as values.

    >>> convert_2([('Wesley', 'Microsoft'), ('Aaron', 'Microsoft'),\
    ('Aaron', 'Apple'), ('Judy','Microsoft'), ('Judy', 'Facebook')])
    {'Microsoft': ['Wesley', 'Aaron', 'Judy'], 'Apple': ['Aaron'], \
'Facebook': ['Judy']}
    >>> convert_2([('Owen', 'TMobile'), ('Aaron', 'AT&T'), ('Wesley',\
    'SoftBank'), ('Owen', 'Qualcomm'), ('Xiang', 'Qualcomm'),\
    ('Wesley', 'AT&T'), ('Xiang', 'SoftBank'), ('Aaron', 'TMobile')])
    {'TMobile': ['Owen', 'Aaron'], 'AT&T': ['Aaron', 'Wesley'], \
'SoftBank': ['Wesley', 'Xiang'], 'Qualcomm': ['Owen', 'Xiang']}
    >>> convert_2([('David', 'Intel'), ('David', 'Amazon'), ('Judy',\
    'Intel'), ('Judy', 'AMD'), ('Judy', 'Amazon'), ('Aaron',\
    'Amazon'), ('Xiang', 'Amazon'), ('Wesley', 'Amazon')])
    {'Intel': ['David', 'Judy'], 'Amazon': ['David', 'Judy', 'Aaron', \
'Xiang', 'Wesley'], 'AMD': ['Judy']}
    >>> convert_2([('Jason', 'Tmobile'), ('Nigel', 'Facebook'),\
    ('Nigel', 'Twitter'), ('Veronica', 'Verizon'), ('Veronica', 'Cricket'),\
('Abby', 'Sprint'), ('Abby', 'Verizon')])
    {'Tmobile': ['Jason'], 'Facebook': ['Nigel'], 'Twitter': ['Nigel'], \
'Verizon': ['Veronica', 'Abby'], 'Cricket': ['Veronica'], 'Sprint': ['Abby']}
    >>> convert_2([('Tom', 'Sony'), ('Kathy', 'Sony'), \
    ('Mike', 'Samsung'), ('Kyle', 'Boss')])
    {'Sony': ['Tom', 'Kathy'], 'Samsung': ['Mike'], 'Boss': ['Kyle']}
    >>> convert_2([('Ethan', 'Dasani'), ('Robert', 'Nestle'), \
    ('Ethan', 'Nestle'), ('Aaron', 'Arrowhead'), ('Robert', 'Arrowhead')])
    {'Dasani': ['Ethan'], 'Nestle': ['Robert', 'Ethan'], \
'Arrowhead': ['Aaron', 'Robert']}
    """
    directory = {}
    for tuple in lst:
        if tuple[1] in directory.keys():
            directory[tuple[1]].append(tuple[0])
        else:
            directory.setdefault(tuple[1],[])
            directory[tuple[1]].append(tuple[0])
    return directory

## Question 3 ##

MAX_N = 9

def multiplication_chart(n):
    """
    Create a triangle multiplication chart with given size. n will be positive
    integers only. If 1 <= n <= 9, create the chart normally. If n > 9, add
    a notice before creating a chart with n = 9. See the write-up for detailed
    description.

    >>> print(multiplication_chart(3))
    01
    02  04
    03  06  09
    >>> print(multiplication_chart(6))
    01
    02  04
    03  06  09
    04  08  12  16
    05  10  15  20  25
    06  12  18  24  30  36
    >>> print(multiplication_chart(10))
    n = 10 is too hard for me! Why not have n = 9?
    01
    02  04
    03  06  09
    04  08  12  16
    05  10  15  20  25
    06  12  18  24  30  36
    07  14  21  28  35  42  49
    08  16  24  32  40  48  56  64
    09  18  27  36  45  54  63  72  81
    >>> print(multiplication_chart(0.9))
    01
    >>> print(multiplication_chart(100))
    n = 100 is too hard for me! Why not have n = 9?
    01
    02  04
    03  06  09
    04  08  12  16
    05  10  15  20  25
    06  12  18  24  30  36
    07  14  21  28  35  42  49
    08  16  24  32  40  48  56  64
    09  18  27  36  45  54  63  72  81
    >>> print(multiplication_chart(5))
    01
    02  04
    03  06  09
    04  08  12  16
    05  10  15  20  25
    """
    chart = ''
    if n % 1 < 1:
        n = round(n)
    if n <= MAX_N:
        for row in range(1,n+1):
            tally = 0
            for i in range(1,n+1):
                number = row * i
                if number <= MAX_N:
                    number = '0' + str(number)
                    tally += 1
                else:
                    number = str(number)
                    tally += 1
                if tally == row:
                    chart += number
                    break
                else:
                    chart += number + '  '
                    continue
            if row != n:
                chart = chart + '\n'
        return chart
    else:
        for row in range(1,MAX_N+1):
            tally = 0
            for i in range(1,MAX_N+1):
                number = row * i
                if number < MAX_N + 1:
                    number = '0' + str(number)
                    tally += 1
                else:
                    number = str(number)
                    tally += 1
                if tally == row:
                    chart += number
                    break
                else:
                    chart += number + '  '
                    continue
            if row != MAX_N:
                chart = chart + '\n'
        return 'n = ' + str(n) +' is too hard for me! \
Why not have n = 9?\n'+ chart

## Question 4 ##

LEN_ALPHABET = 26

def encrypt(s):
    """
    Encrypt the string by capitalizing all letters, applying Atbash cipher,
    and reverse the string. See the write-up for detailed description.

    >>> encrypt('ABCDefg, HIJKlmn, opqRST, uvwXYZ')
    'ABCDEF ,GHIJKL ,MNOPQRS ,TUVWXYZ'
    >>> encrypt('encrypt encrypt?')
    '?GKBIXMV GKBIXMV'
    >>> encrypt('CsE BaSeMeNt >.<')
    '<.> GMVNVHZY VHX'
    >>> encrypt('Data Science')
    'VXMVRXH ZGZW'
    >>> encrypt('Hi! How are you today? >.<')
    '<.> ?BZWLG FLB VIZ DLS !RS'
    >>> encrypt('tODaY iS A GooD DAy')
    'BZW WLLT Z HR BZWLG'
    """
    encrypted_message = ''
    number_count = ''
    tally = 1
    capitalized = s.upper()
    reverse = ['','Z','Y','X','W','V','U','T','S','R','Q','P',
    'O','N','M','L','K','J','I','H','G','F','E','D','C','B','A']
    alp = ['','A','B','C','D','E','F','G','H','I','J','K','L','M',
    'N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    for i in range(len(capitalized)):
        number_count += capitalized[len(s) - tally]
        tally += 1
    for letter in number_count:
        if letter in alp:
            encrypted_message += reverse[alp.index(letter)]
        else:
            encrypted_message += letter
    return encrypted_message

## Question 5 ##

def sum_some(lst1, num):
    """
    Splits lst1 into subgroups of (equal) size num, and sums the contents of each subgroup.
    Returns the individual sums in a new list. If splitting can't be done properly, \
returns "split not valid"

    >>> sum_some([1, 2, 3, 4, 5, 6], 2)
    [3, 7, 11]
    >>> sum_some([1, 2, 3, 4, 5, 6], 3)
    [6, 15]
    >>> sum_some([1,2,3,4,5,6,7], 3)
    'split not valid'
    >>> sum_some([1,2], 3)
    'split not valid'
    >>> sum_some([],6)
    []
    >>> sum_some([100,200,300], 2)
    'split not valid'
    >>> sum_some([0,5,8,4,2,6], 1)
    [0, 5, 8, 4, 2, 6]
    """
    new_list = []
    index_num = 0
    new_num = int(len(lst1)/num)
    if len(lst1) % num != 0:
        return 'split not valid'
    else:
        for i in range(new_num):
            new_list.append(sum(lst1[index_num:index_num+num]))
            index_num+= num
        return new_list

## Question 6 ##

def subset(lst1, lst2):
    """
    Returns True if lst1 is a subset of lst2. Returns False otherwise.

    >>> subset([1,2], [1,2,3])
    True
    >>> subset([1,2,3,4], [1,2,3])
    False
    >>> subset([], [1])
    True
    >>> subset([1,2,3], [1,2,3])
    True
    >>> subset([1], [])
    False
    >>> subset([1],[1,2])
    True
    >>> subset([4,5], [1,2,3,4,5,6])
    True
    >>> subset([0,1], [1,2,3])
    False
    """
    if len(lst1) == 0:
        return True
    elif len(lst1) > len(lst2):
        return False
    else:
        for i in lst1:
            if i in lst2:
                continue
            else:
                return False
        return True
