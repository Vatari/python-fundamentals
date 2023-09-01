def sort_list(nums):
    sorted_list = [int(n) for n in nums]
    sorted_list = sorted(sorted_list)
    return sorted_list


numbers = input().split()
print(sort_list(numbers))
