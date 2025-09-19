# Guessing Game Assignment

## Overview
Create a guessing game function that uses a while loop to let the user guess a number until they get it correct.

## Requirements

### Function Structure
Your `guessing_game` function should:

1. **Set the target number to 15**
2. **Use a while loop** to keep asking for guesses
3. **Provide hints** (too high/too low) for each guess
4. **Return a success message** when the correct number is guessed
5. **Use input()** to get user guesses

## Expected Behavior

### Example Usage
```python
def guessing_game():
    # Your implementation here
    pass

# When called, it should work like this:
# Enter your guess: 10
# Too low! Try again.
# Enter your guess: 20
# Too high! Try again.
# Enter your guess: 15
# Congratulations! You guessed it!
```

### Test Cases
Your implementation should pass all the following test cases:

1. **Correct guess first try**: User guesses 15 immediately
2. **Multiple guesses**: User tries several wrong numbers before getting it right
3. **High/low hints**: Function provides appropriate feedback
4. **Negative number**: Handles negative input correctly
5. **Zero**: Handles zero input correctly
6. **Large number**: Handles large numbers correctly
7. **While loop usage**: Function uses while loop structure
8. **Target is 15**: The target number is exactly 15

## Implementation Tips

- Use `input()` to get user input
- Convert input to integer with `int()`
- Use a while loop with a condition that continues until correct guess
- Provide clear feedback messages
- Return a success message when done
- The target number should be hardcoded as 15


