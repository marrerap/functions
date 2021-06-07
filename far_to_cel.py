def temp(F):
    C = (F - 32) * 5/9
    return f"The temperature is {C} degrees."

F = int(input('What is the temperature in Fahrenheit? '))
print(temp(F))
