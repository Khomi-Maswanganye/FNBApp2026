secret_password = input("Type in your password: ").strip()
first = secret_password[0]
last = secret_password[-1]

print(f"Your password hint: It starts with {first.upper()} and ends with {last.upper()}")

