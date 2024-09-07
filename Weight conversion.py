print("Weight converter!")
weight = float(input("Enter your weight: "))
unit = input("Is this weight is in kilograms or pounds? (k or l): ")
if unit.lower() == "k" :
    weight = weight * 2.20462
    unit = "lbs"
    print(f"The weight in {unit} is {round(weight,2)}")
elif unit.lower() == "l" :
    weight = weight / 2.20462
    unit = "kgs"
    print(f"The weight in {unit} is {round(weight,2)}")
else :
    print("Invalid unit")