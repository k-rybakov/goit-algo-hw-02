from collections import deque

def is_palindrome(string):
    queue = deque()

    for char in string.lower().replace(" ", ""):
        queue.append(char)

    while len(queue) > 1:
        if queue.popleft() != queue.pop():
            return False
    
    return True

# Usage:
print(is_palindrome("abccba"))  # True
print(is_palindrome("hello"))  # False
