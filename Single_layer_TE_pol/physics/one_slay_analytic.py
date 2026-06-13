import numpy as np

def _kz_count(k, kx):
    kz = np.sqrt(k**2 - kx**2 + 0j)
    return np.where(np.imag(kz) >= 0, kz, -kz)

def frenel_r(q1, q2):
    """Frenele`s coef"""
    return (q1 - q2) / (q1 + q2)

def r_total(k_val, h, theta):
    k_val = np.array(k_val, dtype=complex)
    k0, k1, k2 = k_val[0], k_val[1], k_val[2]

    kx = k0 * np.sin(theta)
    kz0 = _kz_count(k0, kx)
    kz1 = _kz_count(k1, kx)
    kz2 = _kz_count(k2, kx)

    q0, q1, q2 = kz0, kz1, kz2

    r01 = frenel_r(q0, q1)
    r12 = frenel_r(q1, q2)

    phase = np.exp(2j*kz1*h)

    return (r01 + r12*phase) / (1 + r01*r12*phase)