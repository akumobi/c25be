# =============================================
# Beginner Data Structures Assignment (15 Questions)
# =============================================

"""
1. Create a Dictionary
Make a dictionary called 'person' with:
- 'name' (your name as string)
- 'age' (your age as number)
- 'hobbies' (a list of 3 hobbies)
Print the dictionary.
"""
# Answer No 1 here
person = {
    "name": "Kingsley",
    "age": 24,
    "hobbies": ["Reading", "Strategic Thinking", "Nature Walk"]
}
print("Answer No 1 here:", person)

"""
2. Access Dictionary Values
Using the 'person' dictionary:
1. Print just the age
2. Print the second hobby
3. Add a new key 'city' with your city
"""
# Answer No 2 here
person ["city"] = "Lagos"
print("Answer No 2 here:", person["age"], person["hobbies"][1])

"""
3. Modify a List
Create this list:
fruits = ['apple', 'banana', 'cherry']
Then:
1. Change 'banana' to 'mango'
2. Add 'orange' to the end
3. Remove 'apple'
Print the final list
"""
# Answer No 3 here
fruits = ['apple', 'banana', 'cherry']
fruits[1] = "mango"
fruits.append("orange")
del fruits[0]
print("Answer No 3 here:", fruits)

"""
4. Check if Item Exists (in keyword)
Using the 'fruits' list from #3:
1. Check if 'mango' is in the list
2. Check if 'apple' is NOT in the list
Print both results
"""
# Answer No 4 here
print("Answer No 4 here:")
if 'mango' in fruits:
    print("mango is in the list")
else:
    print("mango is not in the list")

if 'apple' not in fruits:
    print("apple is NOT in the list")
else:
    print("apple is in the list")

"""
5. Tuple Basics
1. Create a tuple with 3 colors
2. Print the first color
3. Try to change the second color (this should fail)
"""
# Answer No 5 
print("Answer No 5 here:")
colors = ("red", "blue", "green")
print(colors[0])
# colors[1] = "yellow"


"""
6. Set Operations
Create two sets:
set1 = {1, 2, 3}
set2 = {3, 4, 5}
1. Print their intersection (common elements)
2. Print their union (all elements)
"""
# Answer No 6 here
print("Answer No 6 here:")
set1 = {1, 2, 3}
set2 = {3, 4, 5}
print("Intersection:", set1 & set2)
print("Union:", set1 | set2)

"""
7. Nested Dictionary Access
Create a dictionary for a book with:
- 'title'
- 'author'
- 'year'
- 'details' (another dictionary with 'pages' and 'genre')
Print the book's genre
"""
# Answer No 7 here
print("Answer No 7 here:")
book = {
    'title': 'Force Yourself to Be Consistent',
    'author': 'Youtube',
    'year': 1925,
    'details': {
        'pages': 1280,
        'genre': 'Self Dev'
    }
}
print("Book's genre:", book['details']['genre'])

"""
8. List of Dictionaries
Create a list called 'students' with 2 student dictionaries.
Each student should have 'name' and 'grade'.
Print the second student's name.
"""
# Answer No 8 here

students = [
    {'name': 'Ebun', 'grade': 'A'}, 
    {'name': 'Yinka', 'grade': 'A+'}]
print("Answer No 8 here:", students[1]['name'])

"""
9. Dictionary Methods
Using the 'person' dictionary:
1. Print all keys
2. Print all values
3. Check if 'age' exists as a key
"""
# Answer No 9 here
print("Answer No 9 here:")
print("All keys:", person.keys())
print("All values:", person.values())
if 'age' in person:
    print("'age' exists as a key")
else:
    print("'age' does not exist as a key.")

"""
10. Logical AND Operation
Given:
has_subscription = True
has_payment = False
Check if both conditions are True using AND
Print the result
"""
# Answer No 10 here
has_subscription = True
has_payment = False
print("Answer No 10 here:", has_subscription and has_payment)

"""
11. Logical OR Operation
Using the same variables from #10:
Check if at least one condition is True using OR
Print the result
"""
# Answer No 11 here

print("Answer No 11 here:", has_subscription or has_payment)


"""
12. Combined Logical Operations
Create a shopping cart list:
cart = ['apple', 'milk', 'bread']
Check if:
1. 'milk' is in cart AND 'eggs' are not in cart
2. 'bread' is in cart OR 'juice' is in cart
Print both results
"""
# Answer No 12 here
cart = ['apple', 'milk', 'bread']
check1 = 'milk' in cart and 'eggs' not in cart
check2 = 'bread' in cart or 'juice' in cart
print("Answer No 12 here:", 'check1=>', check1, 'check2=>', check2)

"""
13. Dictionary Comparison
Create two dictionaries:
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 2, 'a': 1}
Check if they have the same content using ==
Check if they are the same object using 'is'
Print both results
"""
# Answer No 13 here
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 2, 'a': 1}
same_content = dict1 == dict2
same_object = dict1 is dict2
print("Answer No 13 here:", 'using ==', same_content, 'using "is"', same_object)

"""
14. Membership Testing in Nested Structure
Given this nested list:
data = [1, [2, 3], 4, [5, 6]]
Check if 3 is in any of the sublists
Print the result
Hint: Check each sublist manually
"""
# Answer No 14 here
data = [1, [2, 3], 4, [5, 6]]
print("Answer No 14 here: can't seem to figure this out")

"""
15. Complex Logical Check
Create a game character dictionary:
character = {
    'name': 'Warrior',
    'level': 15,
    'items': ['sword', 'shield', 'potion'],
    'active': True
}
Check if:
1. Level is > 10 AND has 'sword' in items
2. Is active OR has 'magic' in items
Print both results
(Take note: Do not use if statements. Only what you where taught.)
"""
# Answer No 15 here
character = {
    'name': 'Warrior',
    'level': 15,
    'items': ['sword', 'shield', 'potion'],
    'active': True
}

condition1 = character['level'] > 10 and 'sword' in character['items']
condition2 = character['active'] or 'magic' in character['items']
print("Answer No 15 here:", condition1, 'and', condition2)