import sys
import numpy as np
from length import getstartend
from vigour import vigour
from complexity import complexity
import pandas as pd

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Bad arguments")
        sys.exit(0)
    
    # read file somewhere
    data = pd.read_csv(sys.argv[1])
    data = data.drop(0)
    start, end = getstartend(data['x'])
    length = end - start
    handshake = data.values[start:end]
    vigval = vigour(handshake)
    compval = complexity(handshake)

    print("Vigour: %s, Complexity: %s, Length: %s" % (vigval, compval, length))