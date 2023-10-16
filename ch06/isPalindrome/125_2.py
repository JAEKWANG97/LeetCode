from collections import deque
import collections

def isPalindrome(s : str)-> bool:
    strs: deque = collections.deque()
    
    for char in s:
        if char.isalnum():
            strs.append(char.lower())
    
    while len(strs) > 1 :
        if strs.popleft() != strs.pop():
            return False
    
    return True
            