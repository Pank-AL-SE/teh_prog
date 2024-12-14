import numpy as np
from scipy.stats import chi2, poisson

# Функция для расчета критерия хи-квадрат
def chi_square_test(observed, expected, ddof=0):
    # observed - наблюдаемые частоты
    # expected - ожидаемые частоты
    # ddof - степень свободы (по умолчанию 0)
    
    chi_sq_stat = np.sum((observed - expected)**2 / expected)
    df = len(observed) - 1 - ddof
    p_value = 1 - chi2.cdf(chi_sq_stat, df)
    
    return chi_sq_stat, p_value

# Наблюдаемые данные
observed = np.array([20, 25, 30, 15, 10])

# Ожидаемое распределение Пуассона
lambda_ = np.mean(observed)
expected = poisson.pmf(np.arange(len(observed)), lambda_)
expected *= np.sum(observed)

# Тестирование
chi_sq_stat, p_value = chi_square_test(observed, expected)
print(f"Критерий хи-квадрат: {chi_sq_stat:.4f}")
print(f"П-значение: {p_value:.4f}")

# Интерпретация результатов
alpha = 0.05
if p_value <= alpha:
    print("Отвергаем нулевую гипотезу.")
else:
    print("Не отвергаем нулевую гипотезу.")