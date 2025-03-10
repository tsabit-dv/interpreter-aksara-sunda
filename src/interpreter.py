from parser import VariableAssignment, PrintStatement, Program

# 🔹 Mapping transliterasi Aksara Sunda ke huruf Latin
TRANSLIT_TABLE = {
    "ᮜᮤᮒᮨᮛᮜᮤ": "var",  # Kata "deklarasi variabel"
    "ᮞᮧᮔ᮪": "son",      # Pemisah nama variabel
    "ᮊ": "k",
    "ᮊᮦᮒ": "ket",
    "ᮊᮨᮞ᮪": "=",  # Simbol "=" dalam ekspresi
    "ᮕᮜ᮪ᮒᮦᮔ᮪": "print",
}

def transliterate(text, silent_mode=False):
    """ Mengubah teks Aksara Sunda ke huruf Latin sebelum dieksekusi """
    debug_before = text  # Simpan sebelum diubah

    for aksara in sorted(TRANSLIT_TABLE.keys(), key=len, reverse=True):
        text = text.replace(aksara, TRANSLIT_TABLE[aksara])

    # Hapus pemisah variabel yang tidak diperlukan
    text = text.replace("son", "").strip()

    # Hapus "var" jika ada di awal nama variabel
    if text.startswith("var "):
        text = text.replace("var ", "").strip()

    if not silent_mode:
        debug_log(f"🔹 Transliterate: '{debug_before}' ➡ '{text}'")

    return text

def debug_log(message, silent_mode=False):
    """ Cetak debug dalam warna redup jika silent_mode=False """
    if not silent_mode:
        print(f"\033[2m{message}\033[0m")  # Warna abu-abu


class Interpreter:
    def __init__(self, silent_mode=False):
        self.variables = {}
        self.silent_mode = silent_mode  # 🔹 Menyimpan mode silent

        
    def execute(self, ast):
        for statement in ast.statements:
            if isinstance(statement, VariableAssignment):
                name = transliterate(statement.name, self.silent_mode).strip()
                value = transliterate(statement.value, self.silent_mode).strip()

                if not name.isidentifier():
                    print(f"❌ Error: Nama variabel '{name}' tidak valid di Python")
                    continue

                try:
                    self.variables[name] = eval(value, {}, self.variables)
                    # 🔹 Sembunyikan variabel "ket" dari output
                    if name != "ket":
                        print(f"✅ Variabel '{name}' disimpan dengan nilai {self.variables[name]}")
                except Exception as e:
                    print(f"❌ Error saat evaluasi ekspresi '{value}': {e}")

            elif isinstance(statement, PrintStatement):
                expression = transliterate(statement.expression, self.silent_mode).strip()
                try:
                    result = eval(expression, {}, self.variables)
                    print(f"🖨️ Output: {result}")
                except Exception as e:
                    print(f"❌ Error evaluasi ekspresi print '{expression}': {e}")


# Contoh penggunaan interpreter
if __name__ == "__main__":
    from lexer import lexer
    from parser import parse

    code = """
    ᮜᮤᮒᮨᮛᮜᮤ ᮞᮧᮔ᮪ ᮊ ᮊᮨᮞ᮪ 10
    ᮜᮤᮒᮨᮛᮜᮤ ᮞᮧᮔ᮪ ᮊᮦᮒ ᮊᮨᮞ᮪ 5
    ᮕᮜ᮪ᮒᮦᮔ᮪(ᮊ + ᮊᮦᮒ)
    """

    tokens = lexer(code)  # 🔹 Lexer membaca kode Aksara Sunda
    ast = parse(tokens)  # 🔹 Parser mengubah ke AST
    
    interpreter = Interpreter(silent_mode=True)  # 🔹 Matikan log debug
    interpreter.execute(ast)  # 🔹 Interpreter menjalankan kode yang sudah dikonversi
