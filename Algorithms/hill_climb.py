import numpy as np

# Define the function
def f(x):
    return -(x-3)**2 +9  # Parabola with max at x = 3

# Hill Climbing Algorithm
def hill_climb(start_x, step_size = 0.1, max_iterations = 1000):
    x = start_x  # Fixed starting point
    for _ in range(max_iterations):
        next_x = x + step_size
        prev_x = x - step_size

        if f(next_x) > f(x):
            x = next_x
        elif f(prev_x) > f(x):
            x = prev_x
        else:
            break

    return x, f(x)

# Fixed starting point (not random anymore)
start_x = -5.0

# Run the hill climbing algorithm
x_max, f_max = hill_climb(start_x)

# Print results
print(f"Starting at x = {start_x:.2f}")
print(f"Maximum found at x = {x_max:.2f}, f(x) = {f_max:.2f}")
