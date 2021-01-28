# convert temperatures
# input
celsius = "60°C"
fahrenheit = "45°F"

C = 60
F = 45

# do the math
calF = (C * 1.8) + 32
calC = ((F -32)) * (5 / 9)


rounded_calF = round(calF)
rounded_calC = round(calC)

# For testing:
    # print(rounded_calF)
    # print(rounded_calC)

# output
print(celsius, "is", rounded_calF, "in Fahrenheit")
print(fahrenheit, "is", rounded_calC, "in Celsius")