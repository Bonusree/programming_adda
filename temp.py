# Declare variables
x1, y1, x2, y2, dx, dy, x, y, step = 0, 0, 0, 0, 0, 0, 0, 0, 0

# Input values
x1 = int(input("Enter x1: "))
y1 = int(input("Enter y1: "))
x2 = int(input("Enter x2: "))
y2 = int(input("Enter y2: "))

# Calculate differences
dx = x2 - x1
dy = y2 - y1

# Determine step
if abs(dx) >= abs(dy):
    step = abs(dx)
else:
    step = abs(dy)

# Calculate increments
xinc = dx / step
yinc = dy / step

# Set initial point
x = x1
y = y1

# Draw line
for i in range(step):
    print(round(x), round(y))
    x += xinc
    y += yinc

# Print final point
print(round(x), round(y))
