# The following program draws a spiral when run while MS paint is open
# Taken from the Udemy course "Automate the Boring Stuff with Python Programming"
# Taught and written by Al Sweigart

import pyautogui

pyautogui.click() #click to put the cursor on MS Paint
distance = 300
while distance > 0:
    print(distance, 0)
    pyautogui.dragRel(distance, 0, duration=0.1) # move right
    distance = distance - 25
    print(0, distance)
    pyautogui.dragRel(0, distance, duration=0.1) # move down
    distance = distance - 25
    print(-distance, 0)
    pyautogui.dragRel(-distance, 0, duration=0.1) # move left
    distance = distance - 25
    print(0, -distance)
    pyautogui.dragRel(0, -distance, duration=0.1) # move up
    
