# Ask the user for a positive integer (`x`)
# For each number (`n`) less than `x`,

# print whether or not `n` is a factor of `x`.

# Example:
# ```

# x: 12

# 1 is a factor of 12

# 2 is a factor of 12

# 3 is a factor of 12

# 4 is a factor of 12

# 5 is not a factor of 12

# 6 is a factor of 12

# 7 is not a factor of 12

# 8 is not a factor of 12

# 9 is not a factor of 12

# 10 is not a factor of 12

# 11 is not a factor of 12

# ```

x = int(input("Please enter a positive integer: "))

# for n in range(1, x):
#     if x % n == 0:
#         print(f"{n} is a factor of {x}")
#     else:
#         print(f"{n} is not a factor of {x}")

n = 1
while (n < x and n != 0):
    if x % n == 0:
        print(f"{n} is a factor of {x}")
    else:
        print(f"{n} is not a factor of {x}")
    n += 1
