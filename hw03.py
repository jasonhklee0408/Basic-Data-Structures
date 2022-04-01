"""
DSC 20 HW 03
NAME: Jason Lee
PID: A15879338
"""

from math import isclose

## Question 1 ##

def order_scores(student_ids, student_scores, student_hours_worked):
    """
    Orders elements of student_ids, student_scores, and student_hours_worked,
    according to the contents of student_scores (descending order)

    >>> order_scores(['Work','Hard','Get','A'],[100, 80, 90, 70],[10,12,13,10])
    {'Work': (100, 10), 'Get': (90, 13), 'Hard': (80, 12), 'A': (70, 10)}
    >>> order_scores(['A1','A2','A3'],[90, 27, 56],[9,10, 6])
    {'A1': (90, 9), 'A3': (56, 6), 'A2': (27, 10)}
    >>> order_scores(['A1','A2','A3'],[90.4, 27],[9,10, 6])
    Traceback (most recent call last):
    ...
    AssertionError
    >>> order_scores(['A1','A2','A3'],[90, 27, 80],[9,10, "hello!!"])
    Traceback (most recent call last):
    ...
    AssertionError

    +++++++++++++++++++++++++
    >>> order_scores(['beta','phil','alex'],[10, 20, 90, 70],[2,3,14,9])
    Traceback (most recent call last):
    ...
    AssertionError
    >>> order_scores(['Paul','Nigel','phil',1],[50, 70, 90, 30],[5,7,10,4])
    Traceback (most recent call last):
    ...
    AssertionError
    >>> order_scores(['Paul','Nigel','phil','paula'],[50, 70, 90, 30],[5,7,10,4])
    {'phil': (90, 10), 'Nigel': (70, 7), 'Paul': (50, 5), 'paula': (30, 4)}

    +++++++++++++++++++++++++

    """
    assert len(student_ids) == len(student_scores) == len(student_hours_worked)
    for i in student_scores:
        assert isinstance(i, int)
    for i in student_hours_worked:
        assert isinstance(i, int)
    for i in student_ids:
        assert isinstance(i, str)

    order_dict = {}
    sorted_list = sorted(list(zip(student_scores, \
    student_ids, student_hours_worked)), reverse = True)
    sorted_list_nonameme = sorted(list(zip(student_scores, student_hours_worked)), reverse = True)
    sorted_ids = []
    for i in range(0, len(sorted_list)):
        sorted_ids.append(sorted_list[i][1])
    for i in range(0, len((student_ids))):
        order_dict[sorted_ids[i]] = sorted_list_nonameme[i]

    return order_dict

## Question 2 ##

def word_length_count(book):
    """
    Returns a dictionary containing the count of each length of word
    E.g. how many words total of length 1, 2, 3...?

    This function takes in a string book, which is a file name
    string. The function reads the file with the argument string
    and returns a dictionary where the keys are the length of words
    and the values are the number of words of that length. The keys
    should be sorted in ascending order.

    >>> word_length_count('War_and_Peace_no_punc.txt')[6]
    48342
    >>> word_length_count('War_and_Peace_no_punc.txt')[15]
    254
    >>> word_length_count('War_and_Peace_no_punc.txt')[23]
    2

    +++++++++++++++++++++++++
    >>> word_length_count('War_and_Peace_no_punc.txt')[4]
    97791
    >>> word_length_count('War_and_Peace_no_punc.txt')[10]
    11155
    >>> word_length_count('War_and_Peace_no_punc.txt')[13]
    1572

    +++++++++++++++++++++++++

    """
    open_file = open(book)
    letters_dict = {}
    listed_string = str(open_file.read()).split()
    for i in listed_string:
        wordlength = len(i)
        if wordlength not in letters_dict.keys():
            letters_dict[wordlength] = 1
        else:
            letters_dict[wordlength] += 1
    open_file.close()
    return letters_dict

## Question 3 ##

def counting_spaces(list_of_strings):
    """
    >>> test = ["s t r i n g ", 'nospace', 'one space']
    >>> counting_spaces(test)
    [True, True, 1]

    >>> test2 = ["two spac es", "thr ee spa ces", "nospaces"]
    >>> counting_spaces(test2)
    [2, True, True]

    +++++++++++++++++++++++++
    >>> counting_spaces(['100', 't h e', 'a'])
    [True, 2, True]
    >>> counting_spaces(['', 'h i', 'go od mor ning'])
    [True, 1, True]
    >>> counting_spaces(['h i ', 'h o w', 'are', 'y ou'])
    [2, 2, True, 1]

    +++++++++++++++++++++++++

    """
    return [True if i.count(' ')%3==0 else i.count(' ')for i in list_of_strings]


## Question 4 ##

def create_trigrams(input_file, starting_words, num_words):
    """read in the input text, create a dictionary of trigrams, generate
    a new story based on the sequence of words starting a pair of words

    >>> create_trigrams("data/sherlock_small.txt", "one night", 10)
    'one night it was on the twentieth of march 1888'

    >>> create_trigrams("data/sherlock_small.txt", "i was", 10)
    'i was returning from a journey to a patient for'

    >>> create_trigrams("data/sherlock_small.txt", "Holmes Sherlock", 10)
    Traceback (most recent call last):
    ...
    AssertionError

    +++++++++++++++++++++++++
    >>> create_trigrams("data/sherlock_small.txt", "Holmes Sherlock", 1)
    Traceback (most recent call last):
    ...
    AssertionError
    >>> create_trigrams("data/sherlock_small.txt", "i was", 3)
    'i was returning'
    >>> create_trigrams("data/sherlock_small.txt", "night", 5)
    Traceback (most recent call last):
    ...
    AssertionError

    +++++++++++++++++++++++++

    """
    shift_by_2 = 2
    open_file = open(input_file)
    read_file = list(str(open_file.read()).lower().split(' '))
    start = 0
    end = start + 1
    word_dict = {}
    output = ''
    for i in range(len(read_file)-shift_by_2):
        word_dict[read_file[start]+ ' '+read_file[end]] = read_file[end+1]
        start += 1
        end += 1
    assert starting_words in word_dict
    key_list = list(word_dict.keys())
    list_index = key_list.index(starting_words)
    output += starting_words + " "
    for i in range(num_words-shift_by_2):
        output += word_dict[key_list[list_index]]
        list_index +=1
        if i != num_words-shift_by_2-1:
            output += ' '
    return output

## Question 5 ##

DELTA = 0.0001
def newton_sqrt(n):
    """
    >>> newton_sqrt(4)
    1
    >>> newton_sqrt(1)
    5
    >>> newton_sqrt(2)
    4

    +++++++++++++++++++++++++
    >>> newton_sqrt('hi')
    Traceback (most recent call last):
    ...
    AssertionError
    >>> newton_sqrt(3)
    4
    >>> newton_sqrt('4')
    Traceback (most recent call last):
    ...
    AssertionError

    +++++++++++++++++++++++++

    """
    assert isinstance(n, int)
    DELTA = 0.0001
    square = 2
    halve_divider = 2
    prediction = 0
    tally = 1
    first_test = n/halve_divider

    if isclose(n, first_test**square, abs_tol = DELTA) == True:
        return 1
    else:
        while isclose(n, prediction**square, abs_tol = DELTA) == False:
            if tally == 1:
                prediction = (first_test+(n/first_test))*(1/halve_divider)
                tally +=1
                if isclose(n, prediction**square, abs_tol = DELTA)==True:
                    break
            else:
                prediction = (1/halve_divider)*(prediction+(n/prediction))
                tally +=1
                if isclose(n, prediction**square, abs_tol = DELTA)==True:
                    break
    return tally

## Question 6.1 ##

B = 'O'
W = ' '

def list_to_pixel(file_path, filename):
    """
    >>> list_to_pixel("data/list0.txt","graph.txt")
    >>> with open ("graph.txt", "r") as f:
    ...     print(f.readline())
      OOOO
    <BLANKLINE>
    >>> f1 = open("expected_graph.txt", "r")
    >>> f2 = open("graph.txt", "r")
    >>> f1.read() == f2.read()
    True
    >>> f1.close()
    >>> f2.close()

    +++++++++++++++++++++++++
    WRITE YOUR DOCTESTS BELOW
    +++++++++++++++++++++++++

    """

    interpreted_file = list(open(file_path).read().splitlines())
    data_list = []
    int_lst = []
    for n in range(len(interpreted_file)):
        data_list.append(interpreted_file[n].split(','))
    for n in data_list:
        int_lst.append([int(i) for i in n])
    for l in int_lst:
        start = 0
        end = 1
        with open(filename, 'w') as f:
            for n in l:
                if l.index(n, start, end)%2 != 0:
                    f.write('O'*n)
                    start +=1
                    if end == len(l):
                        end = end
                    else:
                        end += 1
                else:
                    f.write(' '*n)
                    start +=1
                    if end == len(l):
                        end = end
                    else:
                        end += 1
            f.write('\n')
            f.close()


## Question 6.2 ##

def pixel_to_list(pixel):
    """
    >>> pixel0="O OO OOOO OO O\\n"
    >>> pixel_to_list(pixel0)
    [[0, 1, 1, 2, 1, 4, 1, 2, 1, 1]]


    >>> with open("data/pixel_art.txt",'r') as infile:
    ...     pixel1 = infile.readlines()
    >>> pixel1 = ''.join(pixel1)
    >>> pixel_to_list(pixel1)
    [[2, 4, 2], [1, 2, 2, 2, 1], [0, 2, 4, 2], [0, 1, 6, 1], \
[0, 1, 6, 1], [0, 2, 4, 2], [1, 2, 2, 2, 1], [2, 4, 2]]

    +++++++++++++++++++++++++
    >>> pixel_to_list("O OO OOO OOOO\\n")
    [[0, 1, 1, 2, 1, 3, 1, 4]]
    >>> pixel_to_list("OOOO\\n")
    [[0, 4]]
    >>> pixel_to_list("O O OOO OO\\n")
    [[0, 1, 1, 1, 1, 3, 1, 2]]

    +++++++++++++++++++++++++

    """
    total_list = []

    if pixel == '':
        total_list = pixel_list

    pixel_splitted = pixel.split('\n')
    pixel_splitted_list = list(filter(('').__ne__, pixel_splitted))
    for i in pixel_splitted_list:
        pixel_list = []
        if i[0] == ' ':
            for index in range(1, len(i)):
                if i[index-1] != i[index]:
                    pixel_list.append(index-sum(pixel_list))
                if index == len(i)-1:
                    pixel_list.append(len(i)-sum(pixel_list))
        elif i[0] == 'O':
            pixel_list.append(0)
            for index in range(1, len(i)):
                if i[index-1] != i[index]:
                    pixel_list.append(index-sum(pixel_list))
                if index == len(i)-1:
                    pixel_list.append(len(i)-sum(pixel_list))
        total_list.append(pixel_list)
    return total_list

## Question 7 Extra Credit ##

def parameter_debugger(*params):
    """
    Given a list of string values representing function parameter, output a
    tuple with two items: a corrected list of parameter and a boolean value
    telling whether the list has been corrected or not.

    >>> parameter_debugger('first', 'second=30', '*third', '**fourth')
    (['first', 'second=30', '*third', '**fourth'], True)
    >>> parameter_debugger('slope', '*constants', 'intercept')
    (['slope', 'intercept', '*constants'], False)
    >>> parameter_debugger('*tutor', 'professor="Marina"', '*ta', 'me')
    (['me', 'professor="Marina"', '*tutor'], False)

    +++++++++++++++++++++++++
    >>> parameter_debugger('triangle', 'prism=cylinder', '*pyrimid', 'circle')
    (['triangle', 'circle', 'prism=cylinder', '*pyrimid'], False)
    >>> parameter_debugger('*first', 'second=2+2', '*3', 'fourth')
    (['fourth', 'second=2+2', '*first'], False)
    >>> parameter_debugger('2', 'second=1+', '*4-2', '2nd')
    (['2', '2nd', 'second=1+', '*4-2'], False)

    +++++++++++++++++++++++++

    """
    param_list = []
    string_list = []
    original_list = []
    args_list = []
    official_args_list = []
    assert all(isinstance(i,str)for i in params)
    output_lst = []
    for i in params:
        if '**' in i:
            if len(official_args_list) > 0:
                continue
            else:
                official_args_list.append(i)
        elif '*' in i:
            if len(args_list) > 0:
                continue
            else:
                args_list.append(i)
        elif '=' in i:
            original_list.append(i)
        else:
            string_list.append(i)
    param_list += string_list+original_list + args_list + official_args_list
    if param_list == list(params):
        output_lst = [param_list]
        output_lst.append(True)
        return tuple(output_lst)
    else:
        output_lst = [param_list]
        output_lst.append(False)
        return tuple(output_lst)
