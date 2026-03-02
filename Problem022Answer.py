def minimumSteps(s):
    # Initialize a counter for the number of '1's seen so far
    ones = 0
    # Initialize a counter for the total number of swaps needed
    swaps = 0
    
    # Iterate through each character in the string
    for char in s:
        if char == '1':
            # If the character is '1', increment the 'ones' counter
            ones += 1
        else:  # char == '0'
            # If the character is '0', it needs to be swapped with all '1's before it
            swaps += ones
            
    # Return the total number of swaps needed to move all '1's to the right of all '0's
    return swaps

# Example usage
x = "1100101"
ans = minimumSteps(x)
print(ans)  # Output: 5