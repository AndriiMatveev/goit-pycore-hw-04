def parse_input(user_input: str) -> tuple:
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def add_contact(args: list, contacts: dict) -> str:
    if len(args) != 2:
        return "Usage: add [name] [phone]"
    name, phone = args
    contacts[name] = phone
    return "Contact added."


def change_contact(args: list, contacts: dict) -> str:
    if len(args) != 2:
        return "Usage: change [name] [new phone]"
    name, phone = args
    if name not in contacts:
        return "Contact not found."
    contacts[name] = phone
    return "Contact updated."


def show_phone(args: list, contacts: dict) -> str:
    if len(args) != 1:
        return "Usage: phone [name]"
    name = args[0]
    if name not in contacts:
        return "Contact not found."
    return contacts[name]


def show_all(contacts: dict) -> str:
    if not contacts:
        return "No contacts saved yet."
    return "\n".join(f"{name}: {phone}" for name, phone in contacts.items())


def main() -> None:
    contacts = {}
    print("Welcome to the assistant bot!")

    while True:
        user_input = input("Enter a command: ")
        if not user_input.strip():
            continue

        command, *args = parse_input(user_input)

        match command:
            case "close" | "exit":
                print("Good bye!")
                break
            case "hello":
                print("How can I help you?")
            case "add":
                print(add_contact(args, contacts))
            case "change":
                print(change_contact(args, contacts))
            case "phone":
                print(show_phone(args, contacts))
            case "all":
                print(show_all(contacts))
            case _:
                print("Invalid command.")


if __name__ == "__main__":
    main()
