kilos = float(input("How many kilometers do you want to drive?:"))
petrol_ppl = float(input("Current petrol pprice per liter?:"))

litres_needed = kilos/10
price_cost = litres_needed*petrol_ppl

print("South African Cost Calculator".title())
print("================================")

print(f"Kilometers drive:R{round(kilos,2)}","\n")
print(f"Petrol price per liter:R{round(petrol_ppl,2)}","\n")
print(f"Liters need:R{round(litres_needed,3)}","\n")
print(f"Price cost:R{round(price_cost,2)}","\n")