# List
# access element in list
# l1 = [1, 2, 3, 4, 5, 6, 7]
# print(l1[3])

# length find in list
# l1 = [1, 2, 3, 4, 5, 6, 7]
# print(len(l1))

# l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(l1.pop())
# print(l1)
# print(l1.remove(1))


# l1 =  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(11 in l1)

# nums = [10, 20, 30, 40, 50]
# rev = nums[::-1]
# print(rev)

# l1 = [1, 2, 3, 4, 5]
# sum = 0
# for i in l1:
#     sum += i
# print(sum)

# user = list(input("Enter the number of list : "))
# print(user)
# ******************************************************
# Largest and smallest number in list
# nums = [10, 20, 30, 40, 50]

# largest = nums[0]
# smallest = nums[0]

# for i in nums:
#     if i > largest:
#         largest = i
#     if i < smallest:
#         smallest = i
# print("Larger number : ", largest)
# print("Smaller number : ", smallest)

nums = [10, 20, 30, 40, 50]
print("Largest number : ", max(nums))
print("Smallest number : ", min(nums))