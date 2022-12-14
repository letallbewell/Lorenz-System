# Lorenz-System

Illustration of the onset of chaos in the Lorenz system of differential equations.

# Theory

## The Lorenz System of Differential Equations

The Lorenz system arose in a simplified description of atmospheric convection and is probably the best-known example of a chaotic system. The following system of differential equations defines it:

$$ \frac{dx}{dt} = \sigma \left( y - x \right), $$

$$ \frac{dy}{dt} = x \left( \rho - z \right)  - y, $$

$$ \frac{dz}{dt} = xy - \beta z.$$

$\alpha, \beta \text{ and } \sigma$ are parameters of the system.

## Chaos

The defining property of chaotic systems is **approximate initial conditions cannot predict approximate futures whereas exact initial conditions can predict exact future**.

The popular notion of the butterfly effect (the flap of a butterfly's wing affecting a tornado weeks later) is a metaphorical version of this phenomenon of sensitive dependence on initial conditions. The shape of the solutions also resembles a butterfly to the romanticization's merit.

<p>
  <img align="center" src="Lorenz_Attractor_Compressed.png" alt="" width="500px">
</p>




The above is the solution for the system for the initial condition $[1, 1, 1]$.

# Simulation

**Note:** [ffmpeg](https://github.com/kkroening/ffmpeg-python) might be required to generate the movie apart from the [requirements.txt](requirements.txt)

The program uses the **RK45** algorithm to integrate the system of equations; the adaptive time steps of the algorithm comes in handy in dealing with chaotic systems: the integrator adjusts the time step to keep the error in each step under the specified threshold. We later interpolate the solutions to cast the trajectories onto a linearly spaced time grid.

A particle cloud of $N = 1000$, points starting about $[1, 1, 1]$ is integrated this way. You can see how quickly these particles (red dots) diverge from the solution for the starting point $[1, 1, 1]$ (golden curve).



https://user-images.githubusercontent.com/43025445/182188478-5b147908-779f-4cc1-a89a-fd367d58d799.mp4



