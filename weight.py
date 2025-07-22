weight = int(input("Weight:"))
unit = input("(K)g or (L)bs:")

if unit.upper()  == "K":
    converted = weight / 0.45
    print("The weight in Lbs " + str(converted))
else:
    converted = weight * 0.45
    print("The weight is KGs " + str(converted))

# Used Type conversion and concatenating int with string using str