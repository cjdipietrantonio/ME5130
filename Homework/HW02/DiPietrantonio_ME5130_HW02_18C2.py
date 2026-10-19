r'''
Christian DiPietrantonio
ME5130: Advanced Heat and Mass Transfer
HW02: Problem 18C.2, Part (a):
  Integrate Eq. 18.7-6 separately for the active and inactive regions. Then apply the appropriate boundary conditions to evaluate the integration constants, and solve for the concentration profile in each region. Give qualitative sketches to illustrate the forms of the profiles.

'''

import numpy as np
import matplotlib.pyplot as plt

def main():
  kappa = 0.5 
  x = np.linspace(0, 1, 1001)

  for phi in [1, 5, 10]:
    u = phi * (1 - kappa)
    D = kappa * phi * np.cosh(u) + np.sinh(u)

    c = np.full_like(x, phi / D)

    s = x >= kappa

    c[s] = (kappa * phi * np.cosh(phi * (x[s] - kappa)) + np.sinh(phi * (x[s] - kappa))) / (x[s] * D)

    plt.plot(x, c, label=rf'$\phi$ = {phi}')

  plt.axvline(kappa, color='gray', ls=':')
  plt.xlabel(r'$x = r/R$')
  plt.ylabel(r'$c_A/c_{AR}$')
  plt.title(rf'$\kappa$ = {kappa}')
  plt.legend()
  plt.tight_layout()
  plt.savefig('DiPietrantonio_ME5130_HW02_18C2.png', dpi=300)

if __name__ == '__main__':
  main()


