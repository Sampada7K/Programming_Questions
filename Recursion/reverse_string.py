# def print_reverse(str_a):
#     def print_reverse_helper(str_r, index):
#         if index == len(str_r) - 1:
#             print(str_r[index])
#             return
#
#         print_reverse_helper(str_a, index + 1)
#         print(str_r[index])
#
#     n = len(str_a)
#     index = 0
#     if n == 0:
#         print(str_a)
#     print_reverse_helper(str_a, index)


def reverse_string(str_a):
    def helper(str_1, index):
        if index == len(str_1) - 1:
            return str_1[index]
        return helper(str_1, index+1) + str_1[index]

    n = len(str_a)
    index = 0
    if n == 0:
        return str_a
    return str_a, helper(str_a, index)







# ip_str = ""
# ip_str = "a"
ip_str = "sampada"
# print_reverse(ip_str)
print(reverse_string(ip_str))
