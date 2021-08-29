# Countdown - Create a function that accepts a number as an input. Return a new list that counts down by one, from the number (as the 0th element) down to 0 (as the last element).

from typing_extensions import TypeGuard


def countDown(num):
    newList = []
    for i in range(num, -1, -1):
        newList.append(i)
    return newList
print(countDown(15))

# Print and Return - Create a function that will receive a list with two numbers. Print the first value and return the second.

def printReturn(p,r):
    print(p)
    return r
printReturn(234, 88)
print(printReturn(234,88))

# First Plus Length - Create a function that accepts a list and returns the sum of the first value in the list plus the list's length.

def sumFirstLength(list):
    sum = list[0] + len(list)
    return sum
print(sumFirstLength([10, 2, 2, 3]))

#Values Greater than Second - Write a function that accepts a list and creates a new list containing only the values from the original list that are greater than its 2nd value. Print how many values this is and then return the new list. If the list has less than 2 elements, have the function return False

def comparison(list):
    newList = []
    for i in range(len(list)):
        if(list[1] < list[i]):
            newList.append(list[i])
    print(len(newList))
    if(len(newList) < 2):
        return False
    else:
        return True

print(comparison([1,2,5]))

# This Length, That Value - Write a function that accepts two integers as parameters: size and value. The function should create and return a list whose length is equal to the given size, and whose values are all the given value.

def size_and_value(size, value):
    list = []
    for i in range(size):
        list.append(value)
    return list
print(size_and_value(5, 18))