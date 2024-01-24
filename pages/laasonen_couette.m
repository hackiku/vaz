% Clear workspace and command window
clear all;
clc;

% Couette flow simulation using Laasonen method

% Parameters
h = 1.0;  
u_g = 1.0;  
Ny = 100;  
dy = h / (Ny - 1);  
dt = 0.0001;  
total_time = 2.0;  
num_steps = round(total_time / dt);  
Dy = 0.001;  

% Initialize velocity profile
u = zeros(Ny, 1);
u(end) = u_g;  % Boundary condition for upper plate

% Coefficient matrix and right-hand side vector
A = zeros(Ny, Ny);
for i = 2:Ny-1
    A(i, i-1) = -Dy * dt / dy^2;
    A(i, i) = 1 + 2 * Dy * dt / dy^2;
    A(i, i+1) = -Dy * dt / dy^2;
end
A(1, 1) = 1;
A(end, end) = 1;

% Laasonen scheme
for n = 1:num_steps
    b = u;  % Right-hand side vector
    b(1) = 0;  % Boundary condition for lower plate
    b(end) = u_g;  % Boundary condition for upper plate
    u = A\b;  % Solve linear system
end

% Plotting
y = linspace(0, h, Ny);
plot(y, u);
xlabel('Position between the plates (m)');
ylabel('Fluid velocity (m/s)');
title('Laasonen method: Velocity profile of fluid between two parallel plates');
grid on;