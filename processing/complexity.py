import numpy as np

def complexity(x):
    if not len(x):
        return 0
        
    switch = 0
    for i in range(1, len(x)):
        for j in range(3):
            a, b = x[i-1][j], x[i][j]
            a /= abs(a)
            b /= abs(b)
            if a != b: 
                switch += 1
                
    return (switch) * 10 / (270)