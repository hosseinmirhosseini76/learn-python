# ! Accessing Values in Lists
list1 = ['physics', 'chemistry', 1997, 2000]
list2 = [1, 2, 3, 4, 5, 6, 7]
list3 = [[1, 2, 3, 4], [5, 6, 7]]
# print("list1[0]: ", list1[0])
# print("list2[1:5]: ", list2[1:5])
print("list3 : ", list3)

# ! Updating Lists
list_test = ['physics', 'chemistry', 1997, 2000]
# print("Value available at index 2 : ")
# print(list_test[2])
list_test[2] = 2001
# print("New value available at index 2 : ")
# print(list_test[2])

# ! Delete List Elements
deletedList = ['physics', 'chemistry', 1997, 2000]
# print(deletedList)
del deletedList[2]
# print("After deleting value at index 2 : ")
# print(deletedList)

# ! Basic List Operations
listA = [1, 2, 3, 7, 8]
listB = [4, 5, 6, 9, 10]
# print(len(listA))
# print(listA + listB)
# print(listA * 2)
# print(3 in listA)
'''
len([1, 2, 3]) -> 3 -> Length
[1, 2, 3] + [4, 5, 6] -> [1, 2, 3, 4, 5, 6] -> Concatenation
['Hi!'] * 4 -> ['Hi!', 'Hi!', 'Hi!', 'Hi!'] -> Repetition
3 in [1, 2, 3] -> True-> Membership
for x in [1, 2, 3]: print x, -> 1 2 3 -> Iteration
'''
# ! Indexing, Slicing, and Matrix's
# print(listA[2])
# print(listA[-2])
# print(listA[1:])

# ! Built-in List Functions & Methods
aTuple = (123, 'xyz', 'zara', 'abc')
aList = list(aTuple)
# print("List elements : ", aList)
# print(len(aList))
'''
1	len(list)
Gives the total length of the list.
2	max(list)
Returns item from the list with max value.
3	min(list)
Returns item from the list with min value.
4	list(seq)
Converts a tuple into list.
'''
