import time
import concurrent.futures


def binary_search(sorted_num_list, num):
    if num > sorted_num_list[-1] or num < sorted_num_list[0]:
        return False
    l_index = 0
    r_index = len(sorted_num_list) - 1

    def helper(sorted_num_list, num, l_index, r_index):
        while l_index <= r_index:
            time.sleep(2)
            mid_pt = (l_index + r_index) // 2
            if sorted_num_list[mid_pt] == num:
                return mid_pt
            else:
                if num < sorted_num_list[mid_pt]:
                    return helper(sorted_num_list, num, 0, mid_pt)
                else:
                    return helper(sorted_num_list, num, mid_pt+1, r_index)
        return False

    return helper(sorted_num_list, num, l_index, r_index)


start_time = time.time()
input_list1 = [1, 2, 4, 5, 7, 9, 10, 11, 13, 30, 55, 70, 90, 99]
input_list2 = [1, 2, 4, 5, 7, 9, 10, 11, 13, 30, 55, 70, 90, 99]

# with concurrent.futures.ThreadPoolExecutor() as executor:
#     num_list = [input_list1, input_list2]
#     nums = [5, 70]
#     results = executor.map(binary_search, num_list, nums)
#     for result in results:
#         print(result)

print(binary_search(input_list1, 5))
print(binary_search(input_list2, 70))

end_time = time.time()

print(f'Finished in {round(end_time-start_time, 3)} seconds.')


