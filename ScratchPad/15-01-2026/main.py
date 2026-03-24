def get_lst():
    n = int(input("Enter range : "))
    lst = []
    for i in range(n):
        val = int(input("Enter element : "))
        lst.append(val)
    return lst

my_list = get_lst()
print(my_list)

# def nums(lst):
#     lst1 = []
#     for i in range(lst):
#         val = int(input("Enter elements : "))
#         lst1.append(val)
#     return lst1
# my_list = nums(5)
# print(my_list)

# def nums(lst):
#     lst1 = []
#     for i in range(lst):
#         val = int(input("Enter elements"))
#         list1.append(val)
#     return lst1
# my_num = nums(5)
# print(my_num)

# def nums(lst):
#     print(lst)
# nums([1,2,3])

def nums(lst):
    lst1 = []
    for i in range(lst):
        val = int(input("Enter elements"))
        lst1.append(val)
    return lst1

print(nums(int(input("Enter range value"))))