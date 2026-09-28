"""Reusable ecological ODE functions for the forest pest model."""
import numpy as np

def climate_growth_rate(t, r_s, amplitude=0.0, period=1.0):
    """Return foliage growth rate under periodic climate forcing."""
    return r_s - amplitude * np.sin(2 * np.pi * t / period)

def stable_system(t, y, p):
    """Two-state budworm/effective-foliage model."""
    B, ES = np.maximum(y, 0.0)
    foliage = max(ES / p["E0"], p["eps"])
    dB = p["r_B"] * B * (1 - B / (p["K_B"] * foliage)) - p["beta"] * B**2 / (p["alpha"]**2 + B**2)
    dES = p["r_S"] * ES * (1 - ES / p["K_S"]) - p["decay"] * ES - p["P_B"] * B
    return np.array([dB, dES])

def dual_pest_system(t, y, p):
    """Three-state budworm, bark-beetle, and foliage model."""
    B, C, S = np.maximum(y, 0.0)
    S_safe = max(S, p["eps"])
    climate_r = climate_growth_rate(t, p["r_S"], p["A"], p["period"])
    dB = p["r_B"] * B * (1 - B / (p["K_B"] * S_safe)) - p["delta"] * B * C - p["beta"] * B**2 / (p["alpha"]**2 + B**2) - p["mu"] * B
    dC = p["r_C"] * C * (1 - C / (p["K_C"] * S_safe)) - p["delta"] * B * C
    dS = climate_r * S * (1 - S / p["K_S"]) - p["decay"] * S - p["P_B"] * B - p["P_C"] * C
    return np.array([dB, dC, dS])
