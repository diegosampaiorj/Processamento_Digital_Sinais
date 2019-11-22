from __future__ import print_function, division

import thinkdsp
import thinkplot
import numpy as np
from ipywidgets import interact, interactive, fixed
import ipywidgets as widgets
from IPython.display import display

cos_sig = thinkdsp.CosSignal(freq=440, amp=1.0, offset=0)
sin_sig = thinkdsp.SinSignal(freq=880, amp=0.5, offset=0)

#cos_sig.plot()
#sin_sig.plot()
#thinkplot.config(xlabel='Time (s)')

mix = sin_sig + cos_sig
mix

wave = mix.make_wave(duration=0.5, start=0, framerate=11025)
wave
wave.make_audio()

from IPython.display import Audio
audio = Audio(data=wave.ys, rate=wave.framerate)
audio

wavesax = thinkdsp.read_wave("C:\som sax.wav")
wavesax.make_audio()
waveguitar = thinkdsp.read_wave('C:\som guitarra.wav')


