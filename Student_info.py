first_name = input("Firstname: ")
surname = input("Surname: ")
age = int(input("Age: "))
fav_num = float(input("Favourite number: "))
age_in_months = age * 12

new_num = round(fav_num, 2)

print(f"Welcome, {first_name.upper(), surname.upper()}".title() ,"\n")
print("Datatype of name: ", type(first_name),"\n")

print(f"Your age is: {age}","\n")
print(f"In months: {age_in_months}","\n")
print("Datatype of age: ", type(age),"\n")

print(f"Your favourite number is: {new_num}","\n")
print("Datatype of new number: ", type(new_num))