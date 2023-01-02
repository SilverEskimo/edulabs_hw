# Write a Python function that checks whether a passed string is palindrome or not.


def check_if_palindrome(word: str) -> bool:
    if not word == word[-1::-1]:
        return False
    return True


print(check_if_palindrome("palindromemordnilap"))