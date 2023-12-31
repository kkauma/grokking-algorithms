def binary_search(list, item):
    low = 0
    high = len(list) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = list[mid]

        if guess == item:
            return mid

        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None


my_list = [11, 25, 36, 47, 58, 69, 77, 85, 92]
result = binary_search(my_list, 77)
print(result)  # 6

my_list2 = [1, 3, 5, 7, 9]
result2 = binary_search(my_list2, 3)
print(result2)  # 1
