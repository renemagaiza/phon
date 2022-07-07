#!C:\Users\Rena\AppData\Local\Programs\Python\Python38\python.exe
import logging
logging.basicConfig(level=logging.WARNING, format="%(asctime)s - %(levelname)s - %(message)s")
total = 1
#logging.disable(logging.WARNING)
def factorial(n):
    #assert n < 0, "O valor passado em menor que 0 "
    total = 1
    for i in range(1, n + 1):
        total *= i
        logging.warning("O valor de i e %d e valor de total e %d"%(i, total))
def fatrecrusive(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fatrecrusive(n -1)

factorial(5)
fatrecrusive(5)
