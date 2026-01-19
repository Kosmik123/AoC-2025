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

class Equation:
    def __init__(self, lhs: Expression, rhs: Expression):
        self.lhs = lhs
        self.rhs = rhs

    def __str__(self):
        return f"{self.lhs} = {self.rhs}"

    def get_expression(self, unknown: str) -> Expression:
        if not unknown in self.lhs and not unknown in self.rhs:
            return None
         
        rhs_terms: dict[str, int] = {}
        lhs_coeff = 0
        if unknown in self.lhs:
            lhs_coeff += self.lhs.terms[unknown]
        
        for other, coeff in self.lhs.terms.items():
            if other == unknown:
                continue
            rhs_terms[other] = -coeff     
        
        if unknown in self.rhs:
            lhs_coeff -= self.rhs.terms[unknown]
            
        for other, coeff in self.rhs.terms.items():
            if other == unknown:
                continue
            if other in rhs_terms:
                rhs_terms[other] += coeff     
            else:
                rhs_terms[other] = coeff

        for term in rhs_terms:
            coeff = rhs_terms[term]
            rhs_terms[term] = coeff / lhs_coeff
        
        return Expression(rhs_terms)

