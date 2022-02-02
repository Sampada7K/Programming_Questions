def give_highest_product_of_3(int_list):
    if len(int_list) < 3:
        return "error"

    highest_product_of_3 = int_list[0] * int_list[1] * int_list[2]

    if len(int_list) == 3:
        return highest_product_of_3

    highest_product_of_1 = max(int_list[0], int_list[1], int_list[2])
    lowest_product_of_1 = min(int_list[0], int_list[1], int_list[2])
    highest_product_of_2 = max(int_list[0] * int_list[1], int_list[1] * int_list[2], int_list[0] * int_list[2])
    lowest_product_of_2 = min(int_list[0] * int_list[1], int_list[1] * int_list[2], int_list[0] * int_list[2])

    for i in range(3, len(int_list)):
        highest_product_of_3 = \
            max(highest_product_of_3, highest_product_of_2*int_list[i], lowest_product_of_2*int_list[i])
        if i == len(int_list)-1:
            return highest_product_of_3
        highest_product_of_2 = \
            max(highest_product_of_2, highest_product_of_1*int_list[i], lowest_product_of_1*int_list[i])
        lowest_product_of_2 = \
            min(lowest_product_of_2, highest_product_of_1 * int_list[i], lowest_product_of_1 * int_list[i])
        highest_product_of_1 = max(int_list[i], highest_product_of_1)
        lowest_product_of_1 = min(int_list[i], lowest_product_of_1)


integer_list = [-10, -10, 1, 3, 2]
integer_list = [-10, 2, -5, 7, -8, 3]
print(give_highest_product_of_3(integer_list))


