## Fundamental Partial Differential Equations

### Laplace's Equation

Laplace's equation is a second-order PDE that appears in many areas of physics, such as electromagnetism, astronomy, and fluid dynamics:

$$
\frac{\partial^2 T}{\partial x^2} + \frac{\partial^2 T}{\partial y^2} = 0.
$$

This equation is used for problems involving the absence of external forces, like static potential fields or incompressible fluid flows.

### Poisson's Equation

Poisson's equation is similar to Laplace's equation but includes a source term $$  T_0(x, y)  $$ , representing an external influence such as charge or heat sources:

$$
\frac{\partial^2 T}{\partial x^2} + \frac{\partial^2 T}{\partial y^2} = T_0(x, y).
$$

This equation is essential in electrostatics and gravitational fields where the sources are distributed within the domain.

### Wave Equation

The wave equation models the propagation of waves, such as sound or water waves, in a medium:

$$
\frac{\partial^2 u}{\partial t^2} = a^2 \frac{\partial^2 u}{\partial x^2}.
$$

The variable $$  u  $$  often represents the wave's amplitude, and $$  a  $$  is the wave speed.

### Euler-Tricomi Equation

The Euler-Tricomi equation is used in transonic flow studies, where the flow speed is close to the speed of sound:

$$
\frac{\partial^2 u}{\partial y^2} + \frac{\partial^2 u}{\partial x^2} = 0.
$$

This equation governs the behavior of potential flow in aerodynamics, particularly in the transonic regime where flow can be both subsonic and supersonic.

Each of these PDEs is instrumental in modeling and understanding the behavior of physical systems under various conditions. They are the starting point for many complex simulations in aerodynamics and other engineering applications.
