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



input = '''123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +'''

input = load_input()

lines = input.split('\n')

for i in range(len(lines) - 1):
    line = lines[i]
    parse_numbers_line(line)

parse_operations_line(lines[-1])


grand_total = 0
for p in problems:
    answer = p.calculate()
    grand_total += answer

print(grand_total)