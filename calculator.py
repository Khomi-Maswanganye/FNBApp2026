num1 = float(input("Number:"))
num2 = float(input("Number:"))

if num2 == 0:
    print("Error: Second number shouldnt not be 0")
else:
    add = num1 + num2
    sub = num1 - num2
    times = num1 * num2
    divide = num1/num2

    floor = num2//num1
    mod = num2%num1

    print(f"Addition:{round(add,2)}","\n")
    print(f"Subtraction:{round(sub,2)}","\n")
    print(f"Multiplication:{round(times,2)}","\n")
    print(f"divide:{round(divide,2)}","\n")
    print(f"floor:{round(floor,2)}","\n")
    print(f"Modulus:{round(mod,2)}")

