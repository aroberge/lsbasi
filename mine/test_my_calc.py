# Use pytest to run
import my_calc

# ============================
# Recognizing tokens
# ============================


def test_lexer_multidigit_integer():
    lexer = my_calc.Lexer("234")
    token = lexer.get_next_token()
    assert token.type == my_calc.INTEGER
    assert token.value == 234


def test_lexer_plus():
    lexer = my_calc.Lexer("+")
    token = lexer.get_next_token()
    assert token.type == my_calc.PLUS
    assert token.value == "+"


def test_lexer_minus():
    lexer = my_calc.Lexer("-")
    token = lexer.get_next_token()
    assert token.type == my_calc.MINUS
    assert token.value == "-"


def test_lexer_eof():
    lexer = my_calc.Lexer("-")
    token = lexer.get_next_token()
    token = lexer.get_next_token()
    assert token.type == my_calc.EOF


def test_lexer_whitespace():
    lexer = my_calc.Lexer("  23")
    token = lexer.get_next_token()
    assert token.type == my_calc.INTEGER
    assert token.value == 23


def test_lexer_left_paren():
    lexer = my_calc.Lexer("(")
    token = lexer.get_next_token()
    assert token.type == my_calc.LPAREN
    assert token.value == "("


def test_lexer_right_paren():
    lexer = my_calc.Lexer(")")
    token = lexer.get_next_token()
    assert token.type == my_calc.RPAREN
    assert token.value == ")"


# ============================
# Lexer
# ============================


def test_lexer_addition():
    lexer = my_calc.Lexer("2+3")

    token = lexer.get_next_token()
    assert token.type == my_calc.INTEGER
    assert token.value == 2

    token = lexer.get_next_token()
    assert token.type == my_calc.PLUS
    assert token.value == "+"

    token = lexer.get_next_token()
    assert token.type == my_calc.INTEGER
    assert token.value == 3

    token = lexer.get_next_token()
    assert token.type == my_calc.EOF
    assert token.value is None


def test_lexer_subtraction():
    lexer = my_calc.Lexer(" 32 - 3  ")

    token = lexer.get_next_token()
    assert token.type == my_calc.INTEGER
    assert token.value == 32

    token = lexer.get_next_token()
    assert token.type == my_calc.MINUS
    assert token.value == "-"

    token = lexer.get_next_token()
    assert token.type == my_calc.INTEGER
    assert token.value == 3

    token = lexer.get_next_token()
    assert token.type == my_calc.EOF
    assert token.value is None


# ============================
# Computations
# ============================


def interpret(text):
    lexer = my_calc.Lexer(text)
    parser = my_calc.Parser(lexer)
    interpreter = my_calc.Interpreter(parser)
    return interpreter.interpret()


def test_do_addition():
    assert interpret("10+22") == 32


def test_do_addition_with_spaces():
    assert interpret(" 3 +  2") == 5


def test_do_subtraction_with_spaces():
    assert interpret(" 33 -  22") == 11


def test_two_additions():
    assert interpret("1 + 2 + 3") == 6


def test_mixed_additions_subtractions():
    assert interpret("1 + 2 - 3") == 0


def test_do_multiplication():
    assert interpret("10 * 22") == 220


def test_do_division():
    assert interpret("220 / 10") == 22


def test_mixed_mul_div():
    assert interpret("3 * 4 / 2") == 6


def test_mixed_addition_mul():
    assert interpret("3 + 4 * 5") == 23

    assert interpret("4 * 5 + 3") == 23

    assert interpret("(3 + 4) * 5") == 35


def test_mixed_sub_div():
    assert interpret("8 - 4 / 2") == 6

    assert interpret("(8 - 4) / 2") == 2


def test_mixed_expressions():
    assert interpret("14 + 2 * 3 - 6 / 2") == 17

    assert interpret("7 + 3 * (10 / (12 / (3 + 1) - 1))") == 22

    assert interpret("7 + 3 * (10 / (12 / (3 + 1) - 1)) / (2 + 3) - 5 - 3 + (8)") == 10

    assert interpret("7 + (((3 + 2)))") == 12


def test_unary_ops():
    assert interpret("++4") == 4
    assert interpret("-4") == -4
    assert interpret("--4") == 4
    assert interpret("+-+4") == -4

