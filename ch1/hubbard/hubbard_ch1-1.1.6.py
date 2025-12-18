import matplotlib.pyplot as plt

f_dict = {
    "a": lambda x, y : (0, 1),
    "b": lambda x, y : (x, 0),
    "c": lambda x, y : (x, y),
    "d": lambda x, y : (x, -y),
    "e": lambda x, y : (y, x),
    "f": lambda x, y : (-y, x),
    "g": lambda x, y : (y, x - y),
    "h": lambda x, y : (x - y, x + y),
    "i": lambda x, y : ((x**2) - y - 1, x - y),
}
import math
import numpy as np
def main():
    func = "i"
    scale = 0.3

    for x in range(-4, 5, 1):
        for y in range(-4, 5, 1):
            _dx, _dy = f_dict[func](x, y)
            dx, dy = _dx * scale, _dy * scale
            plt.arrow(x, y, dx, dy, head_width=4*0.01)
    plt.show()

if __name__ == "__main__":
    main()
