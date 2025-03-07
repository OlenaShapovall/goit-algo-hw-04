from pathlib import Path

file_path = Path("./cats_file.txt")

def get_cats_info(path):
    cats_list = []

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                line = line.strip().split(',')

                if len(line) == 3:
                    try:
                        cat_dict = {
                        "id": line[0],
                        "name": line[1],
                        "age": line[2]
                        }

                        cats_list.append(cat_dict)

                    except ValueError:
                         print(f"Попередження: неправильний формат рядка: {line}")
            return cats_list

    except FileNotFoundError:
        print("Помилка: файл не знайдений.")
    except PermissionError:
        print("Помилка: немає прав доступу до файлу.")
    except IOError as e:
        print(f"Помилка вводу/виводу: {e}")


cats_info = get_cats_info(file_path)

print(cats_info)



