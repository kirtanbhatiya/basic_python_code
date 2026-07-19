#==========================
# simple Ser
#==========================
# students = {"rahul","mihir","het","kishan","rahul","mihir"}
# print(students) #{'het', 'rahul', 'mihir', 'kishan'}

#==========================
# empty set
#==========================

# s = set()
# print(s) #set()

#==========================
# set with values
#==========================

# numbers = {10,20,30,40}
# print(numbers) #{40, 10, 20, 30}

#==========================
# mixed datatype with set
#==========================

# st = {"kirtan",20,True,3.14}
# print(st) #{'kirtan', 3.14, 20, True}

#==========================
# set in for loop
#==========================

# fruits = {"apple","mango","banana","watermalon"}
# for i in fruits:
#     print(i)

#==========================
# Membership operator
#==========================

# fruits = {"apple","mango","banana","watermalon"}
# print("apple" in fruits) # True

#==========================
# SET METHODS :
#==========================

#==========================
# 1. add(): # add the element in the set
#==========================

# s = {1,2,3,4}
# s.add(5)
# print(s)

#==========================
# 2. updatae() # multiple iterable add in the set
#==========================

# s = {1,2,3,4}
# s.update([6,7])
# print(s) # {1, 2, 3, 4, 6, 7}

#==========================
# 3. remove() # delete the value from set
#==========================

# s = {1,2,3,4,5}
# s.remove(5)
# print(s) #{1, 2, 3, 4}

#==========================
# 4. discard() # remove the element but element not in a set not give error.
#==========================

# s = {1,2,3,4,5}
# s.discard(6)
# print(s) #{1, 2, 3, 4, 5}

#==========================
# 5. pop() # random element ko remove karta hai.
#==========================

# s = {1,2,3,4,5}
# s.pop()
# print(s) #{2, 3, 4, 5}

#==========================
# 6. clear() # clear the set
#==========================

# s = {1,2,3,4,5}
# s.clear()
# print(s) #set()

#==========================
# 7. copy() # copy the set and return a same set
#==========================

# s = {1,2,3,4,5}
# s.copy()
# print(s) #{1, 2, 3, 4, 5}

#==========================
# SET OPERATIONS:
#==========================

#==========================
# 1. Union() # combine the two set and remove the duplicate value
#==========================

# a = {1,2,3}
# b = {3,4,5}

# print(a.union(b)) #{1, 2, 3, 4, 5}

#==========================
# 2. intersection() # return a common value of both set
#==========================

# a = {1,2,3}
# b = {3,2,4,5} 

# print(a.intersection(b)) #{2, 3}

#==========================
# 3. difference() # dono set mai se common value ko remove arta hai or
# return sirf first set ki value karta hai or vo bhi jo repeat na ho rahi ho
#==========================

# a = {1,2,3}
# b = {3,2,4,5} 

# print(a.difference(b)) #{1}

#==========================
# 4. symmetric_difference() # common value hata deta hai or dono ki value return karta hai.
#==========================

# a = {1,2,3}
# b = {3,2,4,5} 

# print(a.symmetric_difference(b)) #{1, 4, 5}

#==========================
# UPDATE OPERATOR :
#==========================

#==========================
# 1. issubset() # dono set ki value check karta hai, first ki value second mai hai ya nai 
#==========================

# a = {1,2,3}
# b = {3,2,4,1}

# print(a.issubset(b)) #True

#==========================
# 2. issuperset() # ye check karta hai ki second ki value first mai hai ki nahi
#==========================

# a = {1,2,3}
# b = {3,2,4,1}

# print(b.issuperset(a)) #True

#==========================
# BUILT-IN-FUNCTIONS :
#==========================

#==========================
#1.len(): 
#==========================
# s = {10, 20, 30, 40}

# print(len(s))

#==========================
#2.sum():
#==========================
# s = {10, 20, 30, 40}

# print(sum(s))

#==========================
#  3.Max():
#==========================
# s = {10, 20, 30, 40}

# print(max(s))


#==========================
#  4.Min():
#========================== 
# s = {10, 20, 30, 40}

# print(min(s))

#==========================
#  5.sorted()
#==========================
# s = {40, 10, 30, 20}

# print(sorted(s))
