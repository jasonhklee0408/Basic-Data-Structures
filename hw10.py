import numpy as np
from stack import Stack

## Question 1 ##
def paren_checker(expression):
    """
    YOU MUST USE YOUR STACK CLASS THAT YOU IMPLEMENTED IN LAB10. Check the
    writeup for details. This function checks whether the pairs and the orders
    of '{', '}', '(','), '[', ']' are correct in a given expression.

    >>> paren_checker("(((]})")
    False
    >>> paren_checker("(")
    False
    >>> paren_checker("(){}[]")
    True
    >>> paren_checker("(   x   )")
    True
    >>> paren_checker("a()b{}c[]d")
    True
    >>> paren_checker("")
    True

    +++++++++++++++++++++++++
    WRITE YOUR DOCTESTS BELOW
    +++++++++++++++++++++++++
    >>> paren_checker('(){}')
    True
    >>> paren_checker('[{this is not a list}]')
    False
    >>> paren_checker('[')
    False
    """
    stacked_expression = Stack(len(expression))
    for i in expression:
        if i == '(' or i == '{' or i == '[':
            stacked_expression.push(i)

    for i in expression[::-1]:
        if i == ')':
            check_pair = stacked_expression.pop()
            if check_pair == "(":
                continue
            else:
                return False
        if i == '}':
            check_pair = stacked_expression.pop()
            if check_pair == "{":
                continue
            else:
                return False
        if i == ']':
            check_pair = stacked_expression.pop()
            if check_pair == "[":
                continue
            else:
                return False
    if len(stacked_expression.list) == 0:
        return True
    else:
        return False

## Question 2 ##
class Queue:
    """
    A queue ADT that dequeues from front and enqueues at rear.

    >>> a=Queue()
    >>> a.enqueue(1)
    >>> a.enqueue(2)
    >>> a.enqueue(3)
    >>> a.enqueue(4)
    >>> a.enqueue(5)
    >>> a.print_queue()
    [ | 1 | 2 | 3 | 4 | 5 | ]
    >>> a.front
    0
    >>> a.rear
    5
    >>> a.data
    array([1, 2, 3, 4, 5, None, None, None, None, None], dtype=object)
    >>> a.capacity
    10
    >>> a.dequeue()
    1
    >>> a.print_queue()
    [ | 2 | 3 | 4 | 5 | ]
    >>> a.front
    1
    >>> a.rear
    5

    >>> a=Queue(10)
    >>> a.capacity
    10

    >>> b=Queue()
    >>> b.dequeue()
    Attempt to dequeue from an empty queue
    >>> b.enqueue(1)
    >>> b.enqueue(max)
    >>> b.print_queue()
    [ | 1 | <built-in function max> | ]
    >>> b.dequeue()
    1
    >>> b.dequeue()
    <built-in function max>
    >>> b.front
    2
    >>> b.rear
    2
    >>> b.dequeue()
    Attempt to dequeue from an empty queue

    +++++++++++++++++++++++++
    WRITE YOUR DOCTESTS BELOW
    +++++++++++++++++++++++++
    >>> ex1 = Queue()
    >>> ex1.enqueue(0)
    >>> ex1.enqueue(2)
    >>> ex1.enqueue(6)
    >>> ex1.print_queue()
    [ | 0 | 2 | 6 | ]
    >>> ex1.front
    0
    >>> ex1.rear
    3
    >>> ex1.data
    array([0, 2, 6, None, None], dtype=object)
    >>> ex1.dequeue()
    0
    >>> ex1.is_full()
    False
    >>> ex1.dequeue()
    2
    >>> ex1.dequeue()
    6
    >>> ex1.is_empty()
    True
    >>> ex1.expand()
    >>> ex1.capacity
    10
    >>> ex2 = Queue()
    >>> ex2.enqueue(1)
    >>> ex2.enqueue(3)
    >>> ex2.enqueue(5)
    >>> ex2.enqueue(7)
    >>> ex2.enqueue(9)
    >>> ex2.enqueue(11)
    >>> ex2.rear
    6
    >>> ex2.capacity
    10
    >>> ex2.dequeue()
    1
    >>> ex2.dequeue()
    3
    >>> ex2.front
    2
    >>> ex2.num_elems
    4
    >>> ex2.data
    array([None, None, 5, 7, 9, 11, None, None, None, None], dtype=object)
    >>> ex2.expand()
    >>> ex2.capacity
    20
    >>> ex2.is_full()
    False
    >>> ex2.is_empty()
    False
    >>> ex2.print_queue()
    [ | 5 | 7 | 9 | 11 | ]
    >>> ex3 = Queue()
    >>> ex3.enqueue(2)
    >>> ex3.enqueue(5)
    >>> ex3.enqueue(8)
    >>> ex3.enqueue(11)
    >>> ex3.enqueue(14)
    >>> ex3.enqueue(17)
    >>> ex3.enqueue(20)
    >>> ex3.front
    0
    >>> ex3.rear
    7
    >>> ex3.num_elems
    7
    >>> ex3.capacity
    10
    >>> ex3.data
    array([2, 5, 8, 11, 14, 17, 20, None, None, None], dtype=object)
    >>> ex3.dequeue()
    2
    >>> ex3.dequeue()
    5
    >>> ex3.expand()
    >>> ex3.capacity
    20
    >>> ex3.is_full()
    False
    >>> ex3.is_empty()
    False
    >>> ex3.print_queue()
    [ | 8 | 11 | 14 | 17 | 20 | ]
    """

    def __init__(self, capacity = 5):
        """
        >>> q = Queue()
        """
        # Your Code Here
        self.front = 0
        self.rear = 0
        self.num_elems = 0
        self.capacity = capacity
        self.data = np.array([None for i in range(capacity)])

    def dequeue(self):
        """
        dequeues from the front of the queue

        >>> q = Queue()
        >>> q.dequeue()
        Attempt to dequeue from an empty queue
        """
        # Your Code Here
        if self.is_empty() != True:
            self.front += 1
            pop_elem = self.data[self.front - 1]
            self.data[self.front - 1] = None
            self.num_elems -= 1
            return pop_elem
        else:
            print('Attempt to dequeue from an empty queue')

    def enqueue(self, elem):
        """
        enqueue at the rear of the queue
        >>> q = Queue()
        >>> q.enqueue("a")
        """
        # Your Code Here
        if self.is_full() == False:
            self.data[self.rear] = elem
            self.num_elems += 1
            self.rear += 1
            if self.is_full() == True:
                self.expand()
        else:
            self.expand()
            self.data[self.rear] = elem
            self.num_elems += 1
            self.rear += 1

    def expand(self):
        """
        expand the capacity of the circular array when needed
        >>> q = Queue()
        >>> q.capacity
        5
        >>> q.expand()
        >>> q.capacity
        10
        """
        # Your Code Here
        self.data = np.concatenate((self.data, np.array([None for i in range(self.capacity)])))
        self.capacity = self.capacity + self.capacity

    def is_full(self):
        """
        checks if circular array is full
        >>> q = Queue()
        >>> for i in range(4): q.enqueue(i)
        >>> q.data
        array([0, 1, 2, 3, None], dtype=object)
        >>> q.is_full()
        False
        """
        # Your Code Here
        for i in self.data[self.front:]:
            if i == None:
                return False
            else:
                continue
        return True

    def is_empty(self):
        """
        checks if circular array is full
        >>> q = Queue()
        >>> q.is_empty()
        True
        """
        # Your Code Here
        for i in self.data:
            if i != None:
                return False
            else:
                continue

        return True

    def print_queue(self):
        """
        prints out queue in a human-friendly format
        >>> q = Queue()
        >>> for i in range(5): q.enqueue(i)
        >>> q.print_queue()
        [ | 0 | 1 | 2 | 3 | 4 | ]
        >>> p = Queue()
        >>> p.print_queue()
        []
        """
        # Your Code Here
        opening = '['
        middle = ''
        closing = ']'
        for i in range(len(self.data)):
            if self.data[i] == None:
                continue
            elif i != self.rear-1:
                middle += ' | ' + str(self.data[i])
            else:
                middle += ' | ' + str(self.data[i]) + ' | '
        print(opening + middle + closing)

## Question 3 ##
def cursed_carousel(n, m):
    """
    m is the number of customers in line
    n is the number of customers sent to the back of the line
    Return the number of the customer which is last to be served

    >>> cursed_carousel(6,3)
    3
    6
    4
    2
    5
    1
    >>> cursed_carousel(-1,-2)
    m and n should be positive!
    >>> cursed_carousel('5','1')
    Invalid input data type.

    +++++++++++++++++++++++++
    WRITE YOUR DOCTESTS BELOW
    +++++++++++++++++++++++++
    >>> cursed_carousel(10,'2')
    Invalid input data type.
    >>> cursed_carousel(10, 10-11)
    m and n should be positive!
    >>> cursed_carousel(10, 2)
    2
    4
    6
    8
    10
    3
    7
    1
    9
    5
    """
    # Your Code Here
    try:
        assert m > 0
        assert n > 0
        convert_queue = Queue()
        for i in range(1,n+1):
            convert_queue.enqueue(i)
        for i in range(n):
            for i in range(m-1):
                convert_queue.enqueue(convert_queue.data[convert_queue.front])
                extra_elem = convert_queue.dequeue()
            print(convert_queue.dequeue())
    except AssertionError:
        print('m and n should be positive!')
    except TypeError:
        print('Invalid input data type.')




## Question 4 (Extra Credit) ##
def find_best_farm(land_plots):
    """
    Finds the best farm given a list of land plots.

    Restrictions: You must use a stack and your algorithm must run
    in O(n) time. Make sure to fill out extra_credit.txt to get credit.

    >>> find_best_farm([3, 2, 3])
    6
    >>> find_best_farm([1, 2, 3, 4, 5])
    9
    >>> find_best_farm([5, 4, 3, 2, 1])
    9

    +++++++++++++++++++++++++
    WRITE YOUR DOCTESTS BELOW
    +++++++++++++++++++++++++
    """
    # Your Code Here
