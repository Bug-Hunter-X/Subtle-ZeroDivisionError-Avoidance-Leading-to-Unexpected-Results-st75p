def function_with_uncommon_error(a, b):
    if a == 0:
        return b
    elif b == 0:
        return a
    else:
        return a / b

result = function_with_uncommon_error(5, 0)  # Returns 5
print(result)  
result = function_with_uncommon_error(0, 5)  # Returns 5
print(result)  
result = function_with_uncommon_error(0,0) # Returns 0
print(result)
result = function_with_uncommon_error(5,5) # Returns 1.0
print(result)