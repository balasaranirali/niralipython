def add_numbers(*args):
    total= 0
    for num in args:
        total += num
        return total
# calling function 
print(add_numbers(10,20))
print(add_numbers(5,10,15,20))