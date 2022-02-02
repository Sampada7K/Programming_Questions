def urlify(str1, true_len):

    str1_index = len(str1) - 1
    for i in range(true_len-1, -1, -1):
        if str1_index == i:
            print("No more space")
            break

        if str1[i] == " ":
            str1[str1_index] = "0"
            str1[str1_index-1] = "2"
            str1[str1_index-2] = "%"
            str1_index -= 3

        else:
            str1[str1_index] = str1[i]
            str1_index -= 1

    return str1


print(urlify(['M','r','J','o','h','n','S','m','i','t','h',' ',' ',' ',], 12))
