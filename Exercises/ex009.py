# Your Student ID: 230543001
# Your Name and Surname: Esra Gürbüz

#celciustofahrenheit = ctof = (C * (9/5) + 32)
#fahrenheittocelcius = ftoc = ((F -32) * (5/9))

which = input("Which conversion do you want: (ctof or ftoc) ")
value = int(input("Which value do you want to change? "))



if which == "ctof":
    result = ((value * 9/5) + 32)
    print(f"{value}°C is equal to {result}°F")
elif which == ftoc:
    result = (value - 32) * 5/9
    print(f"{value}°F is equal to {result}°C")
else:
    print("Invalid input.")

