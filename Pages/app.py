# list1 = [1,2,3,1,2]
# print(list1)



# def add(num1, num2):
#     return num1+num2


# print(add(2,3))

# # Empty dictionary
# my_dict = {}

# # Dictionary with initial values
# my_dict = {'name': 'John', 'age': 30, 'city': 'New York'}

# # Using dict() constructor with keyword arguments
# another_dict = dict(name='Jane', age=25, city='San Francisco')


# print(my_dict['name'])  # Output: 'John'
# print(another_dict['age'])  # Output: 25


# # Modify value
# my_dict['age'] = 32

# # Add new key-value pair
# my_dict['occupation'] = 'Engineer'


# print(my_dict)

# del my_dict['city']
# print(my_dict)

# print("--------------------------")


# for key in my_dict:
#     print(key, my_dict[key])

# for value in my_dict.values():
#     print(value)

# for key, value in my_dict.items():
#     print(key, value)


# print("-------------")


# mylist = ["a", "b", "c"]

# for values in mylist:
#     print(values)
#     if values == "b":
#         break

#     print(values)




file_name = open("/Users/kishankunwar/PycharmProjects/GeoDashboard/Pages/countries.txt", "r")

for files in file_name.readlines():
    print(files)

    
print(file_name.readable())

file_name.close()

    


