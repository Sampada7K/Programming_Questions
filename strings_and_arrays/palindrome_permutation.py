from collections import defaultdict


def permutation_palindrome(string1):
    char_count = defaultdict(int)
    for char in string1:
        if char.lower().isalpha():
            char_count[char] += 1
        else:
            print("String contains numbers, spaces or special characters.")
            return False
    print(char_count)

    odd = 0
    for value in char_count.values():
        if value % 2 != 0:
            odd += 1
        if odd > 1:
            return False

    return True


print(permutation_palindrome("123"))
