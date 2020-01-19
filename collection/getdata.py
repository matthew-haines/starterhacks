import sys
from serial import Serial
import time
import csv
import pandas

if __name__ == '__main__':
    # parameters are device, baud, and then output file
    if len(sys.argv) != 4:
        print("Bad parameters")

    ser = Serial(sys.argv[1], sys.argv[2])
    data = []
    time.sleep(2)
    for i in range(0,1000):

        temp = ser.readline().decode().rstrip()
        x, y, z = temp.split(' ')
        data.append({'x': x, 'y': y, 'z': z})
        time.sleep(1/60)
        
    df = pandas.DataFrame(data)

    df.to_csv(sys.argv[3], sep=',',index=False)

