import sys,pathlib
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.signal import savgol_filter, hilbert, find_peaks

CSV_FILE  = "new.csv"          
DISP_UM   = 10.1 
WINDOW    = 31                  # SavGol window
POLY      = 3
THR_MIN   = 0.055               # accept peaks ≥ 5.5 % 
THR_MAX   = 0.90                # dont allow big spikes
THR_PROM  = 0.027               
DIST_S    = 8.0e-6   


def count_fringes(csv_path, *, plot=True):
    """
    Count bright Michelson fringes in an oscilloscope CSV.

    Parameters
    ----------
    csv_path : str | pathlib.Path
        Two-column CSV: column 0 = time [s], column 1 = voltage/intensity.
    plot : bool
        If True, show a diagnostic plot with markers.

    Returns
    -------
    bright_count : int
    """
    # data
    p = pathlib.Path(csv_path)
    df = pd.read_csv(p)
    t = df.iloc[1:, 0].astype(float).values
    y = df.iloc[1:, 1].astype(float).values

    # smooth and detrend
    y_s = savgol_filter(y, WINDOW, POLY)
    y_d = y_s - np.median(y_s)

    # envelope normalise
    env = np.abs(hilbert(y_d)); env += env.mean()*1e-3
    y_n = y_d / env

    dt = np.mean(np.diff(t))
    dist_pts  = max(1, int(DIST_S / dt))

    max_idx, _ = find_peaks(
        y_n,
        height=(THR_MIN, THR_MAX),
        prominence=THR_PROM,
        distance=dist_pts
    )
    if plot:
        plt.figure(figsize=(8, 3.5))
        plt.plot(t, y_n, lw=1)
        plt.plot(t[max_idx], y_n[max_idx], "r^", label=f"{len(max_idx)} maxima")
        plt.title(f"{p.name}: {len(max_idx)} bright fringes")
        plt.xlabel("Time (s)"); plt.ylabel("normalised amplitude")
        plt.legend(); plt.tight_layout(); plt.show()

    return len(max_idx)

def wavelength(displacement_m, fringe_count):
    """
    λ = 2·Δs / N 
    """
    if fringe_count <= 0:
        raise ValueError("fringe count must be positive")
    return 2.0 * displacement_m / fringe_count

if __name__ == "__main__":
    bright = count_fringes(CSV_FILE, plot=True)
    print(f"Bright peaks = {bright}")

    lam = wavelength(DISP_UM * 1e-6, bright)       # µm → m
    print(f"Estimated λ = {lam*1e9:.2f} nm "
          f"(mirror travel {DISP_UM:.3f} µm)")

