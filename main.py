import sys
import numpy as np
from processing.length import getstart
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
from serial import Serial

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

def process(data: pd.DataFrame) -> Dict:
    # read file somewhere
    start = getstart(data['x'])
    length = len(data['x']) - start
    handshake = data.values[start:]
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
def queryNew():
    ser = Serial('/dev/tty.tty.usbmodem1421', 115200)
    data = []
    tempx = np.zeros((1000))
    time.sleep(2)
    for i in range(700):
        temp = ser.readline().decode().rstrip()
        x, y, z = temp.split(' ')
        data.append({'x': x, 'y': y, 'z': z})
        temp[i] = x
        if i > 40:
            if np.std(tempx[i-39:i+1]) < 0.05:
                break
        time.sleep(1/60)
        
    df = pd.DataFrame(data)
    df = df.drop(0)

    return json.dumps(process(df))

@app.route('/dummy')
def dummyQuery():
    df = pd.read_csv('collection/coolShake.csv')
    df = df.drop(0)
    return json.dumps(process(df))

@app.route('/all')
def queryDB():
    samples = database.load_data()
    for sample in samples:
        del sample['raw']

    return json.dumps(samples)

if __name__ == '__main_':
    app.run(debug=True, port=5000) #run app in debug mode on port 5000