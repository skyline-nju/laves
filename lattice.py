""" To generate the coordinates of colloidal crystal.
"""
import os
import numpy as np


class UnitCell:
    def __init__(self,
                 inside_atoms=None,
                 a=[1, 0, 0],
                 b=[0, 1, 0],
                 c=[0, 0, 1],
                 alpha=90,
                 beta=90,
                 gamma=90):
        self.a = np.array(a)
        self.b = np.array(b)
        self.c = np.array(c)
        self.alpha = alpha / 180 * np.pi
        self.beta = beta / 180 * np.pi
        self.gamma = gamma / 180 * np.pi
        if inside_atoms is None:
            self.atom = np.array([0, 0, 0])
        elif isinstance(inside_atoms[0], list):
            inside_atoms.append([0, 0, 0])
            self.atom = np.array(inside_atoms)
        else:
            # ndim of inside_atoms is 1
            self.atom = np.array([inside_atoms, [0, 0, 0]])

    def expand(self, n1=1, n2=1, n3=1):
        def for_each_atom(x0, y0, z0):
            for k1 in range(n1 + 1):
                x_new = x0 + k1
                if x_new > n1:
                    continue
                for k2 in range(n2 + 1):
                    y_new = y0 + k2
                    if y_new > n2:
                        continue
                    for k3 in range(n3 + 1):
                        z_new = z0 + k3
                        if z_new > n3:
                            continue
                        r.append([x_new, y_new, z_new])

        r = []
        if self.atom.ndim == 1:
            for_each_atom(self.atom[0], self.atom[1], self.atom[2])
        else:
            for x0, y0, z0 in self.atom:
                for_each_atom(x0, y0, z0)
        return np.array(r)

    def to_xyz(self, r, file="test.xyz", pType="A"):
        with open(file, "w") as f:
            f.write("%d\n" % len(r))
            f.write("just for test\n")
            for x, y, z in r:
                f.write("%s\t%g\t%g\t%g\n" % (pType, x, y, z))


SC = UnitCell()
BCC = UnitCell([0.5, 0.5, 0.5])
FCC = UnitCell([[0.5, 0.5, 0], [0.5, 0, 0.5], [0, 0.5, 0.5]])

if __name__ == "__main__":
    os.chdir("data")
