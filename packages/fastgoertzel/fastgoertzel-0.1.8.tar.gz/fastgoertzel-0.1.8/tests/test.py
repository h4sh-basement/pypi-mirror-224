import numpy as np
import pandas as pd

import fastgoertzel as G


def wave(amp, freq, phase, x):
    return amp * np.sin(2*np.pi * freq * x + phase)


x = np.arange(0, 512)
y = wave(1, 1/128, 0, x)

amp, phase = G.goertzel(y, 1/128)
print(f'Goertzel Amp: {amp:.4f}, phase: {phase:.4f}')

# Compared to max amplitude FFT output 
ft = np.fft.fft(y)
FFT = pd.DataFrame()
FFT['amp'] = np.sqrt(ft.real**2 + ft.imag**2) / (len(y) / 2)
FFT['freq'] = np.fft.fftfreq(ft.size, d=1)
FFT['phase'] = np.arctan2(ft.imag, ft.real)

max_ = FFT.iloc[FFT['amp'].idxmax()]
print(f'FFT amp: {max_["amp"]:.4f}, '
        f'phase: {max_["phase"]:.4f}, '
        f'freq: {max_["freq"]:.4f}')
