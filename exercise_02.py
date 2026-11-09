
path = "cats.txt"
def get_cats_info(path: str) -> list:
    result = []

    try:
        with open(path, encoding="utf-8") as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue
                try:
                    cat_id, cat_name, cat_age = line.split(',')
                except ValueError:
                    print(f"Invalid line skipped: {line}")
                    continue
                result.append({"id": cat_id, "name": cat_name, "age": cat_age})
    except FileNotFoundError:
        print(f"File not found: {path}")
    except (OSError, UnicodeDecodeError):
        print(f"Could not read file: {path}")

    return result

cats_info = get_cats_info(path)
print(cats_info)
