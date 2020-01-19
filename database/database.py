import pickle
from typing import List, Dict

"""
{
    "fingerprint": [rounded to 0.25],
    "timedata": numpy array
    "vigour": float
    "complexity": float,
    "length": int
}
"""

def load_data() -> List:
    try:
        with open("database/main.dat", "rb") as f:
            samples = pickle.load(f)
    except:
        print("Database did a rip")
        samples = []
    
    return samples

def save_data(data: List):
    with open("database/main.dat", "wb") as f:
        pickle.dump(data, f)

def similarity(fingerprint1: List, fingerprint2: List) -> float:
    similarity = 0
    for i in range(min(len(fingerprint1), len(fingerprint2))):
        if (fingerprint1[i] in fingerprint2):
            similarity += 1
        
    return similarity / max(len(fingerprint1), len(fingerprint2))

def uniqueness(sample: Dict, others: List) -> float:
    similarities = 0
    for othersample in others:
        similarities += similarity(sample['fingerprint'], othersample['fingerprint'])

    return similarities / max(len(others), 1)

def printdb(data: List):
    for sample in data:
        print(sample)
