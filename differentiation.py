import numpy as np
import matplotlib.pyplot as plt


def first_derivative(f, x, h):
    if h == 0:
        return float('nan')
    else:    
        return (f(x + h) - f(x - h)) / (2 * h)

def second_derivative(f, x, h):
    if h == 0:
        return float('nan')
    else:
        return (f(x + h) - 2 * f(x) + f(x - h)) / (h**2)

def third_derivative(f, x, h):
    if h == 0:
        return float('nan')
    else:
        return (f(x + 2*h) - 2*f(x + h) + 2*f(x - h) - f(x - 2*h)) / (2 * h**3)

def fourth_derivative(f, x, h):
    if h == 0:
        return float('nan')
    else:
        return (f(x - 2*h) - 4*f(x - h) + 6*f(x) - 4*f(x + h) + f(x + 2*h)) / (h**4)

def runge_rule(deriv, f, h, p, x):
    h_half = h / 2
    d1 = deriv(f, x, h)
    d2 = deriv(f, x, h_half)
    error = abs(d1 - d2) / (2**p - 1)
    return error

def plot_error_vs_step(deriv, function, order, start, stop, step, x, deriv_name):
    errors = []
    h_values = np.arange(start, stop, step)
    for h in h_values:
        errors.append(runge_rule(deriv, function, h, order, x))
    
    valid_h_values = []
    valid_errors = []
    for h, error in zip(h_values, errors):
        if error > 0:
            valid_h_values.append(h)
            valid_errors.append(error)
    plt.figure(figsize=(10, 6))
    plt.plot(valid_h_values, valid_errors, marker='o')
    plt.xlabel('Размер шага (h)')
    plt.ylabel('Погрешность')
    plt.title(f'График зависимости ошибок от размера шага для производной {deriv_name} порядка')
    plt.xscale('log')
    plt.yscale('log')
    plt.grid(True)
    plt.show()
    