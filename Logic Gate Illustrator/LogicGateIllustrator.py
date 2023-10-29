try:
    from termcolor import colored
except ImportError:
    print("Please install 'termcolor' for a better experience. Continuing without colors.")
    def colored(text, color=None):
        return text

def nor_gate(input_1: int, input_2: int) -> int:
    return int(input_1 == input_2 == 0)

def and_gate(input_1: int, input_2: int) -> int:
    return int((input_1, input_2).count(0) == 0)

def nand_gate(input_1: int, input_2: int) -> int:
    return int((input_1, input_2).count(0) != 0)

def not_gate(input_1: int) -> int:
    return 1 if input_1 == 0 else 0

def or_gate(input_1: int, input_2: int) -> int:
    return int((input_1, input_2).count(1) != 0)

def xnor_gate(input_1: int, input_2: int) -> int:
    return 1 if input_1 == input_2 else 0

def xor_gate(input_1: int, input_2: int) -> int:
    return (input_1, input_2).count(0) % 2

def get_user_input(gate_func):
    if gate_func == not_gate:
        while True:
            try:
                a = int(input("\nEnter value for Input A (0 or 1): "))
                if a not in [0, 1]:
                    raise ValueError
                return a, None
            except ValueError:
                print(colored("Invalid input. Please enter 0 or 1.", "red"))
    else:
        while True:
            try:
                a = int(input("\nEnter value for Input A (0 or 1): "))
                b = int(input("Enter value for Input B (0 or 1): "))
                if a not in [0, 1] or b not in [0, 1]:
                    raise ValueError
                return a, b
            except ValueError:
                print(colored("Invalid input. Please enter 0 or 1 for both inputs.", "red"))

def main():
    print(colored("In this Logic Gate Illustrator:", "cyan"))
    print(colored("1 represents True", "green"))
    print(colored("0 represents False", "red"))
    print("-----------------------------\n")

    while True:
        print("\nLogic Gate Illustrator")
        print("1. NOR Gate")
        print("2. AND Gate")
        print("3. NAND Gate")
        print("4. NOT Gate")
        print("5. OR Gate")
        print("6. XNOR Gate")
        print("7. XOR Gate")
        print("8. Exit")
        choice = input(colored("Select an option: ", "yellow"))

        gate_funcs = {
            "1": nor_gate,
            "2": and_gate,
            "3": nand_gate,
            "4": not_gate,
            "5": or_gate,
            "6": xnor_gate,
            "7": xor_gate
        }

        if choice in gate_funcs:
            a, b = get_user_input(gate_funcs[choice])
            if b is None:
                print(colored(f"Output (Q): {gate_funcs[choice](a)}", "magenta"))
            else:
                print(colored(f"Output (Q): {gate_funcs[choice](a, b)}", "magenta"))
        elif choice == "8":
            print(colored("Exiting...", "cyan"))
            break
        else:
            print(colored("Invalid choice. Please try again.", "red"))

if __name__ == "__main__":
    main()
