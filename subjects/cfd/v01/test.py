# test.py

content = r'''
## Computational Fluid Dynamics: Analytical Solutions

**Topic: Solving PDEs for Fluid Flow**

**Complete Solution:**
The comprehensive solution \( u(x, t) \) is piecewise-defined:
  \( u(x, t) = 1 \) for \( x - 3 < t \)
  \( u(x, t) = \sqrt{\frac{x - 3}{t}} \) for \( t \leq x - 3 < 4t \)
  \( u(x, t) = 2 \) for \( x - 3 \geq 4t \)

**Concepts:**
- To find the solution \( u(x, t) \) for the domain \( t \leq x - 3 < 4t \), we introduce an admissible function \( g \) with the property \( g = a^{-1} \).
- This involves the transformation \( a(u) = u^2 \), leading to \( u(a) = \sqrt{a} \), and subsequently \( g\left(\frac{x - x_0}{t}\right) = \sqrt{\frac{x - x_0}{t}} \).
'''