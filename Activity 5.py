import os

if not os.path.exists('thinkdsp.py'):
    !wget https://github.com/AllenDowney/ThinkDSP/raw/master/code/thinkdsp.py
    
    from thinkdsp import SawtoothSignal

signal = SawtoothSignal(200)
duration = signal.period*3
segment = signal.make_wave(duration, framerate=10000)
segment.plot()
decorate(xlabel='Time (s)')

wave = signal.make_wave(duration=0.5, framerate=10000)
wave.apodize()
wave.make_audio()

spectrum = wave.make_spectrum()
spectrum.plot()
decorate(xlabel='Frequency (Hz)')