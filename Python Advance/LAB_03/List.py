my_list=(12,32,34,12)
print(my_list)

# 1. Create a list of 5 integers and print the third element.
my_list = [1, 2, 3, 4, 5]
print(my_list[2])

# 2. Append the number 10 to the list [1, 2, 3] and print the updated list.
my_list = [1, 2, 3]
my_list.append(10)
print(my_list)

# 3. Remove the last element from the list [4, 5, 6, 7] and print the result.
my_list = [4, 5, 6, 7]
my_list.pop()
print(my_list)

# 4. Reverse the list [1, 2, 3, 4, 5] and print the reversed list.
my_list = [1, 2, 3, 4, 5]
my_list.reverse()
print(my_list)

# 5. Sort the list [9, 3, 7, 1, 5] in ascending order and print the sorted list.
my_list = [9, 3, 7, 1, 5]
my_list.sort()
print(my_list)

# 6. Find the sum of all elements in the list [10, 20, 30, 40, 50].
my_list = [10, 20, 30, 40, 50]
print(sum(my_list))

# 7. Check if the number 7 exists in the list [1, 2, 3, 4, 5].
my_list = [1, 2, 3, 4, 5]
print(7 in my_list)

# 8. Concatenate two lists: [1, 2, 3] and [4, 5, 6], and print the result.
list1 = [1, 2, 3]
list2 = [4, 5, 6]
print(list1 + list2)

# 9. Create a list of even numbers from 1 to 20 using list comprehension.
even_numbers = [x for x in range(1, 21) if x % 2 == 0]
print(even_numbers)

# 10. Replace the second element in the list [10, 20, 30, 40] with 25.
my_list = [10, 20, 30, 40]
my_list[1] = 25
print(my_list)

# 11. Create a tuple with 5 elements and print the second element.
my_tuple = (1, 2, 3, 4, 5)
print(my_tuple[1])

# 12. Convert the tuple (1, 2, 3) into a list and print the result.
my_tuple = (1, 2, 3)
print(list(my_tuple))

# 13. Count the number of occurrences of 3 in the tuple (1, 2, 3, 3, 4).
my_tuple = (1, 2, 3, 3, 4)
print(my_tuple.count(3))

# 14. Access the last element of the tuple (10, 20, 30, 40, 50).
my_tuple = (10, 20, 30, 40, 50)
print(my_tuple[-1])

# 15. Concatenate two tuples: (1, 2, 3) and (4, 5, 6), and print the result.
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
print(tuple1 + tuple2)

# 16. Check if the tuple (1, 2, 3) contains the element 2.
my_tuple = (1, 2, 3)
print(2 in my_tuple)

# 17. Unpack the tuple (10, 20, 30) into three variables a, b, and c, and print their values.
my_tuple = (10, 20, 30)
a, b, c = my_tuple
print(a, b, c)

# 18. Write a program to swap two tuples: t1 = (1, 2) and t2 = (3, 4).
t1 = (1, 2)
t2 = (3, 4)
t1, t2 = t2, t1
print(t1, t2)

# 19. Create a dictionary with three key-value pairs and print it.
my_dict = {'name': 'Alice', 'age': 25, 'city': 'New York'}
print(my_dict)

# 20. Add a new key-value pair 'city': 'New York' to the dictionary {'name': 'Alice', 'age': 25}.
my_dict = {'name': 'Alice', 'age': 25}
my_dict['city'] = 'New York'
print(my_dict)
