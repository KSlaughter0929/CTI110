# CTI-110
# P3T1 - Areas of Retangles
# Kyle Slaughter
# 03/09/2020
#

# Get dimensions of Rectangle 1.
length1 = int(input('Enter the length of rectangle1: '))
width1 = int(input('Enter the wiidth of rectangle1: '))

# Get dimensions of Rectangle 2.
length2 = int(input('Enter the length of rectangle2: '))
width2 = int(input('Enter the width of rectangle2: '))

# Calculte the areas of both rectangles.
area1 = length1 * width1
area2 = length2 * width2

# Determine which rectangle has the greater area.
if area1 > area2:
    print('Rectangle 1 has the greater area.')
elif area2 > area1:
    print('Rectangle 2 has the greater area.')
else:
    print('Both rectangles have the same area.')
