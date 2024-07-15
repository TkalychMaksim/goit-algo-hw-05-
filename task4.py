def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Error. Phone number should be numeric"
        except KeyError:
            return "Error. Contact with this name does not exist"
        except IndexError as exc:
            return str(exc)
    return inner
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args
@input_error
def add_contact(args, contacts):
    if len(args) != 2:
        raise IndexError("Enter both name and phone number")
    name, phone = args
    if not phone.isdigit():
        raise ValueError
    contacts[name] = phone
    return "Contact added."
@input_error
def change_contact(args, contacts):
    if len(args) != 2:
        raise IndexError("Enter both name and phone number")
    name, phone = args
    if not phone.isdigit():
        raise ValueError
    if name not in contacts:
        raise KeyError
    contacts[name] = phone
    return "Contact number was changed."
@input_error
def phone_contact(args,contacts):
    if len(args) != 1:
        raise IndexError("Enter the name of the contact")
    name = args[0]
    if name not in contacts:
        raise KeyError
    return contacts[name]
def all_contacts(contacts):
    contact_list = "\n".join(f"{name}: {phone}" for name, phone in contacts.items())
    return f"Contacts:\n{contact_list}"
    
def main():
    # Init dict for contacts
    contacts = {}
    print("Welcome to the assistant bot :3")
    while True:
        user_input = input("Enter the command: ")
        command, *args = parse_input(user_input)
        match command:
            case "hello": print("How I can help you?")
            case "exit" | "end": 
                print("Good Bye!") 
                break
            case "add":
                print(add_contact(args,contacts))
            case "change":
                print(change_contact(args,contacts))
            case "phone":
                print(phone_contact(args,contacts))
            case "all":
                print(all_contacts(contacts))
            case _:
                print("Command does not exist")
                 

if __name__ == "__main__":
    main()
