import numpy as np

def vigour(x: list) -> float:
    # should be a list of vectors
    total = 0.0
    for vec in x:
        total += np.linalg.norm(vec)
    if (len(x)):
        mean = total / len(x)
        return (mean - 0.9) * 10 / (1.35 - 0.9)

    return 0.0