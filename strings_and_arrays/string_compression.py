def string_compression(original_string):
    index = 0
    compressed_string = original_string[0]
    count = 1

    while index+1 < len(original_string):
        if original_string[index] == original_string[index+1]:
            count += 1
        else:
            compressed_string = compressed_string + str(count)
            compressed_string = compressed_string + original_string[index+1]
            count = 1
        index += 1

    compressed_string = compressed_string + str(count)

    print(compressed_string)

    if len(original_string) <= len(compressed_string):
        return original_string
    else:
        return compressed_string


print(string_compression("aabbccdd"))

print(''.join(['1','1','1']))
