# Python Lab Assignment: The Flexible Calculator

## Objectives
* Practice using variable-length positional arguments (`*args`).
* Practice using variable-length keyword arguments (`**kwargs`).
* Implement robust error handling using `try-except` blocks.

---

## Assignment Instructions

You need to write a flexible calculator function that can accept any number of numbers, configuration settings via keywords, and gracefully handles common input errors.

### Requirements:
1. **Function Name**: Create a function named `calculate_numbers`.
2. **Positional Arguments (`*args`)**: Accept an arbitrary number of numerical inputs to process.
3. **Keyword Arguments (`**kwargs`)**: Accept settings to determine how to process the numbers. Look for a key named `operation`.
   * If `operation="add"` (or if no operation is provided), add all the numbers together.
   * If `operation="divide"`, take the first number and divide it sequentially by all following numbers.
4. **Empty Input**: If no numbers are passed into `*args`, the function must return `0`.
5. **Error Handling (`try-except`)**: Wrap your math execution inside a try block to handle the following exceptions:
   * **`ZeroDivisionError`**: Return the string `"Error: Cannot divide by zero!"` if a division by zero is attempted.
   * **`TypeError`**: Return the string `"Error: All arguments must be numbers!"` if a user passes a string or other invalid data type into `*args`.

---

## Starter Template

Copy the code below into your Python file to begin. Fill in the missing logic.

```python
def calculate_numbers(*args, **kwargs):
    # 1. Check if args is empty, return 0 if it is
    if not args:
        return 0
    
    # 2. Get the operation from kwargs (default to 'add')
    operation = kwargs.get('operation', 'add')
    
    # 3. Implement your math logic inside a try-except block
    try:
        if operation == 'add':
            # TODO: Add all numbers in args together
            pass
            
        elif operation == 'divide':
            # TODO: Divide the first number sequentially by the rest
            pass
            
    except ZeroDivisionError:
        # TODO: Handle division by zero error
        pass
    except TypeError:
        # TODO: Handle wrong data type error
        pass

# --- Test Cases (Uncomment to verify your work) ---
# print(calculate_numbers(10, 5, 2, operation="add"))     # Expected: 17
# print(calculate_numbers(100, 2, 5, operation="divide")) # Expected: 10.0
# print(calculate_numbers(10, 0, operation="divide"))     # Expected: Error: Cannot divide by zero!
# print(calculate_numbers(10, "five", operation="add"))   # Expected: Error: All arguments must be numbers!
# print(calculate_numbers())                              # Expected: 0
```
