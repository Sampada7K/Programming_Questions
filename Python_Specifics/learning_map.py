def calc_square(num):
    return num*num


def add_nums(num1, num2):
    return num1+num2


num_list = [1,2,3,4,5]
squares = map(calc_square, num_list)
print(f"Type is {type(squares)}")
for sq in squares:
    print(sq, end=" ")
print("\n")

num1_list = (1,2,3,4,5)
num2_list = (1,2,3,4,5)
sums = map(add_nums, num1_list, num2_list)
print(f"Type is {type(sums)}")
for new_sum in sums:
    print(new_sum, end=" ")
print("\n")
