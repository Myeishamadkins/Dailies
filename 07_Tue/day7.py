# Given a list of integers, return True if there are more 1s

# than 0s. Otherwise, return False.

# Use a single loop.

# Do not use any counting helpers (`l.count`, `collections.Counter`)

n = [1, 1, 1, 0, 0, 0, 0]
ones = []
zeros = []
for i in n:
    if i == 1:
        ones.append(i)
    else:
        zeros.append(i)
if len(ones) > len(zeros):
    print('True')
else:
    print('false')

ones = 0
zeros = 0

for i in n:
    if i == 1:
        ones += 1
    elif i ==0:
        zeros += 1
print(ones > zeros)

ones = 0
zeros = 0
i = 0

while i < len(n):
    if i == 1:
        ones += 1
    elif i == 0:
        zeros += 1
    i += 1
print(ones > zeros)
