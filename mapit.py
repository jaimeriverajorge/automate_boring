# This script will open up a Google maps page
# with the address that is passed in

import webbrowser, sys, pyperclip

sys.argv # ['mapit.py', '1326', 'Wye', 'Ct.']

# check if command line arguments were passed
# should be greater than 1 as the first argument will be the script name
if len(sys.argv) > 1:
    ## ['mapit.py', '1326', 'Wye', 'Ct.'] -> 1326 Wye Ct.
    address = ' '.join(sys.argv[1:])
else:
    # If the user did not pass in an address, it should be on the clipboard
    address = pyperclip.paste()

# https://www.google.com/maps/place/<ADDRESS>
webbrowser.open('https://www.google.com/maps/place/' + address)
#print('This is the address passed in: ' + address)
