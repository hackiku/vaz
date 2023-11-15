## Numerical Solution Method

The numerical solution of the PDE \( u_t + a u_x = 0 \) can be approached using finite difference methods, which discretize the problem on a grid in space and time.

### Forward Time Backward Space (FTBS) Scheme

To approximate the derivatives, we apply the following finite difference scheme known as the FTBS (Forward Time Backward Space):

$$
\frac{u_i^{n+1} - u_i^n}{\Delta t} + a \frac{u_i^n - u_{i-1}^n}{\Delta x} = 0.
$$

Here, \( u_i^n \) represents the numerical approximation of \( u \) at spatial position \( i \) and time step \( n \), with \( \Delta t \) and \( \Delta x \) being the time and space increments, respectively.

### Discretization and Solution Update

Rearranging the above equation gives us the update formula for \( u_i^{n+1} \):

$$
u_i^{n+1} = u_i^n - c \left( u_i^n - u_{i-1}^n \right),
$$

where \( c = \frac{a \Delta t}{\Delta x} \) is the Courant number, which should satisfy certain conditions for stability.

### Initial Condition Implementation

For numerical solutions, it's essential to have an initial condition. In this case, \( u(x, 0) = e^{-x^2} \), which is used to initialize the values of \( u \) at the first time step (\( n = 0 \)).

The script `pr1_num.m` presumably contains MATLAB code to implement this numerical method and solve the PDE given the initial condition.