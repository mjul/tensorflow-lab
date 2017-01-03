import numpy
from matplotlib.pylab import plot, show, grid, axis, xlabel, ylabel, title

from brownian import brownian, geometric_brownian

# The Wiener process parameter.
delta = 2
# Total time.
T = 10.0
# Number of steps.
N = 500
# Time step size
dt = T/N
# Number of realizations to generate.
m = 5

# The percentage drift per time step (year)
mu = 0.055
# The percentage volatility of the stocks (per year)
sigma = 0.10

# Create an empty array to store the realizations.
x = numpy.empty((m,N+1))


# Initial values of x.
S0=50
x[:, 0] = S0

brownian(x[:,0], N, dt, delta, out=x[:,1:])

t = numpy.linspace(0.0, N*dt, N+1)
#for k in range(m):
#    plot(t, x[k])
xlabel('t', fontsize=16)
ylabel('x', fontsize=16)
grid(True)


gbms = geometric_brownian(S0=S0, mu=mu, sigma=sigma, dt=dt, num_paths=m, num_steps=N+1)
for k in range(m):
    plot(t, gbms[k])

avg = numpy.average(gbms, axis=0)
plot(t, avg, linewidth=5)


show()