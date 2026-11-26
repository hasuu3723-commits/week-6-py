
# Python Week 6 Assignment: Safe Tools and Error Handling

## Files

- safe_tools.py: Contains three safe functions that handle division errors, invalid number conversions, and missing dictionary keys.
- README.md: Provides information about the assignment and explains error handling.

## Reflection

An if check cannot catch "abc" on its own because "abc" is text and cannot be converted into a whole number using int(). Python raises a ValueError during conversion. Using try and except allows the program to catch this error and display a friendly message instead of crashing.
