import numpy as np
np.set_printoptions(precision=2)

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.animation as manimation

from scipy.integrate import solve_ivp
from scipy.interpolate import pchip

import random
from tqdm.auto import tqdm

# Parameters

N = 1000                           # Number of particles
state0 = np.array([1.0, 1.0, 1.0]) # starting point
mu, std = 0, 0.1                   # mean and standard deviation of the 
                                   # point cloud around state0
 
T = 1000                           # Integration time limit
t = np.arange(0.0, 100.0, 0.001)

# Parameters of the Lorenz system
rho = 25.0
sigma = 10.0
beta = 8.0 / 3.0

# The Lorentz system
def f(t, state):
    x, y, z = state 
    x_dot = np.array([sigma * (y - x),
                      x * (rho - z) - y,
                      x * y - beta * z])  # Derivatives
    
    return x_dot

# Generate the attractor curve (solution for state0 initial condition)
Solver = solve_ivp(f, [0,T], y0=[1,1,1], rtol=1e-8,
                   method='RK45') # RK45 adaptive integrator
print('*'*64)
print('Attractor generated.')
print('*'*64)

fig = plt.figure(figsize = (10,10))
ax = fig.add_subplot(111, projection='3d')
ax.patch.set_facecolor('black')

plt.style.use("dark_background")
plt.rcParams['text.usetex'] = True

ax.plot(Solver.y[0,:], Solver.y[1,:], Solver.y[2,:],
                    color = 'gold', linewidth= 0.05)
plt.axis('off')
ax.view_init(10, 100)

plt.savefig('Lorenz_Attractor.jpg', dpi=200)

print('*'*64)
print('Lorenz attractor curve saved to disc')
print('*'*64)

# Generate the trajectory for the point cloud

states = np.array([1,1,1]) + \
         np.random.normal(mu, std, size=(N,3)) # Intial states

T = 50  # Reduced upper limit of time integration for faster execution

# Lists to save the trajectories and the corresponding times
ys = [] 
ts = [] # Remeber RK45 adaptively chooses different time steps
        # necessary to constrain the error, we have to keep t
        # to interpolate later

print('*'*64)
print('Solving for the trajectories of the particles in the point cloud')
print('*'*64)

# Find the trajectories of the N particles
for y0 in tqdm(states):
    
    Solver_2 = solve_ivp(f, [0,T], y0=y0, rtol=1e-8,
                         method='RK45')
    
    ys.append(Solver_2.y)
    ts.append(Solver_2.t)

print('*'*64)
print('Completed')
print('*'*64)

t = np.linspace(0, T, 6000) # Updated time discretization for 
                            # interpolation

y_interp = {}               # Dictionary storing interploated trajectories

for i, t, y in tqdm(zip(list(range(N)),ts, ys)):

    y_interp[i] = pchip(t, y.T)(t) # Interpolation

print('*'*64)
print('Interpolated trajectories.')
print('*'*64)

# Plot results

FFMpegWriter = manimation.writers['ffmpeg'] 
metadata = dict(title='Chaos in Lorenz Attractor', artist='Mathew Alex',
                codec="h264", bitrate=1000000,
                comment= str(N) + 'closely spaced points evolving in Lorenz Attractor')

writer = FFMpegWriter(fps=20, metadata=metadata) # Movie object

print('*'*64)
print('Initiating animated plot')
print('*'*64)

# Update the frames for the movie
with writer.saving(fig, "Lorenz_Attractor_Chaos_Movie (with attractor curve).mp4", 300):
    
    for i in tqdm(range(len(t))):
        
        if i%10 == 0:
            
            ax.cla()
            ax.patch.set_facecolor('black')
            plt.axis('off')
            plt.style.use("dark_background")

            ax.plot(Solver.y[0,:], Solver.y[1,:], Solver.y[2,:],
                    color = 'gold', linewidth= 0.05)
            
            ax.text2D(0.80, 0.95, r"Lorenz Attractor $\vert$ Time = %s s"%(np.round(t[i],2)),
              transform=ax.transAxes)
            ax.text2D(0.80, 0.92, r"$\rho = %s, \sigma = %s, \beta = %s $"\
                                  %(str(rho),str(sigma),str(np.round(beta,2))),
                                  transform=ax.transAxes)
            ax.text2D(0.80, 0.89, r"$N = %s, \mu = %s, std = %s$"\
                      %(str(N), str(mu), str(std)), transform=ax.transAxes)
            
            ax.scatter3D([y[i][0] for y in y_interp.values()],
                         [y[i][1] for y in y_interp.values()],
                         [y[i][2] for y in y_interp.values()],
                         s=1, c='r')
            
            ax.view_init(10, 100)
            
            ax.axes.set_xlim3d(min(Solver.y[0,:])+1, max(Solver.y[0,:])+1)
            ax.axes.set_ylim3d(min(Solver.y[1,:])+1, max(Solver.y[1,:])+1)
            ax.axes.set_zlim3d(min(Solver.y[2,:])+1, max(Solver.y[2,:])+1)
                        
            writer.grab_frame()

print('*'*64)
print('Program complete')
print('*'*64)
