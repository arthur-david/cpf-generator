from random import randint


def generator():
    cpf = ""
    for i in range(9):
        cpf += str(randint(0, 9))

    cpf += _calculator_cpf(cpf)
    cpf += _calculator_cpf(cpf)

    string_cpf = cpf[:3] + "." + cpf[3:6] + "." + cpf[6:9] + "-" + cpf[9:]
    cpf = int(cpf)

    return cpf, string_cpf


def _calculator_cpf(cpf):
    counts = []
    start = 11 if len(cpf) > 9 else 10
    for i, v in enumerate(range(start, 1, -1)):
        num = int(cpf[i]) * v
        counts.append(num)

    total = sum(counts)
    num_generated = 11 - (total % 11)
    return "0" if num_generated > 9 else str(num_generated)
