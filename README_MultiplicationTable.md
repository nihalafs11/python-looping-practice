# Multiplication Table Assignment

## Overview
Create a multiplication table function that uses nested for loops to print a multiplication table.

## Requirements

### Function Structure
Your `multiplication_table` function should:

1. **Take a parameter `n`** for the table size (1 to n)
2. **Use nested for loops** to generate the table
3. **Print each multiplication** in the format "a x b = c"
4. **Print one multiplication per line**
5. **Use print()** to display the table

## Expected Behavior

### Example Usage
```python
def multiplication_table(n):
    # Your implementation here
    pass

# When called with multiplication_table(3), it should print:
# 1 x 1 = 1
# 1 x 2 = 2
# 1 x 3 = 3
# 2 x 1 = 2
# 2 x 2 = 4
# 2 x 3 = 6
# 3 x 1 = 3
# 3 x 2 = 6
# 3 x 3 = 9
```

### Test Cases
Your implementation should pass all the following test cases:

1. **1 to 5 table**: Complete 5x5 multiplication table
2. **1 to 3 table**: Complete 3x3 multiplication table
3. **1 to 10 table**: Complete 10x10 multiplication table
4. **Nested loops**: Function uses nested for loop structure
5. **Single number**: Handles table size of 1
6. **Correct format**: Output follows "a x b = c" format

## Implementation Tips

- Use two nested for loops (outer and inner)
- Outer loop: 1 to n (inclusive)
- Inner loop: 1 to n (inclusive)
- Print each multiplication as "a x b = c"
- Use `print()` function to display results
- Make sure to include all combinations

