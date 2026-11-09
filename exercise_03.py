import sys
from pathlib import Path
from colorama import Fore, Style, init

def print_tree(directory: Path, prefix: str = "") -> None:
    try:
        items = sorted(directory.iterdir(), key=lambda p: (p.is_file(), p.name.lower()))
    except PermissionError:
        print(f"{prefix}{Fore.RED}[access denied]{Style.RESET_ALL}")
        return

    for index, item in enumerate(items):
        is_last = index == len(items) - 1
        connector = "┗ " if is_last else "┣ "

        if item.is_dir():
            print(f"{prefix}{connector}{Fore.BLUE}📂{item.name}{Style.RESET_ALL}")
            extension = "  " if is_last else "┃ "
            print_tree(item, prefix + extension)
        else:
            print(f"{prefix}{connector}{Fore.GREEN}📜{item.name}{Style.RESET_ALL}")

def main() -> None:
    init()

    if len(sys.argv) < 2:
        print(f"{Fore.RED}Usage: python directory_tree.py <directory_path>{Style.RESET_ALL}")
        sys.exit(1)

    path = Path(sys.argv[1])

    if not path.exists():
        print(f"{Fore.RED}Error: path '{path}' does not exist.{Style.RESET_ALL}")
        sys.exit(1)

    if not path.is_dir():
        print(f"{Fore.RED}Error: '{path}' is not a directory.{Style.RESET_ALL}")
        sys.exit(1)

    print(f"{Fore.YELLOW}📦{path.resolve().name}{Style.RESET_ALL}")
    print_tree(path, " ")


if __name__ == "__main__":
    main()