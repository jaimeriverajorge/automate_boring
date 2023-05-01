# this script counts the number of times each letter appears in a message and prints out the count

import pprint

message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {} #'r' : 12

for character in message.upper():
    count.setdefault(character, 0)
    count[character] = count[character] + 1

# printing the dictionary in a random order
print(count)

# using the pprint module to print the dictionary in a nicer way
pprint.pprint(count)
