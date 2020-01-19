import sys
import numpy as np
from processing.length import getstartend
from processing.vigour import vigour
from processing.complexity import complexity
import pandas as pd
from typing import Tuple, List, Dict
from scipy import signal
import scipy
import database.database as database
from flask import Flask, request
import json
import time

app = Flask(__name__)

SAMPLING_FREQUENCY = 60

def fft(data: np.ndarray, hertz: int) -> Tuple[np.ndarray, np.ndarray]:
    x = np.linspace(0, len(data)/hertz, len(data), endpoint=False)
    y = scipy.fft.fft(signal.detrend(data))
    freqs = scipy.fft.fftfreq(len(x)) * hertz
    length = len(freqs) // 2
    return freqs[:length], np.abs(y[:length])

def gettopfreqs(freqs: np.ndarray, powers: np.ndarray, n: int) -> List:
    indices = np.argpartition(powers, -n)[-n:]
    return [[freqs[i], powers[i]] for i in indices]

def buildfingerprint(data: np.ndarray, hertz: int) -> List:
    freqs, powers = fft(data, hertz)
    tops = gettopfreqs(freqs, powers, 8)
    out = list(set([round(top[0] * 4)/4 for top in tops]))
    out.sort()
    return out

def process(inputfile: str) -> Dict:
    # read file somewhere
    data = pd.read_csv(inputfile)
    data = data.drop(0)
    start, end = getstartend(data['x'])
    length = end - start
    handshake = data.values[start:end]
    vigval = vigour(handshake)
    compval = complexity(handshake)

    fingerprint = buildfingerprint(handshake[:, 0], SAMPLING_FREQUENCY)
    
    sample = {
        "fingerprint": fingerprint,
        "raw": handshake,
        "vigour": vigval,
        "complexity": compval,
        "length": length,
        "timestamp": time.time()
    }

    # database
    db = database.load_data()
    uniqueness = database.uniqueness(sample, db)
    sample['uniqueness'] = uniqueness
    db.append(sample)
    database.save_data(db)
    del sample['raw']
    return sample

@app.route('/new')
def query():
    return json.dumps(process('collection/hand1.csv'))

if __name__ == '__main_':
    app.run(debug=True, port=5000) #run app in debug mode on port 5000