# The following Python program demonstrates basic usage of the
# pyautogui module, which is used to control the mouse programatically

import pyautogui

# this gets the dimensions / size of your screen and sets them to variables
width, height = pyautogui.size()

# this function returns the current cursor position
pyautogui.position()

# the moveTo function moves the mouse to entered position
# it has a fail-safe that is triggered if the mouse is currently
# at a corner of the screen
pyautogui.moveTo(10, 10)

# the above function does it instantly, but you can slow it down with the
# duration parameter
pyautogui.moveTo(500, 500, duration = 1.5)

# use moveRel to move a number of pixels in a certain direction
pyautogui.moveRel(100, 0, duration = 2)

# use the click function to have the mouse click on a specific screen position
# it is best to use pyautogui.position() to get the coordinates of where you
# would like to click
pyautogui.click(393, 177)


# The typewrite function will type whatever the input is
# it is recommended to first send a click to where you want to type
pyautogui.typewrite('Hello world', interval=0.2)

# Use the screenshot function to take a screenshot
# you can optionally pass in a file location/name
pyautogui.screenshot()
