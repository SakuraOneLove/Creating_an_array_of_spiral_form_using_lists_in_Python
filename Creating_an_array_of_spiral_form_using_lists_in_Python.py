# Creating an array of n by n size, filled with numbers from 1 to n ** 2 by spiral direction
n = int(input())  # Size of the array

a = [[0 for j in range(n)] for i in range(n)]  # Creating an 0-filled 2-dimensional list

# Filling the 2-dimensional list with numbers in spiral direction
m = 1
c = n // 2  # The number of circules
for i in range(c):  # Going through circules
    for h1 in range(i, n - 1 - i):  # Horizontal upper line of the spiral
        a[i][h1] = m
        m += 1
    for v1 in range(i, n - 1 - i):  # Vertical right line of the spiral
        a[v1][n - 1 - i] = m
        m += 1
    for h2 in range(n - 1 - i, i, -1):  # Horizontal bottom line of the spiral
        a[n - 1 - i][h2] = m
        m += 1
    for v2 in range(n - 1 - i, i, -1):  # Vertical left line of the spiral
        a[v2][i] = m
        m += 1

# Assigning the central value to the array if its size is odd number 
if n % 2 != 0:
    a[n // 2][n // 2] = m

# Showing the result in form of array
for i in range(n):
    if i != 0 or i != n - 1:
        print()
    for j in range(n):
        print(a[i][j], end=' ')

