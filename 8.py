def my_function(*args,b=2):
    results=(all(args),b)
    return sum(results)==b

print(my_function(7,6,7,0,b=6))