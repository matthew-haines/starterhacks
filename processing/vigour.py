import numpy as np

def vigour(x):
    # should be a list of vectors
    total = 0
    for vec in x:
        total += np.linalg.norm(vec)

    mean = total / len(x)
    return (mean - 1.08) * 10 / 2