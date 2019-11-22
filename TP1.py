from __future__ import print_function, division
import thinkdsp
import thinkplot
import numpy as np
from ipywidgets import interact, interactive, fixed
import ipywidgets as widgets
from IPython.display import display

wavesax = thinkdsp.read_wave("C:\som sax.wav")
waveguitar = thinkdsp.read_wave('C:\som guitarra.wav')

spectrumSax = wavesax.make_spectrum()
spectrumSax.plot(high=6000)
spectrumGuitar = waveguitar.make_spectrum()
spectrumGuitar.plot(high=1000)

wavesax.normalize()
wavesax.plot()
segment = wavesax.segment(start=1.1, duration=1)
segment.make_audio()
segment.plot()
segment.segment(start=1.1, duration=0.005).plot()

spectrum = segment.make_spectrum()
spectrum.plot(high=550)

spectrum.low_pass(2000)
spectrum.make_wave().make_audio()

spectrum.peaks()[:10]

waveguitar.normalize()
waveguitar.make_audio()

waveguitar.plot()

segment_guitar = waveguitar.segment(start=1.1, duration=1)
segment_guitar.make_audio()

segment_guitar.plot()
segment_guitar.segment(start=1.1, duration=0.005).plot()

spectrum_guitar = segment_guitar.make_spectrum()
spectrum_guitar.plot(high=410)

spectrum_guitar.low_pass(2000)
spectrum_guitar.make_wave().make_audio()

spectrum_guitar.peaks()[:10]


cos_sig_sax = thinkdsp.CosSignal(freq=492, amp=1.0, offset=0)
cos_sig_guitar = thinkdsp.CosSignal(freq=401, amp=1.0, offset=0)
cos_sig = cos_sig_sax + cos_sig_guitar
cos_sig.plot()
thinkplot.config(xlabel='Time (s)')

wave2 = cos_sig.make_wave(duration=1)
wave2.apodize()

wave2.make_audio()


