def even(num):
    if num % 2 == 0:
        return True
    else: 
        return False    

def only_evens(num_lists):
    even_num = []
    

    for num in num_lists:
        
        if even(num):
            even_num.append(num)
    return even_num


num = [3, 4, 7, 9, 12, 176]





print(only_evens(num))