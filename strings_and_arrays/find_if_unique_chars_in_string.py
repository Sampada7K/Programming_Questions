def if_unique_chars_in_string(string1: 'str') -> 'bool':
    """
    :param string1: str
    :return: True if string has unique chars. false otherwise
    """
    string_set = set()
    for char in string1:
        if char in string_set:
            return False
        else:
            string_set.add(char)
    return True


print(if_unique_chars_in_string('Abcd13'))

