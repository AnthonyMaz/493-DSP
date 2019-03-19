from pysndfx import AudioEffectsChain

fx = (
    AudioEffectsChain()
    .reverb()
    .phaser()
    .delay()
    .reverse()
)

infile = 'sample.wav'
outfile = 'processed_sample.wav'

fx(infile, outfile)


