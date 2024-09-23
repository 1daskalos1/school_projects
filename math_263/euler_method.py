import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Function to implement Euler's method
def euler_method(f, y0, x0, x_end, h):
    x = np.arange(x0, x_end + h, h)  # Create an array of x values (Initial, End, Step)
    y = np.zeros(len(x))  # Initialize y array
    y[0] = y0  # Set initial condition
    for i in range(1, len(x)): # Start at x[1] since the 0th index is the initial condition
        y[i] = y[i-1] + h * f(x[i-1], y[i-1])  # Apply Euler's method
    return x, y

# Example of a lambda function for the ODE dy/dx = 3x + y
# This lambda function represents the ODE: dy/dx = 3x + y
# It takes two arguments, x and y, and returns 3*x + y
# Example: lambda x, y: 3*x + y
ode_str = input("Enter the ODE in the form 'lambda x, y: expression': ")
ode = eval(ode_str)

# Ask user for input
y0 = float(input("Enter the initial value y0: "))
x0 = float(input("Enter the initial x value x0: "))
x_end = float(input("Enter the final x value x_end: "))

# Define step sizes
h1 = float(input("Enter the first step size h1: "))
h2 = float(input("Enter the second step size h2: "))
h3 = float(input("Enter the third step size h3: "))

# Solve the ODE using Euler's method with different step sizes
x1, y1 = euler_method(ode, y0, x0, x_end, h1)
x2, y2 = euler_method(ode, y0, x0, x_end, h2)
x3, y3 = euler_method(ode, y0, x0, x_end, h3)

# Solve the ODE analytically using solve_ivp
def ode_system(t, y):
    return ode(t, y)

sol = solve_ivp(ode_system, [x0, x_end], [y0], t_eval=np.linspace(x0, x_end, 1000))

# Plot the results
plt.plot(x1, y1, label=f'Euler h = {h1}')
plt.plot(x2, y2, label=f'Euler h = {h2}')
plt.plot(x3, y3, label=f'Euler h = {h3}')
plt.plot(sol.t, sol.y[0], label='Analytical Solution', linestyle='dashed')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Euler\'s Method vs Analytical Solution')
plt.legend()
plt.grid(True)
plt.show()
