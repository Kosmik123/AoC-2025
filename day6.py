from helpers import load_input


class Problem:
    def __init__(self):
        self.numbers: list[int] = []
        self.operation = None

    def add(numbers: list[int]) -> int:
        result = 0
        for num in numbers:
            result += num
        return result
    
    def multiply(numbers: list[int]) -> int:
        result = 1
        for num in numbers:
            result *= num
        return result

    def calculate(self) -> int:
        if self.operation == '*':
           return Problem.multiply(self.numbers)
        elif self.operation == '+':
            return Problem.add(self.numbers)

    def __str__(self):
        return self.operation.join([str(n) for n in self.numbers])



problems: list[Problem] = []

def parse_numbers_line(line: str):
    global problems    
    str_numbers = [d for d in line.split(' ') if len(d) > 0]
    for col in range(len(str_numbers)):
        if col >= len(problems):
            problems.append(Problem())
        
        num = int(str_numbers[col].strip())
        problems[col].numbers.append(num)


def parse_operations_line(line: str):
    global problems    
    operations = [d for d in line.split(' ') if len(d) > 0]
    for col in range(len(operations)):
        problems[col].operation = operations[col].strip()


def make_number(input: list[str], col: int) -> int:
    result = 0
    for row in input:
        if col >= len(row):
            continue
        ch = row[col]
        if ch.isdigit():
            result *= 10
            result += int(ch)
    return result
    
def operation_at_column(input: list[str], col: int) -> str:
    return input[-1][col]

input = '''123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +'''

input = load_input()

lines = input.split('\n')
operation_columns: list[int] = []
column_count = len(lines[0])
for col in range(column_count):
    if col >= len(lines[-1]):
        break
    char = lines[-1][col]
    if char != ' ':
        operation_columns.append(col)

print (operation_columns)

for i in range(len(operation_columns)):
    start_col = operation_columns[i]
    end_col = (operation_columns[i + 1] - 1 if (i + 1) < len(operation_columns) else column_count) 
    new_problem = Problem()
    new_problem.operation = operation_at_column(lines, start_col)
    for col in range(start_col, end_col):
        num = make_number(lines, col)
        new_problem.numbers.append(num)

    problems.append(new_problem)

grand_total = 0
for p in problems:
    print(p)
    result = p.calculate()
    grand_total += result

print(grand_total)


