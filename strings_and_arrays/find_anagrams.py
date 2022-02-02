

def find_anagram(s, p):
    output_list = []

    for ind in range(len(s)):
        p_list = list(p)

        for i in range(ind, ind+len(p)):
            if ind+len(p) > len(s):
                break

            for j in range(len(p)):
                if s[i] in p_list:
                    p_list.remove(s[i])
                else:
                    break
        if len(p_list) == 0:
            output_list.append(ind)

    return output_list

s1 = "abab"
p1 = "ab"

print(find_anagram(s1, p1))

s2 = "cbaebabacd"
p2 = "abc"
print(find_anagram(s2, p2))

s3 = "abcd"
p3 = "pqr"
print(find_anagram(s3, p3))
