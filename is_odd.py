def even(num):
    if not num % 2 == 0:
        return True
    else: 
        return False    


num = int(input("Enter any number to determine if it is odd: "))

print(even(num))