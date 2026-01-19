class Expression:
    def __init__(self, unknowns: dict[str, int] = None, value: int = 0):       
        self.terms = {} if not unknowns else dict(unknowns)
        if value != 0:
            self.terms[''] = value

    def __contains__(self, item: str) -> bool:
        return item in self.terms

    def __str__(self) -> str:
        if len(self.terms) < 1:
            return '0'
        result = ''
        for term, coeff in self.terms.items():
            if coeff == 0:
                continue
            if result != '':
                result += " + "
            if term == '':  
                result += f'{coeff}'
            else:
                if coeff != 1:
                    result += f'{coeff}'
                result += f'({term})'
        return result

    def multiply(self, mult: int):
        for term in self.terms:
            self.terms[term] = mult * self.terms[term]  

    def add(self, rhs: Expression):
        for var, coeff in rhs.terms.items():
            if var in self.terms:
                self.terms[var] += coeff
            else: 
                self.terms[var] = coeff

    def substitute(self, variable: str, substitution: Expression):
        if variable not in self.terms:
            return
        expr_copy = Expression(substitution.terms)
        expr_copy.multiply(self.terms[variable])
        self.terms.pop(variable)
        self.add(expr_copy)



class Equation:
    def __init__(self, lhs: Expression, rhs: Expression):
        self.lhs = lhs
        self.rhs = rhs

    def __str__(self):
        return f"{self.lhs} = {self.rhs}"

    def get_expression(self, variable: str) -> Expression:
        if not variable in self.lhs and not variable in self.rhs:
            return None
         
        rhs_terms: dict[str, int] = {}
        lhs_coeff = 0
        if variable in self.lhs:
            lhs_coeff += self.lhs.terms[variable]
        
        for other, coeff in self.lhs.terms.items():
            if other == variable:
                continue
            rhs_terms[other] = -coeff     
        
        if variable in self.rhs:
            lhs_coeff -= self.rhs.terms[variable]
            
        for other, coeff in self.rhs.terms.items():
            if other == variable:
                continue
            if other in rhs_terms:
                rhs_terms[other] += coeff     
            else:
                rhs_terms[other] = coeff

        for term in rhs_terms:
            coeff = rhs_terms[term]
            rhs_terms[term] = coeff / lhs_coeff
        
        return Expression(rhs_terms)



def solve(equations: list[Equation]) -> dict[str, Expression]:
    variables = set[str]()
    for eq in equations:
        for var_name in eq.lhs.terms:
            if var_name != '':
                variables.add(var_name)
        for var_name in eq.rhs.terms:
            if var_name != '':
                variables.add(var_name)
    print(variables)
