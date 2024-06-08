# Многопоточность

from time import sleep
from threading import Thread


def main():
    print("Process 1")
    sleep(3)
    print("Process One Good!")


def main2():
    print("Process 2")
    sleep(3)
    print("Process Two Good!")


one_func = Thread(target=main)
one_func.start()
two_func = Thread(target=main2)
two_func.start()
