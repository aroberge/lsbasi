# Use pytest to run
import my_spi

# ============================
# Recognizing tokens
# ============================


def test_lexer_multidigit_integer():
    lexer = my_spi.Lexer("234")
    token = lexer.get_next_token()
    assert token.type == my_spi.INTEGER
    assert token.value == 234


def test_lexer_plus():
    lexer = my_spi.Lexer("+")
    token = lexer.get_next_token()
    assert token.type == my_spi.PLUS
    assert token.value == "+"


def test_lexer_minus():
    lexer = my_spi.Lexer("-")
    token = lexer.get_next_token()
    assert token.type == my_spi.MINUS
    assert token.value == "-"


def test_lexer_eof():
    lexer = my_spi.Lexer("-")
    token = lexer.get_next_token()
    token = lexer.get_next_token()
    assert token.type == my_spi.EOF


def test_lexer_whitespace():
    lexer = my_spi.Lexer("  23")
    token = lexer.get_next_token()
    assert token.type == my_spi.INTEGER
    assert token.value == 23


def test_lexer_left_paren():
    lexer = my_spi.Lexer("(")
    token = lexer.get_next_token()
    assert token.type == my_spi.LPAREN
    assert token.value == "("


def test_lexer_right_paren():
    lexer = my_spi.Lexer(")")
    token = lexer.get_next_token()
    assert token.type == my_spi.RPAREN
    assert token.value == ")"


def test_tokens_part9():
    """New tokens from part 9 or the tutorial"""
    records = (
        (':=', my_spi.ASSIGN, ':='),
        ('.', my_spi.DOT, '.'),
        ('number', my_spi.ID, 'number'),
        (';', my_spi.SEMI, ';'),
        ('BEGIN', my_spi.BEGIN, 'BEGIN'),
        ('END', my_spi.END, 'END'),
    )
    for text, tok_type, tok_val in records:
        lexer = my_spi.Lexer(text)
        token = lexer.get_next_token()
        assert token.type == tok_type
        assert token.value == tok_val


# ============================
# Lexer
# ============================


def test_lexer_addition():
    lexer = my_spi.Lexer("2+3")

    token = lexer.get_next_token()
    assert token.type == my_spi.INTEGER
    assert token.value == 2

    token = lexer.get_next_token()
    assert token.type == my_spi.PLUS
    assert token.value == "+"

    token = lexer.get_next_token()
    assert token.type == my_spi.INTEGER
    assert token.value == 3

    token = lexer.get_next_token()
    assert token.type == my_spi.EOF
    assert token.value is None


def test_lexer_subtraction():
    lexer = my_spi.Lexer(" 32 - 3  ")

    token = lexer.get_next_token()
    assert token.type == my_spi.INTEGER
    assert token.value == 32

    token = lexer.get_next_token()
    assert token.type == my_spi.MINUS
    assert token.value == "-"

    token = lexer.get_next_token()
    assert token.type == my_spi.INTEGER
    assert token.value == 3

    token = lexer.get_next_token()
    assert token.type == my_spi.EOF
    assert token.value is None
