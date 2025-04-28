# =============================================
# Additional Beginner Data Structures Assignment (10 Questions)
# =============================================

"""
1. Dictionary Creation and Access
Create a dictionary called 'car' with:
- 'make' (string)
- 'model' (string)
- 'year' (number)
- 'features' (list of 3 features)
Print the dictionary, then print just the model and the second feature.
"""
car = {
    'make': 'Mercedes Benz',
    'model': 'G Wagon',
    'year': 2026,
    'features': ['Bullet Proof', 'Carbon Fibre', 'EV']
}
print(car, car['model'], car['features'][1])

"""
2. List Manipulation
Create this list: colors = ['red', 'green', 'blue']
Then:
1. Add 'yellow' to the beginning
2. Remove 'green'
3. Change 'blue' to 'purple'
Print the final list
"""
colors = ['red', 'green', 'blue']
colors.insert(0, 'yellow')
colors.remove('green')
colors[2] = 'purple'
print(colors)

"""
3. Set Operations
Create two sets:
fruits = {'apple', 'banana', 'orange'}
tropical = {'mango', 'pineapple', 'banana'}
1. Print fruits that are not in tropical
2. Print all unique fruits from both sets
"""
fruits = {'apple', 'banana', 'orange'}
tropical = {'mango', 'pineapple', 'banana'}
print(fruits - tropical)
print(fruits | tropical)

"""
4. Nested Dictionary Access
Create a dictionary for a movie with:
- 'title'
- 'director'
- 'year'
- 'cast' (dictionary with 2 main actors and their roles)
Print one actor's name and their role
"""
movie = {
    'title': 'Prison Break',
    'director': 'Movie Director',
    'year': 2017,
    'cast': {'Michael Scofield': 'Lead Actor', 'Lincon Burrows': "Lead Actor's Brother"}
}
print(movie['cast']['Michael Scofield'])

"""
5. Tuple Unpacking
1. Create a tuple with 3 numbers
2. Unpack it into three variables
3. Print their sum
"""
threenums = (7, 9, 5)
var1, var2, var3 = threenums
print(var1 + var2 + var3)

"""
6. Dictionary in List
Create a list called 'inventory' with 2 item dictionaries.
Each item should have 'name', 'price', and 'in_stock' (boolean).
Print the name of the first item and whether the second is in stock.
"""
inventory = [{'name': "Lenovo Yoga", 'price': 1100000, 'in_stock': True},
             {'name': "Dell Lattitude", 'price': 750000, 'in_stock': False}]
print(inventory[0]['name'], inventory[1]['in_stock'])

"""
7. Membership Testing with Multiple Conditions
Create a list of approved users: approved = ['alice', 'bob', 'charlie']
Check if:
1. 'alice' is in the list AND 'dave' is not
2. 'bob' is in the list OR 'eve' is in the list
Print both results
"""
approved = ['alice', 'bob', 'charlie']
result1 = 'alice' in approved and 'dave' not in approved
result2 = 'bob' in approved or 'eve' in approved

print(result1, result2)

"""
8. Dictionary Comparison
Create two dictionaries with the same keys but different order:
dict_a = {'x': 1, 'y': 2}
dict_b = {'y': 2, 'x': 1, 'z': 3}
1. Check if they have the same key-value pairs for common keys
2. Check if they are identical dictionaries
Print both results
"""
dict_a = {'x': 1, 'y': 2}
dict_b = {'y': 2, 'x': 1, 'z': 3}

"""
9. Complex List Operations
Given the list: data = [1, [2, 3], [4, [5, 6]], 7]
1. Print the number 6
2. Check if 3 is in any sublist
3. Check if 7 is at the top level
Print all results
"""
data = [1, [2, 3], [4, [5, 6]], 7]

"""
10. Combined Data Structure
Create a dictionary 'school' with:
- 'name'
- 'students' (list of 2 student dictionaries with 'name' and 'grades')
- 'location' (dictionary with 'city' and 'state')
Print:
1. The second student's name
2. The school's state
"""
school = {
    'name': 'Univelcity',
    'students': [{'name': 'Yinka', 'grade': 'Distinction'}, {'name': 'Ebun', 'grade': 'Excellent'}],
    'location': {'city': 'Yaba', 'state': 'Lagos'}
}
print(school['students'][1]['name'], school['location']['state'])