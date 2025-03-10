import re
from enum import Enum

class TokenType(Enum):
    VAR_ASSIGN = "VAR_ASSIGN"
    PRINT = "PRINT"
    IDENTIFIER = "IDENTIFIER"
    NUMBER = "NUMBER"
    OPERATOR = "OPERATOR"
    KEYWORD = "KEYWORD"  # ✅ Tambahkan kategori keyword baru


# 🔍 Pola regex yang lebih lengkap
var_assign_pattern = re.compile(r"ᮜᮤᮒᮨᮛᮜᮤ\s*ᮞᮧᮔ᮪\s*([\u1B80-\u1BBF]+)\s*ᮊᮨᮞ᮪\s*(\d+)")
print_pattern = re.compile(r"ᮕᮜ᮪ᮒᮦᮔ᮪\((.+)\)")
keyword_pattern = re.compile(r"ᮃᮔ᮪ᮓᮨᮕᮤᮊ᮪")  # ✅ Deteksi kata kunci baru
identifier_pattern = re.compile(r"[\u1B80-\u1BBF]+")  # Sesuai dengan Unicode aksara Sunda
number_pattern = re.compile(r"\d+")
operator_pattern = re.compile(r"[+\-*/]")

def lexer(code):
    tokens = []
    lines = code.strip().split("\n")

    for line in lines:
        line = line.strip()
        print(f"🔍 Debug: Processing line -> {line}")  # ✅ Debugging

        if var_assign_pattern.match(line):
            tokens.append((TokenType.VAR_ASSIGN, line))
            print(f"✅ Matched VAR_ASSIGN -> {line}")  # ✅ Debugging
        elif print_pattern.match(line):
            tokens.append((TokenType.PRINT, line))
            print(f"✅ Matched PRINT -> {line}")  # ✅ Debugging
        elif keyword_pattern.match(line):  # ✅ Tangkap kata kunci baru
            tokens.append((TokenType.KEYWORD, line))
            print(f"✅ Matched KEYWORD -> {line}")  # ✅ Debugging
        else:
            print(f"❌ Lexer Error: Tidak bisa membaca '{line}'")  # ❌ Error handling

    return tokens

# 🔹 Contoh kode input
code = """
ᮜᮤᮒᮨᮛᮜᮤ ᮞᮧᮔ᮪ ᮊ ᮊᮨᮞ᮪ 10
ᮜᮤᮒᮨᮛᮜᮤ ᮞᮧᮔ᮪ ᮊᮦᮒ ᮊᮨᮞ᮪ 5
ᮕᮜ᮪ᮒᮦᮔ᮪(ᮊ + ᮊᮦᮒ)
"""

# 🔥 Jalankan lexer
tokens = lexer(code)

# ✅ Tampilkan hasil token
print("\n🔹 Tokens:")
for token in tokens:
    print(token)
