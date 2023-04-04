#json.dumps

import json

data_1 = {
    "D" : 6,
    "M" : 25,
    "m" : 27
}
print(data_1)
data_2 = json.dumps(data_1)

print(data_2)

#exception handling

try:
    numerator = 10
    denominator = 0

    result = numerator/denominator

    print(result)
except:
    print("Error: Denominator cannot be 0.")
    
finally:
    print("This is finally block.")


#list comprehension without condition

numbers = [ x for x in range(30)]

print(numbers)

#list comprehension with condition

numbers = [ x for x in range(100) if x%5 == 0]

print(numbers)
