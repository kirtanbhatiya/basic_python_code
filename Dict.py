#============================
# dictionary
# key, value pair
#============================

# detail = {
#     "rahul": 9027349,
#     "het": 949164,
#     "sahil": 962394
# }
# print(detail)

#============================
# epty dict
#============================

# d = dict()
# print(d)

#============================
# with keys, values
#============================

# students = {
#     "name": "kirtan",
#     "age":20,
#     "city": "ahmedabad"
# }
# print(students) #{'name': 'kirtan', 'age': 20, 'city': 'ahmedabad'}

#============================
# mixed keys and values
#============================

# data = {
#     "name": "Python",
#     "version": 3.14,
#     "popular": True,
#     "topics": ("List", "Tuple")
# }
# print(data) #{'name': 'Python', 'version': 3.14, 'popular': True, 'topics': ('List', 'Tuple')}

#============================
# nested dictionary
#============================

# data = {
#     "name":"kirtan",
#     "age":20,
#     "subjects":{
#         "maths",
#         "science"
#     }
# }
# print(data) #{'name': 'kirtan', 'age': 20, 'subjects': {'science', 'maths'}}

#============================
# Accsess Dict
#============================

# data = {
#     "name":"kirtan",
#     "age":20,
#     "subjects":{
#         "maths",
#         "science"
#     }
# }

# print(data["name"]) #kirtan

#============================
# Accsess by get 
#============================

# data = {
#     "name":"kirtan",
#     "age":20,
#     "subjects":{
#         "maths",
#         "science"
#     }
# }
# print(data.get("age")) #20

#============================
# Add new key and value
#============================

# data = {
#     "name":"kirtan",
#     "age":20,
#     "subjects":{
#         "maths",
#         "science"
#     }
# }

# data["city"]= "Ahmedabad"

# print(data) #{'name': 'kirtan', 'age': 20, 'subjects': {'maths', 'science'}, 'city': 'Ahmedabad'}

#============================
# update value
#============================

# data = {
#     "name":"kirtan",
#     "age":20,
#     "subjects":{
#         "maths",
#         "science"
#     }
# }

# data["age"]= 22
# print(data) #{'name': 'kirtan', 'age': 22, 'subjects': {'maths', 'science'}}

#============================
# Delete the key and value
#============================

# data = {
#     "name":"kirtan",
#     "age":20,
#     "subjects":{
#         "maths",
#         "science"
#     }
# }
# del data["subjects"]
# print(data) #{'name': 'kirtan', 'age': 20}

# data = {
#     "name":"kirtan",
#     "age":20,
#     "subjects":{
#         "maths",
#         "science"
#     }
# }
# for value in data.items():
#     print(value) 

#Output =
# #('name', 'kirtan')
# ('age', 20)
# ('subjects', {'maths', 'science'})

#============================
# Accessing using for loop with key and value
#============================

# data = {
#     "name":"kirtan",
#     "age":20,
#     "subjects":{
#         "maths",
#         "science"
#     }
# }
# for key,value in data.items():
#     print(key,value) 

# Output = name kirtan
# age 20
# subjects {'science', 'maths'}

#============================
# DIct Mathods
#============================

#============================
# 1. get(): accsess values
#============================

# data = {
#     "name":"kirtan",
#     "age":20,
#     "city":"morbi"
# }

# new_data=data.get("city")
# print(new_data) #morbi

#============================
# 2. key() :
#============================

# data = {
#     "name":"kirtan",
#     "age":20,
#     "city":"morbi"
# }

# new =data.keys()
# print(new) #dict_keys(['name', 'age', 'city'])

#============================
# 3. values()
#============================

# data = {
#     "name":"kirtan",
#     "age":20,
#     "city":"morbi"
# }
# new = data.values()
# print(new) #dict_values(['kirtan', 20, 'morbi'])

#============================
# # 4 items()
#============================
# data = {
#     "name":"kirtan",
#     "age":20,
#     "city":"morbi"
# }
# new = data.items()
# print(new) #dict_items([('name', 'kirtan'), ('age', 20), ('city', 'morbi')])

#============================
# #5 update()
#============================
# data = {
#     "name":"kirtan",
#     "age":20,
#     "city":"morbi"
# }
# data.update({"city":"ahmedabad"})
# print(data) #{'name': 'kirtan', 'age': 20, 'city': 'ahmedabad'}

#============================
# # 6 pop()
#============================
# data = {
#     "name":"kirtan",
#     "age":20,
#     "city":"morbi"
# }
# new = data.pop("age")
# print(new) #20

#============================
# #7 popitem()
#============================
# data = {
#     "name":"kirtan",
#     "age":20,
#     "city":"morbi"
# }
# new = data.popitem()
# print(new) #('city', 'morbi')

#============================
# #8 clear()
#============================
# data = {
#     "name":"kirtan",
#     "age":20,
#     "city":"morbi"
# }
# data.clear()
# print(data) #{}

#============================
# #9 copy()
#============================
# data = {
#     "name":"kirtan",
#     "age":20,
#     "city":"morbi"
# }
# new = data.copy()
# print(new) #{'name': 'kirtan', 'age': 20, 'city': 'morbi'}

#============================
# #10 setdefault()
#============================

# data = {
#     "name":"kirtan",
#     "age":20,
#     "city":"morbi"
# }
# new =data.setdefault("subject","maths")
# print(new) #maths
