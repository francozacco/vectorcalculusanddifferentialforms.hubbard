import matplotlib.pyplot as plt
import math
import numpy as np

def main():
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    r = 0.4
    scale = 0.5
    r_step = 0.05

    def func(x, y, z, theta):
        xa = x - math.cos(theta)
        ya = y - math.sin(theta)
        za = z 

        dx = (r**2 - (xa**2 + ya**2 + za**2)) * (- math.sin(theta))
        dy = (r**2 - (xa**2 + ya**2 + za**2)) * math.cos(theta)
        return dx, dy

    theta_points = np.arange(0, 2 * np.pi, 0.2)
    phi_points = np.arange(0, 2 * np.pi, 0.2)
    r_points = np.arange(0 , r + r_step, r_step)
    r_points = [0, 0.1, 0.2, 0.34]
    for _r in r_points:
        for theta in theta_points:
            for phi in phi_points:
                x = (1 + _r * math.cos(phi)) * math.cos(theta)
                y = (1 + _r * math.cos(phi))* math.sin(theta)
                z = _r * math.sin(phi)
                _dx, _dy = func(x, y, z, theta)
                dx, dy = _dx * scale, _dy * scale
                ax.quiver(x, y, z, dx, dy, 0, color='black', length=1, normalize=False)
    
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_zlabel("z")

    # Donut for reference
    theta = np.linspace(0, 2*np.pi, 100)
    phi = np.linspace(0, 2*np.pi, 50)
    theta, phi = np.meshgrid(theta, phi)
    x = (1 + r * np.cos(phi)) * np.cos(theta)
    y = (1 + r * np.cos(phi)) * np.sin(theta)
    z = r * np.sin(phi)
    ax.plot_surface(x, y, z, color='black', alpha=0.2)

    plt.show()



if __name__ == "__main__":
    main()
