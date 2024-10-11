import matplotlib.pyplot as plt
import sympy as sp
import numpy as np
import streamlit as st

def plot_function(func_str, x_range=(-10, 10)):
    try:
        x, y = sp.symbols('x y')
        # Use sp.sympify to parse the function, expecting proper format
        eq = sp.sympify(func_str)
        
        # If the equation has a variable y
        if y in eq.free_symbols:
            solutions = sp.solve(eq, y)
        else:
            solutions = sp.solve(eq, x)

        x_vals = np.linspace(x_range[0], x_range[1], 1000)
        fig, ax = plt.subplots(figsize=(10, 6))

        for solution in solutions:
            f = sp.lambdify(x, solution, "numpy")

            try:
                y_vals = f(x_vals)
            except TypeError:
                y_vals = np.full_like(x_vals, float(solution))

            ax.plot(x_vals, y_vals, label=f'Solution: {sp.pretty(solution)}')

        ax.set_title(f"Plot of {func_str}")
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        ax.grid(True)
        ax.axhline(y=0, color='k', linestyle='-', linewidth=0.5)
        ax.axvline(x=0, color='k', linestyle='-', linewidth=0.5)
        ax.legend()
        return fig

    except sp.SympifyError as e:
        st.error(f"Unable to parse the function: {func_str}. Error: {str(e)}")
    except ValueError as e:
        st.error(f"Error in plotting the equation: {str(e)}")
    except Exception as e:
        st.error(f"An unexpected error occurred: {str(e)}")

    return None
