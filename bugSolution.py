def function_with_robust_error_handling(a, b):
    if a == 0 and b == 0:
        return 0  # Handle both zeros appropriately
    elif b == 0:
        return float('inf') # Return infinity or NaN as appropriate for division by zero.
    elif a == 0:
        return 0
    else:
        return a / b

result = function_with_robust_error_handling(5, 0) 
print(result) # Output: inf
result = function_with_robust_error_handling(0, 5) 
print(result) # Output: 0.0
result = function_with_robust_error_handling(0,0) 
print(result) # Output: 0
result = function_with_robust_error_handling(5,5) 
print(result) # Output: 1.0