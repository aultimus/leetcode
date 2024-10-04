# https://leetcode.com/problems/palindrome-number/description/


def is_palindrome(x):
    s = str(x)

    # if its odd we don't care about the middle value
    for i in range(0, len(s) // 2):
        if s[i] != s[len(s) - 1 - i]:
            return False
    return True


def test_1():
    assert is_palindrome(121) is True


def test_2():
    assert is_palindrome(-121) is False


def test_3():
    assert is_palindrome(10) is False


def test_4():
    assert is_palindrome(10455401) is True


def test_5():
    assert is_palindrome(2945492) is True
