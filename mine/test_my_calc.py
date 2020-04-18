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


def test_do_addition():
    interpreter = my_calc.Interpreter("10+22")
    assert interpreter.expr() == 32


def test_do_addition_with_spaces():
    interpreter = my_calc.Interpreter(" 3 +  2")
    assert interpreter.expr() == 5


def test_do_subtraction_with_spaces():
    interpreter = my_calc.Interpreter(" 33 -  22")
    assert interpreter.expr() == 11


def test_two_additions():
    interpreter = my_calc.Interpreter("1 + 2 + 3")
    assert interpreter.expr() == 6


def test_mixed_additions_subtractions():
    interpreter = my_calc.Interpreter("1 + 2 - 3")
    assert interpreter.expr() == 0


def test_do_multiplication():
    interpreter = my_calc.Interpreter("10 * 22")
    assert interpreter.expr() == 220


def test_do_division():
    interpreter = my_calc.Interpreter("220 / 10")
    assert interpreter.expr() == 22


def test_mixed_mul_div():
    interpreter = my_calc.Interpreter("3 * 4 / 2")
    assert interpreter.expr() == 6


def test_mixed_addition_mul():
    interpreter = my_calc.Interpreter("3 + 4 * 5")
    assert interpreter.expr() == 23
    interpreter = my_calc.Interpreter("4 * 5 + 3")
    assert interpreter.expr() == 23
    interpreter = my_calc.Interpreter("(3 + 4) * 5")
    assert interpreter.expr() == 35


def test_mixed_sub_div():
    interpreter = my_calc.Interpreter("8 - 4 / 2")
    assert interpreter.expr() == 6
    interpreter = my_calc.Interpreter("(8 - 4) / 2")
    assert interpreter.expr() == 2
