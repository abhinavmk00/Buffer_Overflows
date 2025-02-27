#!/usr/bin/python3

def generate_pattern(length):
    pattern = ''
    parts = []
    for upper in range(65, 91):  # uppercase A-Z
        for lower in range(97, 123):  # lowercase a-z
            for digit in range(48, 58):  # numbers 0-9
                parts.append(chr(upper) + chr(lower) + chr(digit))
                if len(pattern) + 3 <= length:
                    pattern += chr(upper) + chr(lower) + chr(digit)
    return pattern[:length]

# Generate pattern
pattern = generate_pattern(100)
print(pattern)

# Save to file
with open('pattern.txt', 'w') as f:
    f.write(pattern)
