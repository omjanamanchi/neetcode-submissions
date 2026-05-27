def add_two_numbers() -> int:
    s = ""
    user_input = input()
    s+=user_input
    my_list = [int(x) for x in s.split(",")]
    total = sum(my_list)
    return total
    



# do not modify below this line
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
