import numpy as np
from typing import Tuple

def getstartend(x: np.ndarray) -> Tuple[int, int]:
    # x is just a vector
    threshold = 0.05
    start = 0
    for i in range(len(x) - 21):
        if (np.std(x[i:i+20]) > threshold):
            start = i + 10
            break

    end = len(x)-1
    for i in range(start, len(x)-41):
        if (np.std(x[i:i+40]) < threshold):
            end = i
            break

    return start, end
