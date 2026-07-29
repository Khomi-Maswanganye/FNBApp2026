first_name = input("Enter your name: ")
last_name = input("Enter your last name: ")
bio = input("Enter a one line bi message:")
username = f"{first_name[0].lower()}{last_name.lower()}".strip()
num_char= len(bio)
replace = bio.replace("I am","I'm")

print(f"{first_name.title()}","\n")
print(f"{username}","\n")
print(f"{bio}","\n")

print(f"Number of characters are:{num_char}","\n")
print(f"Replace characheres:{replace}")

