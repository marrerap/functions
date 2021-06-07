def temp(C):
    F = (C * 9/5) + 32
    return f"The temperature is {F} degrees."

C = int(input('What is the temperature in Celsius? '))
print(temp(C))
