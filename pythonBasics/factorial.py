# A script that has a sample function that is supposed to return
# the factorial of the number given
# There is an error on purpose within the script to make use of the
# logging feature
import logging
#if you want to log to a text file, just add filename='mylog.txt'
# to the beginning of the logging.basicConfig() statement

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
# The line below disables the logs and prevents them from printing anything
#logging.disable(logging.CRITICAL)


logging.debug('Start of program')

def factorial(n):
    logging.debug('Start of factorial(%s)' % (n))
    total = 1
    for i in range(1, n +1):
        total *= i
        logging.debug('i is %s, total is %s' % (i, total))

    logging.debug('Return value is %s' % (total))
    return total

print(factorial(5))
logging.debug('End of Program')

# There are five levels to logging, in order from lowest importance to highest:
# logging.DEBUG
# logging.INFO
# logging.WARNING
# logging.ERROR
# logging.CRITICAL
