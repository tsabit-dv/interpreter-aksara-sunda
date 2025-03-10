import re
from lexer import TokenType
from ast_custom import VariableAssignment, PrintStatement, Program

# 🔹 Regex untuk menangkap deklarasi variabel
var_assign_pattern = re.compile(r"ᮜᮤᮒᮨᮛᮜᮤ\s*ᮞᮧᮔ᮪\s*([\u1B80-\u1BBF]+)\s*ᮊᮨᮞ᮪\s*(.+)")

class LogicalOperation:
    def __init__(self, keyword, expression):
        self.keyword = keyword  # Contohnya 'ᮃᮔ᮪ᮓᮨᮕᮤᮊ᮪' untuk IF
        self.expression = expression  # Contohnya 'ᮕᮜ᮪ᮒᮦᮔ᮪(ᮊ + ᮊᮦᮒ)'

    def __repr__(self):
        return f"LogicalOperation({self.keyword}, {self.expression})"

class ASTNode:
    """ Kelas dasar untuk node dalam AST """
    pass

class Program:
    """ Node utama yang merepresentasikan seluruh program """
    def __init__(self, statements):
        self.statements = statements  # List dari node AST

class VariableAssignment(ASTNode):
    """ Node untuk deklarasi variabel """
    def __init__(self, name, value):
        self.name = name
        self.value = value

class PrintStatement(ASTNode):
    """ Node untuk statement print """
    def __init__(self, expression):
        self.expression = expression

def parse(tokens):
    ast = []

    for token in tokens:
        token_type, value = token

        if token_type == TokenType.VAR_ASSIGN:
            match = re.match(r"([\u1B80-\u1BBF\s]+)\s*ᮊᮨᮞ᮪\s*(.+)", value)
            if match:
                var_name, var_value = match.groups()
                ast.append(VariableAssignment(var_name.strip(), var_value.strip()))
            else:
                print(f"❌ Parsing Error: Gagal membaca VAR_ASSIGN -> {value}")

        elif token_type == TokenType.PRINT:
            expression_match = re.match(r"ᮕᮜ᮪ᮒᮦᮔ᮪\((.+)\)", value)
            if expression_match:
                expression = expression_match.group(1)
                ast.append(PrintStatement(expression.strip()))
            else:
                print(f"❌ Parsing Error: Gagal membaca PRINT -> {value}")

        elif token_type == TokenType.KEYWORD:
            parts = value.split(" ", 1)
            if len(parts) == 2:
                keyword, expression = parts
                ast.append(LogicalOperation(keyword.strip(), expression.strip()))
            else:
                print(f"❌ Parsing Error: Gagal membaca KEYWORD -> {value}")

    return Program(ast)  # Kembalikan sebagai objek Program

tokens = [
    ("VAR_ASSIGN", "ᮜᮤᮒᮨᮛᮜᮤ ᮞᮧᮔ᮪ ᮊ ᮊᮨᮞ᮪ 10"),
    ("VAR_ASSIGN", "ᮜᮤᮒᮨᮛᮜᮤ ᮞᮧᮔ᮪ ᮊᮦᮒ ᮊᮨᮞ᮪ 5"),
    ("PRINT", "ᮕᮜ᮪ᮒᮦᮔ᮪(ᮊ + ᮊᮦᮒ)")
]

statements = parse(tokens)
print("\n🔹 Hasil Parsing:", statements)

if __name__ == "__main__":
    from lexer import lexer

    code = """
    ᮜᮤᮒᮨᮛᮜᮤ ᮞᮧᮔ᮪ ᮊ ᮊᮨᮞ᮪ 10
    ᮜᮤᮒᮨᮛᮜᮤ ᮞᮧᮔ᮪ ᮊᮦᮒ ᮊᮨᮞ᮪ 5
    ᮃᮔ᮪ᮓᮨᮕᮤᮊ᮪ ᮕᮜ᮪ᮒᮦᮔ᮪(ᮊ + ᮊᮦᮒ)
    """

    tokens = lexer(code)
    ast = parse(tokens)
    print(ast.statements)
