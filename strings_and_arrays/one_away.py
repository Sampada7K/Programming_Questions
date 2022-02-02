def one_away(str1,str2):
    index1 = 0
    index2 = 0
    mismatch = 0
    len1 = len(str1)
    len2 = len(str2)

    if len1 == len2:
        while index1 < len1:
            if str1[index1] != str2[index2]:
                mismatch += 1
            index1 += 1
            index2 += 1
            if mismatch > 1:
                return False

    elif len1-len2 == 1 or len1-len2 == -1:
        if len1-len2 == -1:
            print("Interchanging strings such that str1 is larger")
            temp = str1
            str1 = str2
            str2 = temp

        while index1 < len1 and index2 < len2:
            if str1[index1] != str2[index2]:
                mismatch += 1
                index1 += 1
            else:
                index1 += 1
                index2 += 1
            if mismatch > 1:
                return False

    else:
        return False

    return True


print(one_away("wab", "awab"))
