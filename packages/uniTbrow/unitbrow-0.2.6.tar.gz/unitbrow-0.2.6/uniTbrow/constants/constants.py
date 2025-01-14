from uniTbrow.units.units import metre, second, newton, kelvin, joule, mole, ampere, gram, hertz, coulomb
from sympy import pi as _pi, symbols as _symbols


class Constant:
    def __init__(self, value, symbol_str):
        self.value = value
        self.symbol = _symbols(symbol_str, positive=True, real=True)

    def __repr__(self):
        return str(self.symbol)

    def __str__(self):
        return str(self.symbol)

    def __pow__(self, power, modulo=None):
        return pow(self.symbol, power, modulo)

    def __mul__(self, other):
        return self.symbol * other

    def __rmul__(self, other):
        return self.__mul__(other)

    def __truediv__(self, other):
        return self.symbol / other

    def __rtruediv__(self, other):
        return other / self.symbol


c = Constant(299792458 * metre * second**-1, "c")
"""Speed of light in vacuum"""

G = Constant(6.6743015*10**-11 * metre**3 * (1000*gram)**-1 * second**-2, "G")
"""Newtonian gravitational constant"""

h = Constant(6.62607015*10**-34 * joule * hertz**-1, "h")
"""Planck constant"""

h_bar = Constant(h.value/(2*_pi), "ℏ")
"""Reduced Planck constant"""

mu_0 = Constant(1.2566370621219*10**-6 * newton * ampere**-2, "μ_0")
"""Vacuum magnetic permeability"""

epsilon_0 = Constant(1/(mu_0.value*c.value**2), "ε_0")
"""Vacuum electric permittivity"""

k_e = Constant(1/(4*_pi*epsilon_0.value), "k_e")
"""Coulomb constant"""

k_b = Constant(1.380649*10**-23 * joule * kelvin**-1, "k_b")
"""Boltzmann constant"""

sigma_sb = Constant(_pi**2*k_b.value**4 / (60 * h_bar.value**3 * c.value**2), "σ_{sb}")
"""Stefan-Boltzmann constant"""

e = Constant(1.602176634*10**-19 * coulomb, "e")
"""Elementary charge"""

N_A = Constant(6.02214076*10**23 * mole**-1, "N_A")
"""Avogadro constant"""

R = Constant(N_A.value * k_b.value, "R")
"""Molar gas constant"""

m_e = Constant(9.109383701528*10**-31 * 1000*gram, "m_e")
"""Electron mass"""

m_p = Constant(1.6726219236951*10**-27 * 1000*gram, "m_p")
"""Proton mass"""

m_n = Constant(1.6749274980495*10**-27 * 1000*gram, "m_n")
"""Neutron mass"""


# Looks up a constant in the library of available constants
def const_lookup(key: str):
    return {
        "c": c,
        "G": G,
        "h": h,
        "h_bar": h_bar,
        "ℏ": h_bar,
        "mu_0": mu_0,
        "μ_0": mu_0,
        "epsilon_0": epsilon_0,
        "ε_0": epsilon_0,
        "k_e": k_e,
        "k_b": k_b,
        "sigma_sb": sigma_sb,
        "σ_{sb}": sigma_sb,
        "e": e,
        "N_A": N_A,
        "R": R,
        "m_e": m_e,
        "m_p": m_p,
        "m_n": m_n,
    }[key]
