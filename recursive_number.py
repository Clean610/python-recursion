def compute(expression):
    operators = ['+', '-', '*']
    list_of_ans = []

    # -------------- iterate to find operator and call recursive function ---------------------------------------------
    for index in range(len(expression)):

        if expression[index] in operators:
            index_op = expression[index]
            from_left_side = expression[:index]
            from_right_side = expression[index + 1:]
            left_output = recursion_number(from_left_side)
            right_output = recursion_number(from_right_side)

            # -------------- compute left side and right side value ---------------------------------------------------
            for x in left_output:
                for y in right_output:
                    if index_op == '+':
                        list_of_ans.append(x + y)
                    elif index_op == '-':
                        list_of_ans.append(x - y)
                    elif index_op == '*':
                        list_of_ans.append(x * y)
    if len(list_of_ans) == 0:
        list_of_ans.append(int(expression))
    return list_of_ans


def recursion_number(expression):
    output_number = compute(expression)
    return output_number


output = recursion_number("2-1-1")
print(f'{output = }')
