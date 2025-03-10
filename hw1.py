from pathlib import Path

file_path = Path("./salary_file.txt")

def total_salary(path):
    try:
        with open(path, 'r', encoding='utf-8') as file:
            total_salary = 0
            num_developers = 0

            for line in file:
                parts = line.strip().split(',')

                if len(parts) == 2:
                    name, salary = parts
                    salary = int(salary)
                    total_salary += salary
                    num_developers += 1
            if num_developers > 0:
                average_salary = round(total_salary / num_developers)

        salary_tuple = (total_salary, average_salary)
        return salary_tuple
    except FileNotFoundError:
        print(f"Помилка: Файл '{path}' відсутній.")

try:
    total, average = total_salary(file_path)

    print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
except TypeError:
    print("Помилка")








