"""
A simple python script to print a box of specific height and width
Used for examples of raising exceptions 
***********
*         *
*         *
*         *
***********

"""

def boxPrint(symbol, width, height):
    if len(symbol) != 1:
        raise Exception("Symbol length must be equal to 1.")
    if (width < 2) or (height < 2):
        raise Exception('"width" and "height" must be greater or equal to 2.')

    print(symbol * width)

    for i in range(height - 2):
        print(symbol + (' ' * (width - 2) + symbol))

    print(symbol * width)

boxPrint('*', 1, 5)
boxPrint('O', 5, 10)
