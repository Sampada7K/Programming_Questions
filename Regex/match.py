# matches a pattern at the beginning of a string

import re

pattern = 'a...s$'
test_string = 'nabyss'
result = re.match(pattern, test_string)

#result = re.search(pattern, test_string)

if result:
    print("Search successful.")
    print(result.group())

else:
    print("Search unsuccessful.")
