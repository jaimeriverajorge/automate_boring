# A script to save all of the phone numbers and
# email addresses within a PDF document

import re, pyperclip

# TODO: Create a regex for phone numbers
phoneRegex = re.compile(r'''
# 415-555-0000, 555-0000, (415) 555-0000, 555-0000 ext 12345 

(
((\d\d\d) | (\(\d\d\d\)))?      # area code (optional)
(\s | -)                        # first separator
\d\d\d                          # first 3 digits
-                               # separator
\d\d\d\d                        # last 4 digits
((ext(\.)?\s |x) (\d{2,5}))?    # extension (optional)
)
''', re.VERBOSE)

# TODO: Create a regex for email addresses

emailRegex = re.compile(r'''

   [a-zA-Z0-9_.+]+   # name part
   @                 # @ symbol
   [a-zA-Z0-9_.+]+   # domain name

''', re.VERBOSE)

#emailRegex = re.compile(r"^\S+@\S+\.\S+$")
# TODO: Get the text off the clipboard
text = pyperclip.paste()

# TODO: Extrct the email / phone from the text
extractedPhone = phoneRegex.findall(text)
extractedEmail = emailRegex.findall(text)

allPhoneNumbers = []
for phoneNumber in extractedPhone:
    allPhoneNumbers.append(phoneNumber[0])

# TODO: Copy the extracted email/phone to the clipboard
results = '\n'.join(allPhoneNumbers) + '\n' + '\n'.join(extractedEmail)
pyperclip.copy(results)



