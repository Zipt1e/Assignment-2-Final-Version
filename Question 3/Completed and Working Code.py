global_variable = 100
m1_dict = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}

def process_numbers(numbers):
    local_variable = 5

    # Use list comprehension to create a new list with filtered numbers
    numbers = [num for num in numbers if num % 2 != 0]

    while local_variable > 0:
        local_variable -= 1

    return numbers

m1_set = {1, 2, 3, 4, 5, 5, 4, 3, 2, 1}
result = process_numbers(numbers=m1_set)

def modify_dict(value):
    local_variable = 10
    m1_dict['key4'] = local_variable + value

modify_dict(5)

def update_variable():
    global global_variable
    global_variable += 10

for i in range(5):
    print(i)

if m1_set is not None and m1_dict.get('key4', 0) == 15:  # Use get() method to handle missing key
    print("Condition met!")

if 5 not in m1_dict.values():  # Check if 5 is not present in dictionary values
    print("5 not found in dictionary!")

print(global_variable)
print(m1_dict)
print(m1_set)
