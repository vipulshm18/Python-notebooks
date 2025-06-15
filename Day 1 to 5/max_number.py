numbers = [12,1484,1285,154,6589,6454,6589,454,121,548,1465,15487,1245847,12544,487,2145]

max_number = 0

for number in numbers:
    if max_number < number:
        max_number = number

print(max_number)