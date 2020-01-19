import numpy as np

def vigour(x):
    # should be a list of vectors
    total = 0
    for vec in x:
        total += np.linalg.norm(vec)

    mean = total / len(x)
    print(mean)
    return (mean - 0.85) * 10 / (1.35 - 0.85)