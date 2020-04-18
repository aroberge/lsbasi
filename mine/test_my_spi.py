# Use pytest to run
import my_spi


def make_interpreter(text):
    lexer = my_spi.Lexer(text)
    parser = my_spi.Parser(lexer)
    return my_spi.Interpreter(parser)


def test_arithmetic_expressions():
    for expr, result in (
        ('3', 3),
        ('2 + 7 * 4', 30),
        ('7 - 8 / 4', 5),
        ('14 + 2 * 3 - 6 / 2', 17),
        ('7 + 3 * (10 / (12 / (3 + 1) - 1))', 22),
        ('7 + 3 * (10 / (12 / (3 + 1) - 1)) / (2 + 3) - 5 - 3 + (8)', 10),
        ('7 + (((3 + 2)))', 12),
        ('- 3', -3),
        ('+ 3', 3),
        ('5 - - - + - 3', 8),
        ('5 - - - + - (3 + 4) - +2', 10),
    ):
        interpreter = make_interpreter('BEGIN a := %s END.' % expr)
        interpreter.interpret()
        assert interpreter.GLOBAL_SCOPE['a'] == result


def test_statements():
    text = """
    BEGIN

        BEGIN
            number := 2;
            a := number;
            b := 10 * a + 10 * number / 4;
            c := a - - b
        END;

        x := 11;
    END.
    """
    interpreter = make_interpreter(text)
    interpreter.interpret()
    globals = interpreter.GLOBAL_SCOPE
    assert len(globals) == 5
    assert globals['number'] == 2
    assert globals['a'] == 2
    assert globals['b'] == 25
    assert globals['c'] == 27
    assert globals['x'] == 11


def test_expression_invalid_syntax1():
    interpreter = make_interpreter('BEGIN a := 10 * ; END.')
    syntax_error = False
    try:
        interpreter.interpret()
    except Exception:
        syntax_error = True
    assert syntax_error


def test_expression_invalid_syntax2():
    interpreter = make_interpreter('BEGIN a := 1 (1 + 2); END.')
    syntax_error = False
    try:
        interpreter.interpret()
    except Exception:
        syntax_error = True
    assert syntax_error
