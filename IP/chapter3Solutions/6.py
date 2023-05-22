r = int(input("What is the radius of the circle?\n"))

pref = input("Will you take the value of pi as 22/7 or 3.14?\n")

if pref == "22/7":
    area = (22/7) * r * r
    print(f"The area is {area} sq. unit.")

elif pref == "3.14":
    area = 3.14 * r * r
    print(f"The area is {area} sq. unit.")

else:
    print("Give a valid option and run the code again.")
