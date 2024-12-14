import os
import re
from collections import Counter

def read_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read()
    return content

def count_unique_tokens(content):
    tokens = re.findall(r"\b\w+\b", content)
    unique_tokens = set(tokens)
    return len(unique_tokens)

def calculate_statistics(file_content, eta):
    length = len(file_content)
    unique_tokens_count = count_unique_tokens(file_content)
    
    if unique_tokens_count > eta:
        raise ValueError("Количество уникальных токенов больше чем размер словаря")
    
    return {
        'length': length,
        'unique_tokens_count': unique_tokens_count
    }

def theoretical_values(eta):
    # Теоретические значения
    mean_length = eta * (eta - 1) / (eta - 2)
    variance = eta * (eta - 1) / ((eta - 2)**2 * (eta - 3))
    std_deviation = variance**0.5
    relative_error = std_deviation / mean_length
    
    return {
        'mean_length': mean_length,
        'variance': variance,
        'std_deviation': std_deviation,
        'relative_error': relative_error
    }

def analyze_real_program(file_content):
    # Подсчет количества уникальных символов
    unique_chars = set(file_content)
    dictionary_size = len(unique_chars)
    
    # Измерение длины программы
    program_length = len(file_content)
    
    return {
        'dictionary_size': dictionary_size,
        'program_length': program_length
    }

def main():
    filename = 'your_python_script.py'
    file_content = read_file(filename)
    
    etas = [16, 32, 64, 128]
    
    for eta in etas:
        print(f'Eta: {eta}')
        
        try:
            statistics = calculate_statistics(file_content, eta)
            print('Статистические оценки:')
            print(f'\tДлина программы: {statistics["length"]}')
            print(f'\tКоличество уникальных токенов: {statistics["unique_tokens_count"]}\n')
            
            # Вычисление теоретических значений
            theory = theoretical_values(eta)
            print('Теоретические значения:')
            print(f'\tСредняя длина программы: {theory["mean_length"]:.2f}')
            print(f'\tДисперсия: {theory["variance"]:.2f}')
            print(f'\tСреднеквадратическое отклонение: {theory["std_deviation"]:.2f}')
            print(f'\tОтносительная ошибка: {theory["relative_error"]:.2f}\n')
            
            # Анализ реальной программы
            real_analysis = analyze_real_program(file_content)
            print('Анализ реальной программы:')
            print(f'\tРазмер словаря: {real_analysis["dictionary_size"]}')
            print(f'\tДлина программы: {real_analysis["program_length"]}\n')
            
            # Прогнозирование длины программы
            input_output_params = 10  # предположим, что у нас 10 входных/выходных параметров
            predicted_length = eta * input_output_params
            print(f'Прогнозируемая длина программы: {predicted_length}')
            print(f'Фактическая длина программы: {real_analysis["program_length"]}\n\n')
        except ValueError as e:
            print(e)
            continue

if __name__ == '__main__':
    main()