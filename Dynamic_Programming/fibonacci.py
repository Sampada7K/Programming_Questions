def rec_fibonacci(n):
    if n <= 1:
        return 1
    else:
        return rec_fibonacci(n-2) + rec_fibonacci(n-1)


# for i in range(20):
#     print(rec_fibonacci(i))


def dp_fibonacci(n):
    fib_list = []
    for j in range(n+1):
        if j <= 1:
            fib_list.append(j)
        else:
            fib_list.append(fib_list[j-1]+fib_list[j-2])
    print(fib_list)
    print(len(fib_list))
    return fib_list[n]

print(dp_fibonacci(5))



