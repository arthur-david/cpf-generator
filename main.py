from generator import generator

print("""
----------------------------------------
|                                      |
|     Welcome to the CPF Generator     |
|                                      |
----------------------------------------
""")

while True:
    print("Press 1 to generate a valid CPF. Press any other key to exit.")
    enter = input()

    if enter != "1":
        break

    num_cpf, string_cpf = generator()

    print("\nCPF generated!")
    print(f"Formatted: {string_cpf} | Unformatted: {num_cpf}")
    print("----------------------------------------------------------------\n")