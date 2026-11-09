
path = 'salary.txt'


def total_salary(path: str) -> tuple:
    total = 0
    workers_counter = 0
    try:
        with open(path, encoding="utf-8") as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue
                try:
                    line_parts = line.split(',')
                    salary = int(line_parts[1])
                except (IndexError, ValueError):
                    print(f"Invalid line skipped: {line}")
                    continue
                total += salary
                workers_counter += 1
    except FileNotFoundError:
        print(f"File not found: {path}")
        return 0, 0
    except (OSError, UnicodeDecodeError):
        print(f"Could not read file: {path}")
        return 0, 0

    return total, (total / workers_counter if workers_counter else 0)

total, average = total_salary(path)
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
