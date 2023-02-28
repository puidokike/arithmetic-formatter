def arithmetic_arranger(problems, counting=False):
    # Checking the length of the problems
    if len(problems) > 5:
        return "Error: Too many problems."

    first_operand = []
    second_operand = []
    operators = []

    for problem in problems:
        str_split = problem.split()
        first_operand.append(str_split[0])
        second_operand.append(str_split[2])
        operators.append(str_split[1])

    # Testing if correct digits used:
    for num in first_operand:
        if not num.isdigit():
            return "Error: Numbers must only contain digits."
        if len(num) > 4:
            return "Error: Numbers cannot be more than four digits."

    for num in second_operand:
        if not num.isdigit():
            return "Error: Numbers must only contain digits."
        if len(num) > 4:
            return "Error: Numbers cannot be more than four digits."

    # Testing if "+" and "- used"
    for operator in operators:
        if operator == "+" or operator == "-":
            continue
        else:
            return "Error: Operator must be '+' or '-'."

    first_line = []
    second_line = []
    third_line = []
    fourth_line = []

    # Formatting first three lines
    for x in range(len(first_operand)):
        if len(first_operand[x]) > len(second_operand[x]):
            first_line.append("  " + first_operand[x])
            second_line.append(operators[x] + " " * (len(first_operand[x]) - len(second_operand[x]) + 1) + second_operand[x])
            third_line.append("-" * (len(first_operand[x]) + 2))

        elif len(first_operand[x]) < len(second_operand[x]):
            second_line.append(operators[x] + " " + second_operand[x])
            first_line.append(" " * (len(second_operand[x]) - len(first_operand[x]) + 2) + first_operand[x])
            third_line.append("-" * (len(second_operand[x]) + 2))
        else:
            first_line.append("  " + first_operand[x])
            second_line.append(operators[x] + " " + second_operand[x])
            third_line.append("-" * (len(first_operand[x]) + 2))

    # Formatting the last "answer" line
    for x in range(len(first_operand)):
        if operators[x] == "+":
            answer = str(int(first_operand[x]) + int(second_operand[x]))
        else:
            answer = str(int(first_operand[x]) - int(second_operand[x]))

        if len(answer) > max(len(first_operand[x]), len(second_operand[x])):
            fourth_line.append(" " + answer)
        else:
            fourth_line.append(" " * (max(len(first_operand[x]), len(second_operand[x])) - len(answer) + 2) + answer)

    # Final Phase
    if counting:
        arranged_problems = "    ".join(first_line) + "\n" + "    ".join(second_line) + "\n" + "    ".join(third_line) + "\n" + "    ".join(fourth_line)
    else:
        arranged_problems = "    ".join(first_line) + "\n" + "    ".join(second_line) + "\n" + "    ".join(third_line)

    return arranged_problems
