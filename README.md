# Lorenz-System

Illustration of the onset of chaos in the Lorez system of differential equations.

# Theory

## The Lorenz System of Differential Equations

The Lorenz system is arised in a simplified description of atmospheric convection and probably the best known example of chaotic system. It is defined by the following system of differential equations:

$$ \frac{dx}{dt} = \sigma \left( y - x \right), $$

$$ \frac{dy}{dt} = x \left( \rho - z \right)  - y, $$

$$ \frac{dz}{dt} = xy - \beta z.$$

$\alpha, \beta \text{ and } \sigma$ are parameters of the system.

## Chaos

The defining property of chaotic systems is **approximate initial conditions cannot predict approximate futures whereas exact initial conditions can predict exact future**.

The popular notion of the butterfy effect (the flap of a butterfly's wing affecting a tornado weeks later) is a metaphorical version of this phenomenon of sensitive dependence on initial conditions. The shape of the solutions also resmble a butterfly to the romanticization's merit.

<div>
  <img align="left" src="Lorenz_Attractor_Compressed.png" alt="" width="500px">
</div>

The above is the solution for the system for the initial condition $[1, 1, 1]$.

# Simulation

**Note:**![ffmpeg](https://github.com/kkroening/ffmpeg-python) might be required to generate the moviw apart from the ![requirements.txt](requirements.txt)

The program uses the **RK45** algorithm to integrate the system of equations, the adaptive time steps of the algorithm comes handy in dealing with chaotic systems: the integrator adjusts the time step to keep the error in each step under the specified threshold. We later interpolate the solutions to cast the trajectories onto a linearly spaced time grid.
