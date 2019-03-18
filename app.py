import requests

# Import the package and create an audio effects chain function.
from pysndfx import AudioEffectsChain

fx = (
    AudioEffectsChain()
    .reverb()
    .phaser()
    .delay()
    .reverse()
)

infile = 'sessionAmpd.wav'
outfile = 'processed_session.wav'

# Apply phaser and reverb directly to an audio file.
fx(infile, outfile)

# Or, apply the effects directly to a ndarray.
from librosa import load
y, sr = load(infile, sr=None)
y = fx(y)

# Apply the effects and return the results as a ndarray.
y = fx(infile)

# Apply the effects to a ndarray but store the resulting audio to disk.
fx(y, outfile)





'''
print("Hello World")
my_ip=requests.get("http://bot.whatismyipaddress.com/")
print(my_ip.text)
'''

