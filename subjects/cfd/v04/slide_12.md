## Example 1: Analytical Solution (Continued)

### Solution to the Ordinary Differential Equation

Analyzing and solving the ODE $$ \frac{\partial u}{\partial r} = 0 $$ , we find that $$ u $$  does not depend on $$ r $$  but only on $$ s $$ , thus:

$$
u(r, s) = C(s),
$$

where $$ C(s) $$  represents an arbitrary function of $$ s $$ .

### Determining the Particular Solution

To find the particular solution that satisfies the initial condition, we transform the initial condition and solve:

$$
u(x, 0) = e^{-x^2} \Longleftrightarrow u(r, s) = e^{-(2r+s)^2} = e^{-s^2}.
$$

From the initial condition given at $$ t = 0 $$  (hence $$ r = 0 $$ ), we have:

$$
u(0, s) = C(s) = e^{-s^2} \Rightarrow u(r, s) = e^{-s^2}.
$$

### Final Solution

Finally, returning to the original variables $$ (x, t) $$ , we obtain the solution to the PDE:

$$
u(x, t) = e^{-(x - 2t)^2}.
