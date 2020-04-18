# Use pytest to run
import my_spi

# ============================
# Computations
# ============================


def interpret(text):
    lexer = my_spi.Lexer(text)
    parser = my_spi.Parser(lexer)
    interpreter = my_spi.Interpreter(parser)
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
