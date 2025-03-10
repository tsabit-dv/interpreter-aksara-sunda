class VariableAssignment:
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def __repr__(self):
        return f"VariableAssignment(name={self.name}, value={self.value})"

class PrintStatement:
    def __init__(self, expression):
        self.expression = expression

    def __repr__(self):
        return f"PrintStatement(expression={self.expression})"

class Program:
    def __init__(self, statements):
        self.statements = statements

    def __repr__(self):
        return f"Program({self.statements})"

    def add_statement(self, stmt):
        self.statements.append(stmt)

    def __repr__(self):
        return f"Program(statements={self.statements})"

