def get_even_list(lst):
    even_list = []
    for number in lst:
        if number%2 == 0:
            even_list.append(number)
    return even_list
    
