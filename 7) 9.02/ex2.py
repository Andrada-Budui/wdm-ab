#####################
## -- PROBLEM 1 -- ##
#####################

# Given a list of integers, return True if the sequence of numbers 1, 2, 3
# appears in the list somewhere.

# For example:


def array_check(nums):
    for index in range(len(nums) - 2):
        if (
                nums[index] == 1
                and nums[index + 1] == 2
                and nums[index + 2] == 3
        ):
            return True
    else:
        return False


print(array_check([1, 1, 2, 3, 1]))
print(array_check([1, 3, 1, 2, 4, 1]))
print(array_check([1, 1, 2, 1, 2, 3]))

#####################
## -- PROBLEM 2 -- ##
#####################

# Given a string, return a new string made of every other character starting
# with the first, so "Hello" yields "Hlo".

# For example:


def string_bits(string):
    return string[::2]  # string slicing


print(string_bits('Hello'))
print(string_bits('Hi'))
print(string_bits('ssaaaaaaaaaaaarrppiilliiiiiiiiiiiiiiiii'))


#####################
## -- PROBLEM 3 -- ##
#####################

# Given two strings, return True if either of the strings appears at the very end
# of the other string, ignoring upper/lower case differences (in other words, the
# computation should not be "case sensitive").
#
# Examples:
#
def end_other(a, b):
    a = a.lower()
    b = b.lower()
    if len(a)<len(b):
        if a == b[(len(b)-len(a)):]:
            return True
    elif len(a)>len(b):
        if b == a[(len(a)-len(b)):]:
            return False
    else:
        if a == b:
            return True

print(end_other('Hiabc', 'abc'))
print(end_other('AbC', 'HiaBc'))
print(end_other('abc', 'abXabc'))

#####################
## -- PROBLEM 4 -- ##
#####################

# Given a string, return a string where for every char in the original,
# there are two chars.


def doubleChar(str):
    return ''.join([elem*2 for elem in str])


print(doubleChar('The'))
print(doubleChar('AAbb'))
print(doubleChar('Hi-There'))


#####################
## -- PROBLEM 5 -- ##
#####################

# Read this problem statement carefully!

# Given 3 int values, a b c, return their sum. However, if any of the values is a
# teen -- in the range 13-19 inclusive -- then that value counts as 0, except 15
# and 16 do not count as a teens. Write a separate helper "def fix_teen(n):"that
# takes in an int value and returns that value fixed for the teen rule.
#
# In this way, you avoid repeating the teen code 3 times (i.e. "decomposition").
# Define the helper below and at the same indent level as the main no_teen_sum().
# Again, you will have two functions for this problem!
#
# Examples:
#


def no_teen_sum(a, b, c):
    if a in range(13,15) or a in range(17,20):
        a = fix_teen(a)
    elif b in range(13,15) or b in range(17,20):
        b = fix_teen(b)
    elif c in range(13,15) or c in range(17,20):
        c = fix_teen(c)
    return a+b+c
    

def fix_teen(n):
    return 0

print(no_teen_sum(1, 2, 3))
print(no_teen_sum(2, 13, 1))
print(no_teen_sum(2, 1, 15))

#####################
## -- PROBLEM 6 -- ##
#####################

# Return the number of even integers in the given array.
#
# Examples:
#


def count_evens(nums):
    nr = 0
    for elem in nums:
        if (elem % 2) == 0:
            nr+=1
    return nr

print(count_evens([2, 1, 2, 3, 4]))
print(count_evens([2, 2, 0]))
print(count_evens([1, 3, 5]))
