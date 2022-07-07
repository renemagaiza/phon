#!C:\Users\Rena\AppData\Local\Programs\Python\Python38\python.exe
import logging
logging.basicConfig(filename='myProgramLog.txt', level=logging.INFO, format=' %(asctime)s - %(levelname)s - %(message)s')
logging.debug('Start of program')
#os.chdir("C:\\Users\\Rena\\Documents\\phon")
def factorial(n):
    logging.debug('Start of factorial(%s%%)' % (n))
    total = 1
    for i in range(1, n + 1):
        total *= i
        logging.info('i is ' + str(i) + ', total is ' + str(total))
    logging.debug('End of factorial(%s%%)' % (n))
    return total
print(factorial(5))
total=7
logging.debug('End of program')
