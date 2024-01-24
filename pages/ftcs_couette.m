% Clear workspace and command window
clear all;
clc;

% Couette flow simulation using FTCS method

% Parameters
h = 1.0;  % Distance between the plates in meters
u_g = 1.0;  % Speed of the upper plate in m/s
Ny = 100;  % Number of grid points in y direction
dy = h / (Ny - 1);  % Grid spacing in y direction
dt = 0.0001;  % Time step in seconds
total_time = 2.0;  % Total time for the simulation in seconds
num_steps = round(total_time / dt);  % Number of time steps
Dy = 0.001;  % Diffusion coefficient

% Initialize velocity profile
u = zeros(Ny, 1);
u(end) = u_g;  % Upper plate moving at u_g

% FTCS scheme
for n = 1:num_steps
    u_new = u;
    for i = 2:Ny-1
        u_new(i) = u(i) + (Dy * dt / dy^2) * (u(i+1) - 2*u(i) + u(i-1)) ...
                + (0.02 * dt / (2 * dy)) * (u(i+1) - u(i-1));
    end
    u = u_new;
end

% Plotting
y = linspace(0, h, Ny);
plot(y, u);
xlabel('Position between the plates (m)');
ylabel('Fluid velocity (m/s)');
title('FTCS method: Velocity profile of fluid between two parallel plates');
grid on;