# A simple script that prompts the user to type 'your name'
# and repeats the prompt until they do so.
# The joke is that the user will type their actual name,
# and think that it is a broken loop until they figure it out.
#

name = ''
while name != 'your name':
    print('Please type your name.')
    name = input()
print('Thank you!')
