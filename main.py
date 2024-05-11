import differentiation as df
import numpy as np


# Производная вычисляется в точке x с шагом h
x = 5
h = 0.001

# Тестовые примеры
foo = 'np.sin(x)' # здесь задается произвольная функция
def f(x):
    return eval(foo)  

print(f'\nТестовый пример приводится для функции: {foo} в точке {x} c шагом {h}\n')
print('Производная 1-го порядка =', df.first_derivative(f, x, h))
print('Оценка погрешности методом Рунге:', df.runge_rule(df.first_derivative, f, h, 1, x))
print('Производная 2-го порядка =', df.second_derivative(f, x, h))
print('Оценка погрешности методом Рунге:', df.runge_rule(df.second_derivative, f, h, 2, x))
print('Производная 3-го порядка =', df.third_derivative(f, x, h))
print('Оценка погрешности методом Рунге:', df.runge_rule(df.third_derivative, f, h, 3, x))
print('Производная 4-го порядка =', df.fourth_derivative(f, x, h))
print('Оценка погрешности методом Рунге:', df.runge_rule(df.fourth_derivative, f, h, 4, x))


df.plot_error_vs_step(df.first_derivative, function=f, order=2, start=0, stop=9e-5, step=1e-6, x=x, deriv_name='1-го')
df.plot_error_vs_step(df.second_derivative, f, 2, 0, 9e-3, 1e-5, x, '2-го')
df.plot_error_vs_step(df.third_derivative, f, 4, 0, 1e-2, 1e-4, x, '3-го')
df.plot_error_vs_step(df.fourth_derivative, f, 4, 0, 1, 1e-3, x, '4-го')
