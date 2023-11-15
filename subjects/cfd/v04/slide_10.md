## Example 1: Solving a First-Order PDE

### Problem Statement

We are asked to solve the following PDE:

$$
2 u_x + u_t = 0,
$$

where $$ u_x $$  is the partial derivative of $$ u $$  with respect to $$ x $$ , and $$ u_t $$  is the partial derivative of $$ u $$  with respect to $$ t $$ . This equation is defined for all $$ x $$  in $$ (-\infty, \infty) $$  and for $$ t > 0 $$ .

### Initial Condition

The solution is subject to the initial condition:

$$
u(x, 0) = e^{-x^2},
$$

for all $$ x $$  in $$ (-\infty, \infty) $$ .

### Solution Approach

To solve this PDE, we would typically use the method of characteristics. The characteristics are lines in the $$ x-t $$  plane along which the value of $$ u $$  is constant. We would find these lines by solving the system of ODEs that comes from the method of characteristics.

For this specific PDE, the characteristic equations would be:

$$
\frac{dx}{dt} = 2, \quad \frac{du}{dt} = 0.
$$

Solving these equations gives us the characteristics along which the solution can be expressed in terms of the initial condition. The solution $$ u(x, t) $$  will then be a function that travels along the characteristic lines without changing its shape, a property typical of wave equations.

This problem is a classic example of how to apply analytical methods to solve PDEs, which is an essential skill in fields such as aerodynamics, acoustics, and heat transfer.
