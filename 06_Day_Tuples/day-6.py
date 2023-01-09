"""
Index:
1. Creating a Tuple
2. Tuples length
3. Accessing Tuple Items
  3.1 Positive Index
  3.2 Negative Index
4. Changing Tuples to Lists
5. Checking an Item in a Tuple
6. Joining Tuples
7. Deleting a Tuple
"""

# Creating a Tuple
# syntax
empty_tuple = ()
# or using the tuple constructor
empty_tuple = tuple()

# syntax
tpl = ('item1', 'item2', 'item3')

fruits = ('banana', 'orange', 'mango', 'lemon')

# Tuples length
# syntax
tpl = ('item1', 'item2', 'item3')
print(len(tpl))  # 3

# Accessing Tuple Items
tpl = ('item1', 'item2', 'item3')
first_item = tpl[0]
second_item = tpl[1]
print(first_item)  # item1
print(second_item)  # item2

fruits = ('banana', 'orange', 'mango', 'lemon', 'apple')
first_fruit = fruits[0]
second_fruit = fruits[1]
last_index = len(fruits) - 1
print(last_index)  # 4
last_fruit = fruits[last_index]
print(last_fruit)  # apple

# Accessing : Negative Indexing
tpl = ('item1', 'item2', 'item3', 'item4')
first_item = tpl[-4]
second_item = tpl[-3]
print(first_item)  # item1
print(second_item)  # item2

fruits = ('banana', 'orange', 'mango', 'lemon')
first_fruit = fruits[-4]
second_fruit = fruits[-3]
last_fruit = fruits[-1]
print(first_fruit)  # banana
print(second_fruit)  # orange
print(last_fruit)  # lemon

# Slicing: Range of Positive Indexes
tpl = ('item1', 'item2', 'item3', 'item4')
all_items = tpl[0:4]  # all items
all_items = tpl[0:]  # all items
middle_two_items = tpl[1:3]  # does not include item at index 3

fruits = ('banana', 'orange', 'mango', 'lemon')
all_fruits = fruits[0:4]  # all items
all_fruits = fruits[0:]  # all items
orange_mango = fruits[1:3]  # doesn't include item at index 3
orange_to_the_rest = fruits[1:]

# Slicing: Range of Negative Indexes
tpl = ('item1', 'item2', 'item3', 'item4')
all_items = tpl[-4:]  # all items
middle_two_items = tpl[-3:-1]  # does not include item at index 3 (-1)

fruits = ('banana', 'orange', 'mango', 'lemon')
all_fruits = fruits[-4:]  # all items
orange_mango = fruits[-3:-1]  # doesn't include item at index 3
orange_to_the_rest = fruits[-3:]

# Changing Tuples to Lists
# Syntax
tpl = ('item1', 'item2', 'item3', 'item4')
lst = list(tpl)

fruits = ('banana', 'orange', 'mango', 'lemon')
fruits = list(fruits)
fruits[0] = 'apple'
print(fruits)  # ['apple', 'orange', 'mango', 'lemon']
fruits = tuple(fruits)
print(fruits)  # ('apple', 'orange', 'mango', 'lemon')

# Checking an Item in a Tuple
# Syntax
tpl = ('item1', 'item2', 'item3', 'item4')
'item2' in tpl  # True

fruits = ('banana', 'orange', 'mango', 'lemon')
print('orange' in fruits)  # True
print('apple' in fruits)  # False
fruits[0] = 'apple'  # TypeError: 'tuple' object does not support item assignment

# Joining Tuples
# syntax
tpl1 = ('item1', 'item2', 'item3')
tpl2 = ('item4', 'item5','item6')
tpl3 = tpl1 + tpl2

fruits = ('banana', 'orange', 'mango', 'lemon')
vegetables = ('Tomato', 'Potato', 'Cabbage','Onion', 'Carrot')
fruits_and_vegetables = fruits + vegetables

# Deleting Tuples
# syntax
tpl1 = ('item1', 'item2', 'item3')
del tpl1

fruits = ('banana', 'orange', 'mango', 'lemon')
del fruits


