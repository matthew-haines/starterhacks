import sys
from serial import Serial
import time
import csv

if __name__ == '__main__':
    # parameters are device, baud, and then output file
    if len(sys.argv) != 3:
        print("Bad parameters")

    ser = Serial(sys.argv[1], sys.argv[2])
    data = []
    time.sleep(2)
    print(ser.readline())
