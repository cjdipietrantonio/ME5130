r'''
Christian DiPietrantonio
ME5130: Advanced Heat and Mass Transfer
Midterm Exam: Take-Home
Problem 02
'''

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve


a = 1.0          # m
b = 1.0          # m
k = 0.8          # W/m-K
h = 10.0         # W/m^2-K
T0 = 100.0       # K
H = h / k        # 1/m
n_terms = 1000   # number of eigenvalues, enough for the sum to converge   

def eigen_eq(bm):
    return bm * np.sin(bm * a) - H * np.cos(bm * a)

def eigenvalues(n):
    beta = np.zeros(n)
    for m in range(1, n + 1):
        guess = (m - 0.75) * np.pi / a          # guess in the middle of each solution interval
        beta[m - 1] = fsolve(eigen_eq, guess)[0]
    return beta 


def print_eigenvalues(beta):
    print('+-----+----------------+')
    print('|  m  | beta_m (1/m)   |')
    print('+-----+----------------+')
    for m, bm in enumerate(beta, start=1):
        print(f'| {m:3d} | {bm:14.4f} |')
    print('+-----+----------------+')

def temperature_dist(x, y, beta):
    T = np.zeros_like(x)
    for bm in beta:
        norm_fac = 2 * (bm**2 + H**2) / (a * (bm**2 + H**2) + H)
        #Y_ratio = (bm * np.cosh(bm * (b - y)) + H * np.sinh(bm * (b - y))) / (bm * np.cosh(bm * b) + H * np.sinh(bm * b))
        Y_ratio = np.exp(-bm * y)* ((bm + H) + (bm - H) * np.exp(-2 * bm * (b - y)))/ ((bm + H) + (bm - H) * np.exp(-2 * bm * b)) #avoid overflow errors
        T += norm_fac * (T0 * np.sin(bm * a) / bm) * np.cos(bm * x) * Y_ratio
    return T

def plot_contour(x, y, T, filename):
    isotherms = np.arange(10, 100, 10)
    column    = T[:, np.argmin(np.abs(x - 0.2))]
    spots = [(0.2, np.interp(L, column[::-1], y[::-1])) for L in isotherms]

    fig, ax = plt.subplots(figsize=(7, 6))
    cf = ax.contourf(x, y, T, levels=np.linspace(0, T.max(), 101), cmap="Reds")
    cs = ax.contour(x, y, T, levels=isotherms, colors="black", linewidths=0.8)
    for label in ax.clabel(cs, fmt="%.0f K", fontsize=9, manual=spots):
        label.set_bbox(dict(facecolor="white", edgecolor="none", pad=1))
    fig.colorbar(cf, ax=ax, label="$T$ (K)", ticks=np.arange(0, 101, 10))
    ax.set_xlabel("$x$ (m)")
    ax.set_ylabel("$y$ (m)")
    ax.set_title("Temperature Distribution $T(x, y)$")
    ax.set_aspect("equal")
    fig.savefig(filename, dpi=300, bbox_inches="tight")

def main():
    beta = eigenvalues(n_terms)

    # 2a: print the first ten eigenvalues
    print_eigenvalues(beta[:10])

    # 2b: create contour plot
    x = np.linspace(0, a, 501)
    y = np.linspace(0, b, 501)
    xx, yy = np.meshgrid(x, y)
    T = temperature_dist(xx, yy, beta)
    plot_contour(x, y, T, "DiPietrantonio_ME5130_Midterm_P2.png")


if __name__ == "__main__":
    main()