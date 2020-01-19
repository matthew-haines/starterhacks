import numpy as np
from typing import Tuple

def getstart(x: np.ndarray) -> int:
    # x is just a vector
    threshold = 0.05
    start = 0
    for i in range(len(x) - 21):
        if (np.std(x[i:i+20]) > threshold):
            start = i + 10
            break

    return start
