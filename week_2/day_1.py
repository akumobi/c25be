#Data Structures

#List
#Turple
#Set
#Dictionary

bio = {
    "name": "King",
    "gender": "male",
    "height": 1.68,
    "nationality": "Nigeria",
    "classroom": {
        "cohort": "Charlie",
        "mode": "Onsite",
        "course": "Backend with Django",
        "number of students" : 3,
        "instructor": "Miracle King"
    }
}


#bio.values()
#bio["classroom"]["instructor"]

#Updating Dictionary Values

bio["name"] = "Kingsley"
bio["classroom"]["mode"] = "online"

#Deleting Dictionary Values

del bio["classroom"]["mode"]

#More deleting options
bio.clear() #clears the entire key value of the dictionary
# print(bio)


#Classwork
my_favourite_soup = {}

#Add a key value called 'name' and 
my_favourite_soup ["name"] = "Vegetable"
my_favourite_soup ["protein"] = "Snail"
my_favourite_soup ["swallow"] = "Poundo"
my_favourite_soup ["drink"] = "Pineapple Juice"

#Delete 
del my_favourite_soup["swallow"]

print(my_favourite_soup)


#List
#Can be accessed using index with first index as zero(0)
#Values are in square brackets
#Can take any data type

anything = ["Ball", 2, 0.3, True, {"name": "Kingsley"}, ["ice", False, 23, "price"]]

