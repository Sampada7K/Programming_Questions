nums = (num for num in range(5))
print(type(nums))
for num in nums:
    print(num)


def f_nums(input_num):
    for i in range(input_num):
        yield i


for j in f_nums(5):
    print(j)

print(next(f_nums(5)))