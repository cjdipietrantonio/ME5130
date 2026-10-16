r'''
Christian DiPietrantonio
ME5130: Advanced Heat and Mass Transfer
HW01: Problem 18B.19, Part (d):
  Plot the total oxygen uptake rate and $\xi_0$ as functions of $N$

'''

import numpy as np
import matplotlib.pyplot as plt

def core_radius(N):
    ''' Return the normalized core radius '''

    if N <= 6:
        return 0.0

    roots = np.roots([1.0, -1.5, 0.0, 0.5 - 3.0/N])     # xi^3 - 1.5xi^2 + (0.5 - 3/N) = 0
    real = roots[np.abs(roots.imag) < 1e-9].real
    return real[(real >= 0) & (real < 1)][0]


def main():
    N    = np.linspace(0, 50, 1001)
    xi_0 = np.array([core_radius(n) for n in N])
    W    = N/3 * (1 - xi_0**3)                         # W_02 / (4 \pi R D \rho_0)

    fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True, figsize=(6.5, 7))
    ax1.plot(N, xi_0)
    ax1.set_ylabel(r"Core Radius, $\xi_0$")
    ax2.plot(N, W, label='Non-Dimensional Uptake Rate with Oxygen-Free Core')
    ax2.plot(N, N/3, '--', color='gray', label='Non-Dimensional Uptake Rate without Oxygen-Free Core')
    ax2.set_ylabel(r'Non-Dimensional Uptake Rate, $W_{O_2}^*$')
    ax2.set_xlabel(r'$N$')
    ax2.legend(loc='lower right')
    for ax in (ax1, ax2):
        ax.axvline(6, color='gray', ls=':')
    fig.tight_layout()
    fig.savefig('DiPietrantonio_ME5130_HW02_18B19.png', dpi=300)

if __name__ == "__main__":
    main()
