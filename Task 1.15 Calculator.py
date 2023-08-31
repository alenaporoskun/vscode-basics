result = 0

operand = None
operator = None
wait_for_number = True

ind = 0
while True:
    i = input()
    if i == '=':
        result = float(result)
        print('Result:', result)
        break

    if i not in ('+', '-', '/', '*') and wait_for_number:    
        try:
            operand = int(i)
            wait_for_number = False
        except ValueError:
                print(f'{i} is not a number. Try again.')
        else:
            if ind == 0:
                result = operand
                ind += 1
                
            if operator == '+':
                result += operand
            elif operator == '-':
                result -= operand
            elif operator == '/':
                result /= operand
            elif operator == '*':
                result *= operand

    elif i in ('+', '-', '/', '*') and wait_for_number:
        print(f'{i} is not a number. Try again.')
    elif i not in ('+', '-', '/', '*') and not wait_for_number:
        print(f"{i} is not '+' or '-' or '/' or '*'. Try again.")
    elif i in ('+', '-', '/', '*') and not wait_for_number:
        wait_for_number = True
        operator = i