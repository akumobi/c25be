person = {
    "name": "Ben White",
    "age": 22,
    "height": 5.6,
    "weight": "78 kg",
    "is_present": True,
    "nationality": {
        "state_of_origin": "Delta",
        "LGA": "IKA South",
        "NIN": 26389458620
    },
    "appearance": ["Tall", "Skinny", "dark"],
    "features": {
        "assets": ["car", "house", "dog"],
        "bank_details": {
            "name_of_bank": "Zenith Bank",
            "Account_No": 2345478902,
            "BVN": 34574567856434562985
        }
    }
}

#Use print function to extract a value from each of the follwing keys
#name, nationality, appearance, features >> asstes and bank details

print("My name is", person["name"], "I hail from", person["nationality"]["LGA"], "of", person["nationality"]["state_of_origin"], "and I own a", person["features"]["assets"][1], "that I bought with the money in my", person["features"]["bank_details"]["name_of_bank"])