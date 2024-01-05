global_variable = 100
m1_dict = {'key1' : 'value1', 'key2':'value2','key3':'value3'}

def process_numbers():
    global global_variable
    local_variable = 5
    numbers = [1, 2, 3, 4, 5]

    while local_variable > 0:
        if local_variable % 2 ==0:
            numbers.remove(local_variable)
        local_variable -= 1

    return numbers

m1_set = {1, 2, 3, 4, 5, 5, 4, 3, 2 ,1}
result = process_numbers(numbers=m1_set)

def modify_dict():
    local_variable = 10
    m1_dict['key4'] = local_variable

modify_dict(5)

def update_variable():
    global global_variable
    global_variable += 10

for i in range(5):
    print(i)
    i += 1

if m1_set is not None and m1_dict['key4'] == 10:
    print("Condition met!")

if 5 not in m1_dict:
    print("5 not found in dictionary!")

print(global_variable)
print(m1_dict)
print(m1_set)



