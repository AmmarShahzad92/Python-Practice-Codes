# Define the function
def f(x):
    return -(x**4)/8 + (x**3)/2 + 2*x**2 - 4*x + 5

# Hill Climbing with dynamic step size
def dynamic_hill_climbing(start_x, initial_step, min_step):
    x = start_x
    step = initial_step
    current_value = f(x)

    while step > min_step:
        # Try positive and negative steps
        x_plus = x + step
        x_minus = x - step
        value_plus = f(x_plus)
        value_minus = f(x_minus)

        # Determine the best move
        if value_plus > current_value and value_plus >= value_minus:
            x = x_plus
            current_value = value_plus
            step *= 1.1  # increase step by 10%
        elif value_minus > current_value:
            x = x_minus
            current_value = value_minus
            step *= 1.1  # increase step by 10%
        else:
            step *= 0.8  # decrease step by 20%

    return x, current_value

# Initial parameters
start_x = -2.0
initial_step = 0.1
min_step = 0.0001

# Run the algorithmto check the output
final_x, final_value = dynamic_hill_climbing(start_x, initial_step, min_step)
print("Final position x:", final_x)
print("Function value f(x):", final_value)