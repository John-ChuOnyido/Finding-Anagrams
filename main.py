"""definition of find_anagram function that accept two strings 
and determines if the two strings are anagram"""
def find_anagram(words, anagram):
    """using if else statemnet in a defined function to check 
    whether the sorted function is an anagram, the program 
    returns True if it is an anagram else False if its not."""
    if (sorted(words) == sorted(anagram)):
        return True
    else:
        return False
#collection of data as an input
words= input("please enter your words ")
anagram = input("please enter your anagram check words ")
find_anagram(words, anagram) 
