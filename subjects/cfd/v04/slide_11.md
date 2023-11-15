## Example 1: Analytical Solution Using Characteristics

### Characteristic Equations

From the given PDE, we derive the characteristic equations:

$$
\frac{\partial x}{\partial r} = 2, \quad \frac{\partial t}{\partial r} = 1, \quad \frac{\partial u}{\partial r} = 0.
$$

### Finding the Transformations

Integrating the first two equations, we find the transformations between the original coordinates $$ (x, t) $$  and the characteristic coordinates $$ (r, s) $$ :

$$
dx = 2dr, \quad dt = dr \Rightarrow x = 2r + s, \quad t = r.
$$

By inverting these transformations, we express $$ r $$  and $$ s $$  in terms of $$ x $$  and $$ t $$ :

$$
r = t, \quad s = x - 2t.
$$

### Solution to the PDE

Since $$ \frac{\partial u}{\partial r} = 0 $$ , $$ u $$  is constant along the characteristics. Therefore, $$ u $$  can be expressed as a function of $$ s $$  alone:

$$
u(x, t) = u(s) = u(x - 2t).
$$

With the initial condition $$ u(x, 0) = e^{-x^2} $$ , the solution to the PDE is:

$$
u(x, t) = e^{-(x - 2t)^2}.
$$

This solution implies that the initial profile for $$ u $$  propagates along the characteristics without changing shape, a typical behavior of solutions to linear hyperbolic PDEs.

The analytical solution obtained via the method of characteristics is powerful because it provides explicit formulas for the solution, which are particularly useful for understanding the underlying physics and for validation of numerical methods.
