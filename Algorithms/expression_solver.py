import sympy as sp
import matplotlib.pyplot as plt
import numpy as np

# Define the variable
x = sp.Symbol('x')

# Define the expression: -((x-3)^2)+9
expression = -((x-3)**2) + 9

print("Original expression: -((x-3)²)+9")
print(f"SymPy format: {expression}")
print()

# Expand the expression
expanded = sp.expand(expression)
print(f"Expanded form: {expanded}")
print()

# Factor the expression (if possible)
factored = sp.factor(expression)
print(f"Factored form: {factored}")
print()

# Find the vertex form (it's already in vertex form)
print("Vertex form analysis:")
print("This is a parabola in vertex form: -(x-h)² + k")
print("Where h = 3 (x-coordinate of vertex)")
print("Where k = 9 (y-coordinate of vertex)")
print("Vertex: (3, 9)")
print("Opens downward since coefficient of (x-3)² is negative")
print()

# Find roots/x-intercepts (where y = 0)
roots = sp.solve(expression, x)
print(f"Roots (x-intercepts): {roots}")
print()

# Find y-intercept (when x = 0)
y_intercept = expression.subs(x, 0)
print(f"Y-intercept: {y_intercept}")
print()

# Find maximum value (since parabola opens downward)
print(f"Maximum value: 9 (at x = 3)")
print()

# Create a plot
x_vals = np.linspace(-2, 8, 1000)
y_vals = -((x_vals - 3)**2) + 9

plt.figure(figsize=(10, 6))
plt.plot(x_vals, y_vals, 'b-', linewidth=2, label='-((x-3)²)+9')
plt.axhline(y=0, color='k', linestyle='-', alpha=0.3)
plt.axvline(x=0, color='k', linestyle='-', alpha=0.3)
plt.plot(3, 9, 'ro', markersize=8, label='Vertex (3, 9)')
plt.plot([0, 6], [0, 0], 'go', markersize=6, label='X-intercepts')
plt.plot(0, y_intercept, 'mo', markersize=6, label=f'Y-intercept (0, {y_intercept})')
plt.grid(True, alpha=0.3)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Graph of -((x-3)²)+9')
plt.legend()
plt.xlim(-1, 7)
plt.ylim(-2, 10)
plt.show()

# Additional analysis
print("Summary:")
print("- This is a quadratic function (parabola)")
print("- Vertex: (3, 9)")
print("- Opens downward")
print("- Maximum value: 9")
print("- X-intercepts: 0 and 6")
print("- Y-intercept: 0")
print("- Domain: all real numbers")
print("- Range: y ≤ 9")
