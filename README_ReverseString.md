# Reverse String Assignment

## Overview
Create a function that reverses a string using only loops (no slicing allowed).

## Requirements

### Function Structure
Your `reverse_string` function should:

1. **Take a string parameter**
2. **Use a loop** to build the reversed string
3. **Return the reversed string**
4. **NO SLICING ALLOWED** (no [::-1] or similar)
5. **Build character by character** using loop

## Expected Behavior

### Example Usage
```python
def reverse_string(text):
    # Your implementation here
    pass

# Examples:
print(reverse_string("hello"))     # Output: "olleh"
print(reverse_string("12345"))     # Output: "54321"
print(reverse_string("racecar"))   # Output: "racecar"
print(reverse_string(""))          # Output: ""
```

### Test Cases
Your implementation should pass all the following test cases:

1. **Simple string**: Reverse "hello" to "olleh"
2. **Single character**: Reverse "a" to "a"
3. **Empty string**: Reverse "" to ""
4. **Palindrome**: Reverse "racecar" to "racecar"
5. **Numbers**: Reverse "12345" to "54321"
6. **Mixed characters**: Reverse "a1b2c3" to "3c2b1a"
7. **Spaces**: Reverse "hello world" to "dlrow olleh"
8. **Special characters**: Reverse "!@#$%" to "%$#@!"
9. **Long string**: Reverse longer strings correctly
10. **Loop usage**: Function uses loop structure (no slicing)

## Implementation Tips

- Use a for loop or while loop to iterate through characters
- Build the reversed string character by character
- Start from the end of the string and work backwards
- Use string concatenation to build the result
- NO SLICING ALLOWED - must use loops only

