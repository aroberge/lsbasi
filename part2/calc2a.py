"""Modified from calc2.py to do the following:

1. Extend the calculator to handle multiplication of two integers
2. Extend the calculator to handle division of two integers
3. Modify the code to interpret expressions containing an arbitrary
   number of additions and subtractions, for example “9 - 5 + 3 + 11”
"""
# Token types
# EOF (end-of-file) token is used to indicate that
# there is no more input left for lexical analysis
INTEGER, PLUS, MINUS, MULT, DIV, EOF = (
    "INTEGER",
    "PLUS",
    "MINUS",
    "MULT",
    "DIV",
    "EOF",
)


class Token(object):
    def __init__(self, type, value):
        # token type: INTEGER, PLUS, MINUS, or EOF
        self.type = type
        # token value: non-negative integer value, '+', '-', or None
        self.value = value

    def __str__(self):
        """String representation of the class instance.

        Examples:
            Token(INTEGER, 3)
            Token(PLUS '+')
        """
        return "Token({type}, {value})".format(type=self.type, value=repr(self.value))

    def __repr__(self):
        return self.__str__()


class Interpreter(object):
    def __init__(self, text):
        # client string input, e.g. "3 + 5", "12 - 5", etc
        self.text = text
        # self.pos is an index into self.text
        self.pos = 0
        # current token instance
        self.current_token = None
        self.current_char = self.text[self.pos]

    def error(self):
        raise Exception("Error parsing input")

    def advance(self):
        """Advance the 'pos' pointer and set the 'current_char' variable."""
        self.pos += 1
        if self.pos > len(self.text) - 1:
            self.current_char = None  # Indicates end of input
        else:
            self.current_char = self.text[self.pos]

    def skip_whitespace(self):
        while self.current_char is not None and self.current_char.isspace():
            self.advance()

    def integer(self):
        """Return a (multidigit) integer consumed from the input."""
        result = ""
        while self.current_char is not None and self.current_char.isdigit():
            result += self.current_char
            self.advance()
        return int(result)

    def get_next_token(self):
        """Lexical analyzer (also known as scanner or tokenizer)

        This method is responsible for breaking a sentence
        apart into tokens.
        """
        while self.current_char is not None:

            if self.current_char.isspace():
                self.skip_whitespace()
                continue

            if self.current_char.isdigit():
                return Token(INTEGER, self.integer())

            if self.current_char == "+":
                self.advance()
                return Token(PLUS, "+")

            if self.current_char == "-":
                self.advance()
                return Token(MINUS, "-")

            if self.current_char == "*":
                self.advance()
                return Token(MULT, "*")

            if self.current_char == "/":
                self.advance()
                return Token(DIV, "/")

            self.error()

        return Token(EOF, None)

    def eat(self, token_type):
        # compare the current token type with the passed token
        # type and if they match then "eat" the current token
        # and assign the next token to the self.current_token,
        # otherwise raise an exception.
        if self.current_token.type == token_type:
            self.current_token = self.get_next_token()
        else:
            self.error()

    def expr(self):
        """Parser / Interpreter

        expr -> INTEGER PLUS INTEGER
        expr -> INTEGER MINUS INTEGER
        """
        # set current token to the first token taken from the input
        result = None
        self.current_token = self.get_next_token()
        while True:
            if self.current_token.type == "EOF":
                return result

            if result is not None:
                left = Token("INTEGER", result)
            else:
                left = self.current_token
                self.eat(INTEGER)

            op = self.current_token
            if op.type == PLUS:
                self.eat(PLUS)
            elif op.type == "MINUS":
                self.eat(MINUS)
            elif op.type == "MULT":
                self.eat(MULT)
            elif op.type == "DIV":
                self.eat(DIV)
            else:
                self.error()

            # we expect the current token to be an integer
            right = self.current_token
            self.eat(INTEGER)
            # after the above call the self.current_token is set to
            # EOF token

            # at this point either the INTEGER PLUS INTEGER or
            # the INTEGER MINUS INTEGER sequence of tokens
            # has been successfully found and the method can just
            # return the result of adding or subtracting two integers,
            # thus effectively interpreting client input
            if op.type == PLUS:
                result = left.value + right.value
            elif op.type == MINUS:
                result = left.value - right.value
            elif op.type == MULT:
                result = left.value * right.value
            else:
                result = left.value / right.value


def main():
    while True:
        try:
            text = input("calc> ")
        except EOFError:
            break
        if not text:
            continue
        interpreter = Interpreter(text)
        result = interpreter.expr()
        print(result)


if __name__ == "__main__":
    main()
