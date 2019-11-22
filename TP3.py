from __future__ import print_function, division
import thinkdsp
import thinkplot
import numpy as np
from ipywidgets import interact, interactive, fixed
import ipywidgets as widgets
from IPython.display import display

wavesax = thinkdsp.read_wave("C:\som sax.wav")
waveguitar = thinkdsp.read_wave('C:\som guitarra.wav')

wavesax.make_audio()
waveguitar.make_audio()

spectrumSax = wavesax.make_spectrum()
spectrumSax.plot()

spectrumGuitar = waveguitar.make_spectrum()
spectrumGuitar.plot()

spectrumSax = wavesax.make_spectrum()
spectrumSax.plot(high=6000)

spectrumGuitar = waveguitar.make_spectrum()
spectrumGuitar.plot(high=1000)

spectrumSax.peaks()[:10]
spectrumGuitar.peaks()[:10]

cos_sig_sax = thinkdsp.CosSignal(freq=492, amp=1.0, offset=0)
cos_sig_guitar = thinkdsp.CosSignal(freq=401, amp=1.0, offset=0)
cos_sig = cos_sig_sax + cos_sig_guitar
cos_sig.plot()
thinkplot.config(xlabel='Time (s)')

sin_sig_sax = thinkdsp.SinSignal(freq=492, amp=1.0, offset=0)
sin_sig_guitar = thinkdsp.SinSignal(freq=401, amp=1.0, offset=0)
sin_sig = sin_sig_sax + sin_sig_guitar
sin_sig.plot()
thinkplot.config(xlabel='Time (s)')

wave2 = cos_sig.make_wave(duration=1)
wave2.apodize()
wave2.make_audio()

wave3 = sin_sig.make_wave(duration=1)
wave3.apodize()
wave3.make_audio()