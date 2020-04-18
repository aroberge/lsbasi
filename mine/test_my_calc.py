# Use pytest to run
import my_calc

# ============================
# Recognizing tokens
# ============================


def test_lexer_multidigit_integer():
    lexer = my_calc.Interpreter('234')
    token = lexer.get_next_token()
    assert token.type == my_calc.INTEGER
    assert token.value == 234


def test_lexer_plus():
    lexer = my_calc.Interpreter('+')
    token = lexer.get_next_token()
    assert token.type == my_calc.PLUS
    assert token.value == '+'


def test_lexer_minus():
    lexer = my_calc.Interpreter('-')
    token = lexer.get_next_token()
    assert token.type == my_calc.MINUS
    assert token.value == '-'


def test_lexer_eof():
    lexer = my_calc.Interpreter('-')
    token = lexer.get_next_token()
    token = lexer.get_next_token()
    assert token.type == my_calc.EOF


def test_lexer_whitespace():
    lexer = my_calc.Interpreter('  23')
    token = lexer.get_next_token()
    assert token.type == my_calc.INTEGER
    assert token.value == 23

# ============================
# Lexer
# ============================


def test_lexer_addition():
    lexer = my_calc.Interpreter('2+3')

    token = lexer.get_next_token()
    assert token.type == my_calc.INTEGER
    assert token.value == 2

    token = lexer.get_next_token()
    assert token.type == my_calc.PLUS
    assert token.value == '+'

    token = lexer.get_next_token()
    assert token.type == my_calc.INTEGER
    assert token.value == 3

    token = lexer.get_next_token()
    assert token.type == my_calc.EOF
    assert token.value is None


def test_lexer_subtraction():
    lexer = my_calc.Interpreter(' 32 - 3  ')

    token = lexer.get_next_token()
    assert token.type == my_calc.INTEGER
    assert token.value == 32

    token = lexer.get_next_token()
    assert token.type == my_calc.MINUS
    assert token.value == '-'

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
