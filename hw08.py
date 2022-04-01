from hw08_data import *

## Question 1 ##

CHECK_OUT = "Checking out book failed"
MEMBER_IN_SYSTEM = "Member already in the library System"
MEMBER_NOT_IN_SYSTEM = "Member is not in the library System"

class Library:
    """
    Library class as explained in HW08 writeup.

    >>> sd = Library("San Diego")
    >>> sd.add_book("Harry Potter")
    >>> sd.get_num_books()
    1
    >>> sd.catalog[0]
    'Harry Potter'
    >>> sd.check_out("Harry Potter")
    >>> sd.get_num_books()
    0
    >>> sd.check_out("Tarzan")
    Checking out book failed
    >>> sd.get_location()
    'San Diego'
    >>> la = Library("Los Angeles")
    >>> la.get_location()
    'Los Angeles'
    >>> la.add_member("Harsh")
    >>> la.add_member("Harsh")
    Member already in the library System
    >>> Library.members[0]
    'Harsh'
    >>> sd.remove_member("Harsh")
    >>> sd.remove_member("Harsh")
    Member is not in the library System
    >>> len(Library.members)
    0
    >>> la.add_member("Brian")

    +++++++++++++++++++++++++
    WRITE YOUR DOCTESTS BELOW
    +++++++++++++++++++++++++
    >>> ah = Library('Anaheim Hills')
    >>> ah.get_location()
    'Anaheim Hills'
    >>> ah.add_book('A Tale of 2 Cities')
    >>> ah.add_book('Percy Jackson')
    >>> ah.add_book('1984')
    >>> ah.get_num_books()
    3
    >>> ah.check_out('Harry Potter')
    Checking out book failed
    >>> ah.check_out('1984')
    >>> ah.get_num_books()
    2
    >>> ah.add_member('Brian')
    Member already in the library System
    >>> ah.remove_member('Jason')
    Member is not in the library System
    >>> ah.remove_member('Ethan')
    Member is not in the library System
    """
    ### YOUR CODE GOES HERE ###
    members = []
    def __init__(self, location):
        self.location = location
        self.catalog = []


    def get_location(self):
        return self.location

    def add_book(self,book):
        self.catalog.append(book)

    def get_num_books(self):
        return len(self.catalog)

    def check_out(self, book):
        if book in self.catalog:
            self.catalog.remove(book)
        else:
            print(CHECK_OUT)

    def add_member(self, member):
        if member in self.members:
            print(MEMBER_IN_SYSTEM)
        else:
            self.members.append(member)

    def remove_member(self, member):
        if member in self.members:
            return self.members.remove(member)
        else:
            print(MEMBER_NOT_IN_SYSTEM)


class School_Library(Library):
    """
    School_Library class as explained in HW08 writeup. Inherits from the
    Library class. Used specifically for school libraries.

    >>> geisel = School_Library("San Diego", "UCSD")
    >>> geisel.add_member("Harsh")
    >>> geisel.get_school_name()
    'UCSD'
    >>> School_Library.members
    ['Brian', 'Harsh']
    >>> Library.members
    ['Brian', 'Harsh']
    >>> geisel.members
    ['Brian', 'Harsh']

    +++++++++++++++++++++++++
    WRITE YOUR DOCTESTS BELOW
    +++++++++++++++++++++++++
    >>> oc = School_Library('Orange County', 'Chapman University')
    >>> oc.location
    'Orange County'
    >>> oc.school
    'Chapman University'
    >>> oc.get_school_name()
    'Chapman University'
    >>> oc.add_member('Jinny')
    >>> oc.members
    ['Brian', 'Harsh', 'Jinny']
    >>> oc.remove_member('Jared')
    Member is not in the library System
    >>> len(oc.members)
    3
    >>> oc.add_member('Kyle')
    >>> oc.members
    ['Brian', 'Harsh', 'Jinny', 'Kyle']

    """
    ### YOUR CODE GOES HERE ###
    def __init__(self, location, school):
        self.location = location
        self.school = school

    def get_school_name(self):
        return self.school

## Question 2 ##
max_alp = 26
minus_loop = 97
class Counter:
    """
    Counter class as explained in HW08 writeup.

    >>> c = Counter("marina langlois")
    >>> print(c.counter_array)
    [3, 0, 0, 0, 0, 0, 1, 0, 2, 0, 0, 2, 1, 2, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, \
0, 0, 1]
    >>> print(c.get_count(' '))
    1
    >>> print(c.get_count('!'))
    0
    >>> print(c.get_count('m'))
    1

    +++++++++++++++++++++++++
    WRITE YOUR DOCTESTS BELOW
    +++++++++++++++++++++++++
    >>> ex1 = Counter("Jason Lee")
    >>> print(ex1.counter_array)
    [1, 0, 0, 0, 2, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, \
0, 0, 1]
    >>> print(ex1.get_count('e'))
    2
    >>> print(ex1.get_count('n'))
    1
    >>> print(ex1.get_count('j'))
    1
    >>> ex2 = Counter('DSC is very fun')
    >>> print(ex2.counter_array)
    [0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 2\
, 0, 1, 1, 0, 0, 1, 0, 3]
    >>> print(ex2.get_count('d'))
    1
    >>> print(ex2.get_count('?'))
    0
    >>> print(ex2.get_count('u'))
    1
    """

    ### YOUR CODE GOES HERE ###
    def __init__(self, string):
        self.counter_array = Counter.count_us()
        self.word = string.lower()

        for letter in self.word:
            if letter == ' ':
                self.counter_array[max_alp] += 1
            else:
                self.counter_array[ord(letter)-minus_loop] += 1

    def count_us():
        return [0 for i in range(0,max_alp+1)]

    def get_count(self, letter):
        if letter == " ":
            return self.counter_array[max_alp]
        elif ord(letter) - minus_loop < 0 or ord(letter)- minus_loop > max_alp:
            return 0
        else:
            return self.counter_array[ord(letter)- minus_loop]


## Question 3.1 ##
tie_breaker = 2
skip = 2
def street_fighter_champ(tutors):
    """
    Determines the winner of the street fighter championship. The nested list
    'tutors' shows all the matchups.
    Consider tutor tutor1 = ('Dragon', 10, 10)
    tutor1[1] is the skill level
    tutor1[2] is the tie breaker level. In case skills are tied between two
    tutors, the one with the higher tie breaker score wins. If both skill
    level and tie breaker score is the same, the tutor on the left wins.
    Parameters: tutors(list), nested list of lists representing the tournament
    Returns: winner(tuple) The winner of the tournament, in tuple form.
    Restrictions: You should use recursion.

    >>> tutors1 = [Arda]
    >>> tutors2 = [Yuxuan, Arda]
    >>> tutors3 = [[Yuxuan, Arda],[Etsu, Nabi]]
    >>> tutors4 = [[[Yuxuan, Arda],[Etsu, Nabi]],\
[[Wesley, Cecilia],[Aaron, Prem]]]
    >>> tutors5 = [[[[Yuxuan, Arda],[Etsu, Nabi]],\
[[Wesley, Cecilia],[Aaron, Prem]]], [[[Chase, Sudiksha],[Jonathan, Iman]],\
[[Aragorn, Sauron],[Neo, Morpheus]]]]
    >>> street_fighter_champ(tutors1)
    ('Arda', 5, 10)
    >>> street_fighter_champ(tutors2)
    ('Yuxuan', 6, 5)
    >>> street_fighter_champ(tutors3)
    ('Nabi', 7, 5)
    >>> street_fighter_champ(tutors4)
    ('Wesley', 9, 5)
    >>> street_fighter_champ(tutors5)
    ('Neo', 10, 7)

    +++++++++++++++++++++++++
    WRITE YOUR DOCTESTS BELOW
    +++++++++++++++++++++++++
    >>> example = [[[Arda, Wesley], [Chase, Aaron]],\
 [[Neo, Aragorn], [Sauron, Nabi]]]
    >>> street_fighter_champ(example)
    ('Neo', 10, 7)
    >>> example2 = [[[Arda, Wesley], [Chase, Aaron]], \
[[Neo, Aragorn], [Sauron, Nabi]], [[Cecilia, Morpheus], \
[Iman, Yuxuan]]]
    >>> street_fighter_champ(example2)
    ('Neo', 10, 7)
    >>> example3 = [[[Aragorn, Neo], [Aaron, Nabi]], \
[[Jonathan, Yuxuan], [Cecilia, Sudiksha]], [[Etsu, Wesley],\
[Morpheus, Prem]]]
    >>> street_fighter_champ(example3)
    ('Neo', 10, 7)
    """
    ### YOUR CODE GOES HERE ###
    output_lst = []
    def remove_lists(big_list):
        for i in big_list:
            if type(i) == list:
                remove_lists(i)
            else:
                output_lst.append(i)

    remove_lists(tutors)

    if len(output_lst) == 1:
        return output_lst[0]
    else:
        winners_lst = []
        for i in range(0,len(output_lst)- 1, skip):
            if output_lst[i][1] > output_lst[i+1][1]:
                winners_lst.append(output_lst[i])
            elif output_lst[i][1] < output_lst[i+1][1]:
                winners_lst.append(output_lst[i+1])
            elif output_lst[i][1] == output_lst[i+1][1]:
                if output_lst[i][tie_breaker] > output_lst[i+1][tie_breaker]:
                    winners_lst.append(output_lst[i])
                elif output_lst[i][tie_breaker] < output_lst[i+1][tie_breaker]:
                    winners_lst.append(output_lst[i+1])
                elif output_lst[i][tie_breaker] == output_lst[i+1][tie_breaker]:
                    winners_lst.append(output_lst[i])

    return street_fighter_champ(winners_lst)

## Question 3.2 ##
tie_breaker = 2
skip = 2
def street_fighter_detect_spy(tutors):
    """
    Detect the spy from the street fighter tournament. The worst player wins
    the tournament. ie. lower skill player always wins any matchup. In case of
    skill tie, lower tie breaker score always wins. In case of ties in both,
    the tutor on the right wins.
    Parameters: tutors(list), nested list of lists representing the tournament
    Returns: spy(str) The absolute loser of the tournament, in string form.
    Restrictions: You should use recursion.

    >>> tutors0 = [('Pla3', 4, 1)]
    >>> tutors1 = [[('Pla2', 6, 5), ('Pla1', 5, 10)],[('Pla3', 4, 1),\
('Pla4', 4, 2)]]
    >>> tutors2 = [[[('Pla2', 6, 5), ('Pla1', 5, 10)],[('Pla3', 4, 1),\
('Pla4', 4, 2)]], [[('Pla5', 9, 5), ('Pla8', 8, 3)],[('Pla6', 7, 10),\
('Pla7', 8, 5)]]]
    >>> street_fighter_detect_spy(tutors0)
    'Etsu'
    >>> street_fighter_detect_spy(tutors1)
    'Etsu'
    >>> street_fighter_detect_spy(tutors2)
    'Etsu'

    +++++++++++++++++++++++++
    WRITE YOUR DOCTESTS BELOW
    +++++++++++++++++++++++++
    >>> ex1 = [('Pla8', 8, 3)]
    >>> street_fighter_detect_spy(ex1)
    'Cecilia'
    >>> ex2 = [[('Pla8', 8, 3), ('Pla4', 4, 2)], \
[('Pla3', 4, 1), ('Pla5', 9, 5)]]
    >>> street_fighter_detect_spy(ex2)
    'Etsu'
    >>> ex3 = [[('Pla8', 8, 3)], [('Pla5', 9, 5), ('Pla3', 4, 1)],\
[('Pla2', 6, 5), ('Pla1', 5, 10)]]
    >>> street_fighter_detect_spy(ex3)
    'Etsu'
    """
    ### YOUR CODE GOES HERE ###
    output_lst = []
    def remove_lists(big_list):
        for i in big_list:
            if type(i) == list:
                remove_lists(i)
            else:
                output_lst.append(i)

    def convert_name(tup):
        return secret_dict[str(tup[0])]

    remove_lists(tutors)

    if len(output_lst) == 1:
        return convert_name(output_lst[0])
    else:
        winners_lst = []
        for n in range(0,len(output_lst)- 1, skip):
            if output_lst[n][1] > output_lst[n+1][1]:
                winners_lst.append(output_lst[n+1])
            elif output_lst[n][1] < output_lst[n+1][1]:
                winners_lst.append(output_lst[n])
            elif output_lst[n][1] == output_lst[n+1][1]:
                if output_lst[n][tie_breaker] > output_lst[n+1][tie_breaker]:
                    winners_lst.append(output_lst[n+1])
                elif output_lst[n][tie_breaker] < output_lst[n+1][tie_breaker]:
                    winners_lst.append(output_lst[n])
                elif output_lst[n][tie_breaker] == output_lst[n+1][tie_breaker]:
                    winners_lst.append(output_lst[n+1])

    return street_fighter_detect_spy(winners_lst)


## Question 4 ##

def make_reviews_list(dining_hall, ratings):
    """
    Creates a list of reviews for a particular dining hall given a list of
    ratings.

    Try using list comprehesions!

    >>> make_reviews_list('A', [123])
    [['A', 123]]
    >>> make_reviews_list('B', [0, 1])
    [['B', 0], ['B', 1]]
    >>> make_reviews_list('7th College Dining Hall', [])
    []
    >>> make_reviews_list('Foodworx', ["Best food", 5, ":)", 100, 1, 1, 5])
    [['Foodworx', 'Best food'], ['Foodworx', 5], ['Foodworx', ':)'], \
['Foodworx', 100], ['Foodworx', 1], ['Foodworx', 1], ['Foodworx', 5]]

    +++++++++++++++++++++++++
    WRITE YOUR DOCTESTS BELOW
    +++++++++++++++++++++++++
    >>> make_reviews_list('Panda', ['good', 'bad', 'meh', 'fake'])
    [['Panda', 'good'], ['Panda', 'bad'], \
['Panda', 'meh'], ['Panda', 'fake']]
    >>> make_reviews_list('KFC', [1,'1',2,'5'])
    [['KFC', 1], ['KFC', '1'], ['KFC', 2], ['KFC', '5']]
    >>> make_reviews_list('Subway', [5, 2, 3, 1, 6])
    [['Subway', 5], ['Subway', 2], ['Subway', 3],\
 ['Subway', 1], ['Subway', 6]]
    """
    assert isinstance(dining_hall, str)
    assert isinstance(ratings, list)
    final_list = []
    for i in range(len(ratings)):
        indiv_lst = make_review(dining_hall, ratings[i])
        final_list.append(indiv_lst)
    return final_list


## Question 5 ##

def average_rating(dining_hall, reviews=google_reviews):
    """
    Finds the average rating for a particular dining hall. The list of
    reviews is given as the second parameter. The average rating should be
    returned as its own review.

    >>> average_rating('Canyon Vista')
    2.2
    >>> average_rating('64 Degrees')
    4.2
    >>> average_rating('Foodworx')
    3.4
    >>> average_rating('Pines')
    3.6

    +++++++++++++++++++++++++
    WRITE YOUR DOCTESTS BELOW
    +++++++++++++++++++++++++
    >>> average_rating('OVT')
    4.0
    >>> average_rating('Cafe Ventanas')
    3.4
    >>> average_rating('Subway')
    2.0
    """
    ### YOUR CODE GOES HERE ###
    assert isinstance(dining_hall, str)
    assert isinstance(reviews, list)
    ratings_lst = []
    for i in range(len(reviews)):
        name = get_place(reviews[i])
        if name == dining_hall:
            rating = get_rating(reviews[i])
            ratings_lst.append(rating)
    final_rating = sum(ratings_lst)/len(ratings_lst)
    return final_rating



## Question 6 ##

def better_dining_hall(first, second):
    """
    Returns the name of the better dining hall between the two given
    dining halls. The better dining hall is the dining hall with a higher
    average review.

    >>> better_dining_hall('OVT', 'Pines')
    'OVT'
    >>> better_dining_hall('Canyon Vista', 'Pines')
    'Pines'
    >>> better_dining_hall('Cafe Ventanas', '64 Degrees')
    '64 Degrees'
    >>> better_dining_hall('64 Degrees', 'OVT')
    '64 Degrees'

    +++++++++++++++++++++++++
    WRITE YOUR DOCTESTS BELOW
    +++++++++++++++++++++++++
    >>> better_dining_hall('OVT', 'Cafe Ventanas')
    'OVT'
    >>> better_dining_hall('Subway', 'Pines')
    'Pines'
    >>> better_dining_hall('Foodworx', 'Subway')
    'Foodworx'
    """
    assert isinstance(first, str)
    assert isinstance(second, str)
    avg_rating_1 = average_rating(first)
    avg_rating_2 = average_rating(second)
    if avg_rating_1 > avg_rating_2:
        return first
    elif avg_rating_1 == avg_rating_2:
        return first
    else:
        return second
