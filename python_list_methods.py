list1 = [1,2,3,4,5]
list1.append(5)
list1.append(7)
list1.append([1,2,3])     #By using the append method we can add the another list
print(list1)                #[1, 2, 3, 4, 5, 5, 7, [1, 2, 3]]

# Append Error throw Edge cases

# list1 =[1,2,3,4,5]
# list1.append(2,3,4,5)
# print(list1)           # TypeError: list.append() takes exactly one argument (4 given)




list2 = [87,6,5,4]
list2.extend([1,2,3])
print(list2)                             # output = [87, 6, 5, 4, 1, 2, 3]


# Extend Error throw Edge cases

# list2 = [87,6,5,4]
# list2.extend(2,3,4,5)
# print(list2)              #TypeError: list.extend() takes exactly one argument (4 given)

# list2 = [87,6,5,4]
# list2.extend(7)
# print(list2)                #TypeError: 'int' object is not iterable


# list2 = [87,6,5,4]
# list2.extend()
# print(list2)                   #TypeError: list.extend() takes exactly one argument (0 given)

# list3 = [2,3,4,5]
# list3.insert(0,7)
# print(list3)



list3 = [2,3,4,5]
list3.insert(8,9)
print(list3)          # output = [2,3,4,5,9]        

 

list3 = [2,3,4,5]
list3.insert(8,[9])
print(list3)            # output = [2,3,4,5,[9]] 


# Insert Error throw Edge cases
# list3 = [2,3,4,5]
# list3.insert(0,7,5,6)
# print(list3)                  # TypeError: insert expected 2 arguments, got 4

 

# list3 = [2,3,4,5]
# list3.insert()
# print(list3)                    # TypeError: insert expected 2 arguments, got 0


# list3 = [2,3,4,5]
# list3.insert(1.5,8)
# print(list3)                     # TypeError: 'float' object cannot be interpreted as an integer



list4 = [1,2,3,4,5]
list4.clear()

# Clear Error throw Edge cases
# list4 = [1,2,3,4,5]
# list4.clear(3)  
# print(list4)                 #TypeError: list.clear() takes no arguments (1 given)


# list4 =[]
# list4.clear()
# print(list4)             # []


# list5= [5,6,78,9]
# list5.remove()              #TypeError: list.remove() takes exactly one argument (0 given)


# list5= [5,6,78,9]
# list5.remove(5,6)             #TypeError: list.remove() takes exactly one argument (2 given)


list6= [78,89,76,54,36]
list6.pop(3)
print(list6)                     #output = [78, 89, 76, 36]



# list6= [78,89,76,54,36]
# list6.pop(9)
# print(list6)                    #IndexError: pop index out of range


list7 = [3,45,67,8,9]
list7.reverse()
print(list7)               # [9, 8, 67, 45, 3]