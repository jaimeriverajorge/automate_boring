print('My name is')
for i in range(5):
    print('Jimmy Five Times ' + str(i))

# What Carl Gauss did in his head, adding all the numbers from 1 to 100
# he figured out that there were 50 pairs of numbers that would total to 100
# ex: 1 + 99, 2 + 98
# then add the middle 50, for a total of 5050
total = 0
for num in range(101):
    total = total + num
print(total)
