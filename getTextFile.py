# The following program gets a text file from the web using
# using the 'requests' module, then writes it to a new text
# file that will be stored locally

import requests

# get the text file (example file is the full book of Romeo and Juliet)
res = requests.get('https://automatetheboringstuff.com/files/rj.txt')

# verify that the text was stored successfuly
#print(res.text[:500])

#make a new file where it will be written to, must be opened
# using 'wb' (write-binary)
playFile = open('RomeoAndJuliet.txt', 'wb')

# move through the text and write to the file
# using the res.iter_content() function
for chunk in res.iter_content(100000):
    playFile.write(chunk)

playFile.close()
