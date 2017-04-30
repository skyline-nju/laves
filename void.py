import numpy as np
import lattice


def read(file):
    with open(file) as f:
        lines = f.readlines()
        pos = []
        for line in lines[2:]:
            line = line.replace("\n", "").split(" ")
            line = [i for i in line if i != ""]
            x = float(line[1])
            y = float(line[2])
            z = float(line[3])
            pos.append([x, y, z])
    return np.array(pos)


def fill_void(pos, r1, r2, N):
    dis2 = (r1 + r2) ** 2
    pos_max = pos.max(axis=0)
    pos_min = pos.min(axis=0)
    L = pos_max - pos_min
    pos_s = []

    for i in range(N):
        x = pos_min + L * np.random.rand(3)
        is_overlapping = False
        for x0 in pos:
            if np.sum((x-x0)**2) < dis2:
                is_overlapping = True
                break
        if not is_overlapping:
            pos_s.append(x)
    return pos_s


if __name__ == "__main__":
    # pos = lattice.FCC.expand(3, 3, 3)
    # pos = pos * np.sqrt(2)
    # lattice.FCC.to_xyz(pos, "test.xyz")
    # pos_s = fill_void(pos, 0.5, 0.05, 1000000)
    # lattice.FCC.to_xyz(pos_s, "test2.xyz", "Small")
    pos = read("data\\HCP.xyz")
    pos_s = fill_void(pos, 1.6, 0.1, 100000)
    lattice.FCC.to_xyz(pos_s, "test3.xyz", "small")
