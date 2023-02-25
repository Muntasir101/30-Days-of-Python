# syntax
empty_dict = {}
# Dictionary with data values
dct = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3', 'key4': 'value4'}

person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

"""
Dictionary Length

It checks the number of 'key: value' pairs in the dictionary.
"""

# syntax
dct = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3', 'key4': 'value4'}
print(len(dct))  # 4

person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}
print(len(person))  # 7

## Accessing Dictionary Items

# syntax
dct = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3', 'key4': 'value4'}
print(dct['key1'])  # value1
print(dct['key4'])  # value4

person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}
print(person['first_name'])  # Asabeneh
print(person['country'])  # Finland
print(person['skills'])  # ['JavaScript', 'React', 'Node', 'MongoDB', 'Python']
print(person['skills'][0])  # JavaScript
print(person['address']['street'])  # Space street
print(person['city'])  # Error

## Accessing an item by key name raises an error if the key does not exist.
# To avoid this error first we have to check if a key exist or we can use the _get_ method.
# The get method returns None, which is a NoneType object data type, if the key does not exist.
person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}
print(person.get('first_name'))  # Asabeneh
print(person.get('country'))  # Finland
print(person.get('skills'))  # ['HTML','CSS','JavaScript', 'React', 'Node', 'MongoDB', 'Python']
print(person.get('city'))  # None

### Adding Items to a Dictionary
# syntax
dct = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3', 'key4': 'value4'}
dct['key5'] = 'value5'

person = {'first_name': 'Asabeneh', 'last_name': 'Yetayeh', 'age': 250, 'country': 'Finland', 'is_marred': True,
          'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'], 'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }, 'job_title': 'Instructor'}
person['skills'].append('HTML')
print(person)

### Modifying Items in a Dictionary
# syntax
dct = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3', 'key4': 'value4'}
dct['key1'] = 'value-one'

person['first_name'] = 'Eyob'
person['age'] = 252

### Checking Keys in a Dictionary
# syntax
dct = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3', 'key4': 'value4'}
print('key2' in dct)  # True
print('key5' in dct)  # False

### Removing Key and Value Pairs from a Dictionary

"""
- _pop(key)_: removes the item with the specified key name:
- _popitem()_: removes the last item
- _del_: removes an item with specified key name
"""
# syntax
dct = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3', 'key4': 'value4'}
dct.pop('key1')  # removes key1 item
dct = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3', 'key4': 'value4'}
dct.popitem()  # removes the last item
del dct['key2']  # removes key2 item

person.pop('first_name')  # Removes the firstname item
person.popitem()  # Removes the address item
del person['is_married']  # Removes the is_married item

### Changing Dictionary to a List of Items
dct = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3', 'key4': 'value4'}
print(dct.items())  # dict_items([('key1', 'value1'), ('key2', 'value2'), ('key3', 'value3'), ('key4', 'value4')])
print(dct.items())

### Deleting a Dictionary
# syntax
dct = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3', 'key4': 'value4'}
del dct

### Copy a Dictionary
# syntax
dct = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3', 'key4': 'value4'}
dct_copy = dct.copy()  # {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}

### Getting Dictionary Keys as a List
dct = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3', 'key4': 'value4'}
keys = dct.keys()
print(keys)  # dict_keys(['key1', 'key2', 'key3', 'key4'])

### Getting Dictionary Values as a List
# syntax
dct = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3', 'key4': 'value4'}
values = dct.values()
print(values)  # dict_values(['value1', 'value2', 'value3', 'value4'])
