# couette flow between two parallel plates

import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
import inspect
import pandas as pd

def ftcs_couette():
    h = 1.0  # Distance between the plates in meters
    u_g = 1.0  # Speed of the upper plate in m/s

    # Discretization parameters
    Ny = 100  # Number of grid points in y direction
    dy = h / (Ny - 1)  # Grid spacing in y direction
    dt = 0.0001  # Time step in seconds, chosen for stability
    total_time = 2.0  # Total time for the simulation in seconds
    num_steps = int(total_time / dt)  # Number of time steps

    # Diffusion coefficient for the y direction
    Dy = 0.001  

    # Prepare the array for u(y,t) with initial condition u(y,0) = 0
    u = np.zeros(Ny)

    # Boundary conditions
    u[0] = 0      # u(0,t) = 0 for the lower stationary plate
    u[-1] = u_g   # u(h,t) = u_g for the upper moving plate

    # FTCS scheme to update u for each time step
    for n in range(num_steps):
        u_new = u.copy()  # Copy the current velocity profile
        for i in range(1, Ny-1):  # Update all points except the boundaries
            # Include the term for the first derivative with respect to y
            u_new[i] = u[i] + (Dy * dt / dy**2) * (u[i+1] - 2*u[i] + u[i-1]) \
                    + (0.02 * dt / (2 * dy)) * (u[i+1] - u[i-1])
        u = u_new  # Set the new profile as the current profile

    # Visualize the final velocity profile
    fig, ax = plt.subplots()
    ax.plot(np.linspace(0, h, Ny), u, label=f'Time = {num_steps*dt} seconds')
    ax.set_xlabel('Position between the plates (m)')
    ax.set_ylabel('Fluid velocity (m/s)')
    ax.set_title('Velocity profile of fluid between two parallel plates')
    ax.legend()
    ax.grid(True)
    st.pyplot(fig)

    # Return the final velocity profile
    return u


def laasonen_couette():
    # Parameters are the same as in the ftcs_couette function
    h = 1.0
    u_g = 1.0
    Ny = 100
    dy = h / (Ny - 1)
    dt = 0.0001
    total_time = 2.0
    num_steps = int(total_time / dt)
    Dy = 0.001

    # Initialize the velocity profile
    u = np.zeros(Ny)
    u[0] = 0
    u[-1] = u_g

    # Coefficient matrix and right-hand side vector
    A = np.zeros((Ny, Ny))
    b = np.zeros(Ny)

    # Populate the matrix A
    for i in range(1, Ny - 1):
        A[i, i-1] = -Dy * dt / dy**2
        A[i, i] = 1 + 2 * Dy * dt / dy**2
        A[i, i+1] = -Dy * dt / dy**2

    # Boundary conditions
    A[0, 0] = A[-1, -1] = 1

    # Time-stepping loop
    for n in range(num_steps):
        # Update the right-hand side vector
        b = u.copy()
        b[0] = 0
        b[-1] = u_g

        # Solve the linear system
        u = np.linalg.solve(A, b)

    # Plotting the final velocity profile
    fig, ax = plt.subplots()
    ax.plot(np.linspace(0, h, Ny), u, label=f'Time = {num_steps*dt} seconds')
    ax.set_xlabel('Position between the plates (m)')
    ax.set_ylabel('Fluid velocity (m/s)')
    ax.set_title('Laasonen method: Velocity profile of fluid between two parallel plates')
    ax.legend()
    ax.grid(True)
    st.pyplot(fig)

    return u


def main():
    st.title("Couette Flow Simulation between Two Parallel Plates")
    
    # Display the problem statement and the formula
    st.write("""
    This Streamlit app simulates the Couette flow of fluid between two infinite parallel plates.
    One plate is stationary, and the other moves at a constant velocity, inducing flow in the fluid.
    """)
    
    st.latex(r"""
    \frac{\partial u}{\partial t} - 0.001 \frac{\partial^2 u}{\partial y^2} - 0.02 \frac{\partial u}{\partial y} = 0
    """)
    
    # =========================== FTCS ====================================
    st.subheader("1. FTCS scheme for Couette flow")
    # Call the simulation function and display the results
    velocity_profile_ftcs = pd.DataFrame(ftcs_couette())
    st.write("Final velocity profile:")
    st.dataframe(velocity_profile_ftcs.transpose())  
      
    # Display the source code in a streamlit code box
    ftcs_couette_code = inspect.getsource(ftcs_couette)
    with st.expander("Click to reveal Python code"):
        st.code(ftcs_couette_code, language='python')
    with open('./pages/ftcs_couette.m', 'r') as file:
        output = file.read()
        st.code(output, language='matlab')

    st.markdown("***")

    # =========================== Laasonen ====================================
    st.subheader("1. Laasonen method for Couette flow")
    # Display the problem statement and the formula
    
    velocity_profile_laasonen = pd.DataFrame(laasonen_couette())
    st.write("Laasonen velocity profile:")
    st.dataframe(velocity_profile_laasonen.transpose())

    # Display the source code in a streamlit code box
    laasonen_couette_code = inspect.getsource(laasonen_couette)
    with st.expander("Click to reveal Python code"):
        st.code(laasonen_couette_code, language='python')
    
    with open('./pages/ftcs_couette.m', 'r') as file:
        output = file.read()
        st.code(output, language='matlab')

if __name__ == "__main__":
    main()