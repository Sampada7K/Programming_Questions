from collections import defaultdict


def if_permutation(string1, string2):
    if len(string1) != len(string2):
        return False
    char_dict = defaultdict(int)
    for char in string1:
        char_dict[char] += 1

    print(char_dict)
    for char in string2:
        if char in char_dict:
            char_dict[char] -= 1
            if char_dict[char] < 0:
                return False
        else:
            return False

    return True


print(if_permutation('sampadm', 'padsama'))
