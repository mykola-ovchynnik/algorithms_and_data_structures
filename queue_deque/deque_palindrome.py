from collections import deque


def is_palindrome(s: str) -> bool:
    s = "".join(s.split()).lower()

    d = deque(s)

    while len(d) > 1:
        if d.popleft() != d.pop():
            return False
    return True


print(is_palindrome("Hello"))
print(is_palindrome("Racecar"))
print(is_palindrome("Was it a car or a cat I saw"))
print(is_palindrome("No lemon, no melon"))
