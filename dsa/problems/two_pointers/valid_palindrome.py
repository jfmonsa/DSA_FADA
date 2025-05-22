"""
125. Valid Palindrome

A phrase is a palindrome if, after converting all uppercase letters into
lowercase letters and removing all non-alphanumeric characters, it reads
the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.
"""


def isPalindrome(s: str) -> bool:
    s2 = ""
    for ch in s:
        if ch.isalnum():
            s2 += ch.upper()

    l = 0
    r = len(s2) - 1
    while r > l:
        if s2[r] != s2[l]:
            return False
        l += 1
        r -= 1
    return True


if __name__ == "__main__":
    print(isPalindrome("A man, a plan, a canal: Panama"))
    print(isPalindrome("a.k.a"))
