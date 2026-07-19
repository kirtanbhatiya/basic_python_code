#================================================
#List
#================================================
# data = [10,"kirtan",3.14, True]
# print(data[1])

#================================================
#empty list
#================================================
# a = [], lst = list()

#================================================
#Nested list
#================================================
# matrix = [
#     [1,2],
#     [3,4]
# ]
# print(matrix)

#================================================
#Indexing
#================================================
# fruits = ["mango","banana","apple","pinaple","watermalon"]
# print(fruits)
# fruits = ["mango","banana","apple","pinaple","watermalon"]
# print(fruits[3])

#================================================
#Nagative Indexing
#================================================

# fruits = ["mango","banana","apple","pinaple","watermalon"]
# print(fruits[-5])

#================================================
#slicing[start:stop:step]
#================================================
# data = [1,2,3,4,5,6]
#print(data[:3]) # [1,3]
#print(data[:-2]) # [5,6]
# print(data[0:6:2]) # [1,3,5]
# print(data[::2]) # [1,3,5]
# print(data[::-1]) # [6,5,4,3,2,1]

#================================================
#Update the list
#================================================
# fruits  = ["mango","banana","apple"]
# fruits[1]="warermelon"
# print(fruits)

#================================================
#delete th element
#================================================
# fruits = ["apple","banana","mango"]
# del fruits[1]
# print(fruits)

#================================================
#using index
#================================================
# fruits = ["apple","banana","mango"]
# for i in range(len(fruits)):
#     print(fruits[2])

#================================================
#Using enumirate function
#================================================
# fruits = ["apple","banana","mango"]
# for index, value in enumerate(fruits):
#     print(index, value)

#================================================
#list concet
#================================================
# a = [1,2,3]
# b = [3,5,6]
# print(set(a+b))
# print(a+b)

#================================================
#list repetation
#================================================
# print([1]*5) #[1, 1, 1, 1, 1]
# print(1*[5]) #[5]

#================================================
# Nested list
#================================================
# matrix = [
#     [1,2,3,4],
#     [5,6,7,8]
# ]
# print(matrix[0][2]) #3

#================================================
#built in function in list
#================================================

#================================================
# 1. len() -> return length of List
#================================================

# data = [0,1,2,3,4,5,6,7,8,9]
# print(len(data)) #10

#================================================
# 2.Max() -> return max number of list
#================================================

# data = [0,1,2,3,4,5,6,7,8,9]
# print(max(data)) #9

#================================================
# 2.Min() -> return Min number of list
#================================================

# data = [0,1,2,3,4,5,6,7,8,9]
# print(min(data)) #0

#================================================
# 3.sum() -> return sum of list
#================================================
# data = [0,1,2,3,4,5,6,7,8,9]
# print(sum(data)) #45

#================================================
# 4.sorted() -> return sorted list 
#================================================
# data = [0,6,8,7,4,3,5,1,2,9]
# print(sorted(data)) #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

#================================================
# 5.any -> return value in a list yes or no
#================================================
# data=any([0,False,5])
# print(data) #True

#================================================
# List Method
#================================================

#================================================
# 1. append() ->add the elimant in a list
#================================================
# data = ["chirag","kishan","manish","kirtan"]
# data.append("manthan")
# print(data) #['chirag', 'kishan', 'manish', 'kirtan', 'manthan']

#================================================
# 2. extand() ->add multiple elements from an iterable(like set,tuple)
#================================================
# a = [2,4,1,3,5]
# b = [9,6,8,7,0]

# b.extend(a)
# print(b) #[9, 6, 8, 7, 0, 2, 4, 1, 3, 5]

#================================================
# 3.insert() -> insert the eliment in a list(index, eliment)
#================================================

# data = ["chirag","kishan","manish","kirtan"]
# data.insert(4,"manthan")
# print(data) #['chirag', 'kishan', 'manish', 'kirtan', 'manthan']

#================================================
# 4.remove -> remove the elimant of the list
#================================================

# data = ["chirag","kishan","manish","kirtan"]
# data.remove("kirtan")
# print(data) #["chirag","kishan","manish"]

#================================================
# 5. pop() -> remove the eliment using index and return the list
#================================================

# data = ["chirag","kishan","manish","kirtan"]
# data.pop(2)
# print(data) #["chirag","kishan","kirtan"]

#================================================
# 6. clear() -> clear the list and return empty list
#================================================
# data = ["chirag","kishan","manish","kirtan"]
# data.clear()
# print(data) #[]

#================================================
# 7. index() -> return a index number of list
#================================================

# data =["chirag","kishan","manish","kirtan"]
# print(data.index("kirtan")) #3

#================================================
# 8. count() -> calculate the repetation elimant number
#================================================

# data =["chirag","kishan","manish","kirtan","manish"]
# print(data.count("manish")) #2

#================================================
# 9.sort() -> sort the list 
#================================================
# data = ['a','c','d','b'] # ['a', 'b', 'c', 'd']
# # data = [1,4,3,5,6,2,7,9,8,0] #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# data.sort()
# print(data)

#================================================
#10. reverse() -> reverse the list
#================================================
# data = [1,4,3,5,6,2,7,9,8,0]
# data.reverse()
# print(data) #[0, 8, 9, 7, 2, 6, 5, 3, 4, 1]

#================================================
# 11.copy() ->(Shallow copy) copy the list and return same to same list
#================================================
# data = [1,4,3,5,6,2,7,9,8,0]
# data.copy()
# print(data) #[1,4,3,5,6,2,7,9,8,0]

#================================================
# 12. set() -> remove a duplicate valu from a list
#================================================

#data = [1,2,2,3,4,4,5]
# new_data = list(set(data))
# print(new_data) # [1, 2, 3, 4, 5]

#================================================
#List Comprehension
#================================================
# square=[x*x for x in range(5)]
# print(square) #[0, 1, 4, 9, 16]

#================================================
# print even and odd number
#================================================
# data = [0,1,2,3,4,5,6,7,8,9]
# for x in data:
#     if x%2== 0:
#         print("the number is even")
#     elif x%2!=0:
#         print("the number is odd")

#================================================
#print even number
#================================================
# even=[x for x in range(20) if x%2==0]
# print(even) #[0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

#================================================
# print odd number
#================================================
# odd=[x for x in range(20) if x%2!=0]
# print(odd) #[1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

#================================================
# Nested list comprihention
#================================================

# matrix =[]

# for i in range(3):
#     row = []

#     for j in range(3):
#         row.append(i * j)
#     matrix.append(row)

# print(matrix) #[[0, 0, 0], [0, 1, 2], [0, 2, 4]]

