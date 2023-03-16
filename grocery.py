#######

# making dict emtpy one
grocery_list = {}

while True:
    try:

        fruit = input("").upper()
        if fruit not in grocery_list:
            grocery_list[fruit] = 1
        else:
            grocery_list[fruit] += 1
    except (EOFError, KeyError):
        break

# printing results

for key, value in grocery_list.items():
    print(value, key)